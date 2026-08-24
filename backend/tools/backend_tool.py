#!/usr/bin/env python3
"""Validate and project the Lebl-family modular backend v0.1.

Standard-library only. No network, Git, or implicit filesystem discovery.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sys
import unicodedata
import uuid
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


SCHEMA_NAME = "lebl.backend.record"
SCHEMA_VERSION = "0.1.0"
LANE_ID = "R006+R007+R008"
NAMESPACE_UUID = uuid.UUID("ccdf8f89-242c-5c81-863d-54d9fb08f872")
ID_RE = re.compile(
    r"^urn:uuid:[0-9a-f]{8}-[0-9a-f]{4}-5[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
)
KEY_RE = re.compile(r"^lebl\.(ra|diffyqs|ca|shared)\.[a-z0-9][a-z0-9._-]*$")
SHA_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
RECORD_TYPES = {
    "program",
    "course",
    "resource",
    "edition",
    "unit",
    "concept",
    "segment",
    "term",
    "asset",
    "relation",
    "rights",
    "qa_event",
    "artifact",
    "correction",
}
TYPE_DEF = {record_type: record_type for record_type in RECORD_TYPES}
TYPE_DEF["qa_event"] = "qaEvent"
BASE_REQUIRED = {
    "schema_name",
    "schema_version",
    "record_type",
    "id",
    "semantic_key",
    "semantic_aliases",
    "status",
    "recorded_at",
    "workflow_id",
    "supersedes_id",
}
TYPE_REQUIRED = {
    "program": {"title", "target_locales", "course_ids", "rights_id"},
    "course": {
        "program_id",
        "title",
        "curriculum_role",
        "prerequisite_course_ids",
        "resource_ids",
        "rights_id",
    },
    "resource": {
        "title",
        "creators",
        "original_language",
        "upstream_uri",
        "rights_id",
    },
    "edition": {
        "resource_id",
        "edition_kind",
        "revision",
        "language",
        "locale",
        "translation_state",
        "derivative_of_id",
        "build_entrypoints",
        "rights_id",
    },
    "unit": {
        "resource_id",
        "edition_id",
        "unit_kind",
        "source_local_id",
        "parent_id",
        "order_key",
        "label",
        "title",
        "source_binding",
        "locale_states",
        "concept_ids",
        "prerequisite_ids",
        "rights_id",
    },
    "concept": {"label", "definition", "notation", "source_bindings", "rights_id"},
    "segment": {
        "unit_id",
        "segment_kind",
        "order_key",
        "source_binding",
        "expressions",
        "concept_ids",
        "rights_id",
    },
    "term": {
        "concept_id",
        "language",
        "locale",
        "preferred",
        "variants",
        "rejected_forms",
        "scope_ids",
        "register",
        "evidence",
        "examples",
        "rights_id",
    },
    "asset": {
        "resource_id",
        "edition_id",
        "asset_kind",
        "path",
        "mime_type",
        "sha256",
        "source_binding",
        "dependencies",
        "rights_id",
    },
    "relation": {"subject_id", "predicate", "object_id", "order_key", "rights_id"},
    "rights": {
        "component_kind",
        "license_expression",
        "attribution",
        "change_notice_required",
        "change_notice",
        "non_endorsement",
        "third_party_status",
        "scope_ids",
    },
    "qa_event": {"check_type", "subject_ids", "result", "witness", "toolchain", "note"},
    "artifact": {
        "artifact_kind",
        "path",
        "bytes",
        "sha256",
        "toolchain",
        "produced_from_ids",
        "manifest_ids",
        "rights_id",
    },
    "correction": {
        "affected_ids",
        "defect_summary",
        "proposed_delta",
        "rationale",
        "evidence",
        "upstream_disposition",
        "rights_id",
    },
}
SUPPORT_KIND = {"hints": "hint", "answers": "answer", "solves": "solution"}


class BackendError(Exception):
    pass


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_bytes(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def normalize_nfc(value: Any) -> Any:
    if isinstance(value, str):
        return unicodedata.normalize("NFC", value)
    if isinstance(value, list):
        return [normalize_nfc(item) for item in value]
    if isinstance(value, dict):
        return {normalize_nfc(key): normalize_nfc(item) for key, item in value.items()}
    return value


def reject_floats(value: Any, where: str) -> None:
    if isinstance(value, float):
        raise BackendError(f"{where}: fractional floating-point values are forbidden")
    if isinstance(value, list):
        for index, item in enumerate(value):
            reject_floats(item, f"{where}[{index}]")
    elif isinstance(value, dict):
        for key, item in value.items():
            reject_floats(item, f"{where}.{key}")


def record_uuid(record_type: str, semantic_key: str) -> str:
    return "urn:uuid:" + str(uuid.uuid5(NAMESPACE_UUID, f"{record_type}:{semantic_key}"))


def expression_uuid(expression_key: str) -> str:
    return "urn:uuid:" + str(uuid.uuid5(NAMESPACE_UUID, f"expression:{expression_key}"))


def dataset_uuid(dataset_key: str) -> str:
    return "urn:uuid:" + str(uuid.uuid5(NAMESPACE_UUID, f"dataset:{dataset_key}"))


def load_json(path: Path) -> Any:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise BackendError(f"cannot read {path}: {exc}") from exc
    if text.startswith("\ufeff"):
        raise BackendError(f"{path}: UTF-8 BOM is forbidden")
    try:
        value = json.loads(text)
    except json.JSONDecodeError as exc:
        raise BackendError(f"{path}: invalid JSON: {exc}") from exc
    reject_floats(value, str(path))
    if normalize_nfc(value) != value:
        raise BackendError(f"{path}: strings must be Unicode NFC")
    return value


def schema_allowed_and_required(record_schema: dict[str, Any], record_type: str) -> tuple[set[str], set[str]]:
    defs = record_schema["$defs"]
    base = defs["base"]
    allowed = set(base["properties"])
    required = set(base["required"])
    entity = defs[TYPE_DEF[record_type]]
    for clause in entity["allOf"]:
        allowed.update(clause.get("properties", {}))
        required.update(clause.get("required", []))
    return allowed, required


def validate_schema_documents(backend: Path) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    paths = [
        backend / "schemas" / "record.schema.json",
        backend / "schemas" / "dataset.schema.json",
        backend / "schemas" / "projection-manifest.schema.json",
    ]
    documents = tuple(load_json(path) for path in paths)
    for path, document in zip(paths, documents):
        if document.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            raise BackendError(f"{path}: expected JSON Schema draft 2020-12")
    return documents  # type: ignore[return-value]


def validate_projection_manifest(
    manifest: dict[str, Any], schema_version: str = SCHEMA_VERSION
) -> None:
    if manifest.get("schema_name") != "lebl.backend.projection_manifest":
        raise BackendError("projection manifest: wrong schema_name")
    if manifest.get("schema_version") != schema_version:
        raise BackendError("projection manifest: wrong schema_version")
    dialect = manifest.get("csv_dialect")
    if dialect != {"encoding": "utf-8", "line_ending": "LF", "quote_all": True}:
        raise BackendError("projection manifest: unsupported CSV dialect")
    names: set[str] = set()
    files: set[str] = set()
    ordinary_types: list[str] = []
    for projection in manifest.get("projections", []):
        name = projection.get("name")
        file_name = projection.get("file_name")
        if not isinstance(name, str) or name in names:
            raise BackendError(f"projection manifest: duplicate/invalid name {name!r}")
        if not isinstance(file_name, str) or file_name in files or not file_name.endswith(".csv"):
            raise BackendError(f"projection manifest: duplicate/invalid file {file_name!r}")
        names.add(name)
        files.add(file_name)
        mode = projection.get("mode")
        if mode not in {"records", "exercise_support"}:
            raise BackendError(f"projection {name}: invalid mode")
        columns = projection.get("columns")
        if not isinstance(columns, list) or not columns:
            raise BackendError(f"projection {name}: columns missing")
        for column in columns:
            if not isinstance(column, dict) or set(column) != {"name", "source", "encoding"}:
                raise BackendError(f"projection {name}: malformed column declaration")
            if not isinstance(column["name"], str) or not isinstance(column["source"], str):
                raise BackendError(f"projection {name}: column name/source must be strings")
            if column["encoding"] not in {"scalar", "canonical_json", "record_json"}:
                raise BackendError(f"projection {name}: invalid column encoding")
        column_names = [column.get("name") for column in columns]
        if len(column_names) != len(set(column_names)):
            raise BackendError(f"projection {name}: duplicate column")
        if "record_json" not in column_names:
            raise BackendError(f"projection {name}: lossless record_json column missing")
        sort_by = projection.get("sort_by")
        if not isinstance(sort_by, list) or not sort_by or not set(sort_by).issubset(column_names):
            raise BackendError(f"projection {name}: sort_by must name projected columns")
        if mode == "records":
            ordinary_types.extend(projection.get("record_types", []))
    counts = Counter(ordinary_types)
    if set(counts) != RECORD_TYPES or any(count != 1 for count in counts.values()):
        raise BackendError("ordinary projections must cover every record type exactly once")
    if "exercise_support" not in names:
        raise BackendError("projection manifest: exercise_support view missing")


def load_records(path: Path) -> tuple[list[dict[str, Any]], bytes]:
    try:
        data = path.read_bytes()
    except OSError as exc:
        raise BackendError(f"cannot read {path}: {exc}") from exc
    if data.startswith(b"\xef\xbb\xbf"):
        raise BackendError(f"{path}: UTF-8 BOM is forbidden")
    if not data or not data.endswith(b"\n"):
        raise BackendError(f"{path}: JSONL must be nonempty and end with LF")
    if b"\r" in data:
        raise BackendError(f"{path}: CR bytes are forbidden")
    records: list[dict[str, Any]] = []
    for line_number, raw_line in enumerate(data.splitlines(), 1):
        if not raw_line:
            raise BackendError(f"{path}:{line_number}: blank line")
        try:
            line = raw_line.decode("utf-8")
            record = json.loads(line)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise BackendError(f"{path}:{line_number}: invalid UTF-8 JSON: {exc}") from exc
        reject_floats(record, f"{path}:{line_number}")
        if not isinstance(record, dict):
            raise BackendError(f"{path}:{line_number}: record must be an object")
        if normalize_nfc(record) != record:
            raise BackendError(f"{path}:{line_number}: strings must be Unicode NFC")
        if line != canonical_json(record):
            raise BackendError(f"{path}:{line_number}: record is not canonical JSON")
        records.append(record)
    expected_order = sorted(records, key=lambda item: (item.get("record_type", ""), item.get("id", "")))
    if records != expected_order:
        raise BackendError(f"{path}: records are not sorted by (record_type, id)")
    return records, data


def add_reference(references: list[tuple[str, str]], value: Any, where: str) -> None:
    if value is None:
        return
    if not isinstance(value, str) or not ID_RE.fullmatch(value):
        raise BackendError(f"{where}: invalid referenced ID")
    references.append((value, where))


def add_references(references: list[tuple[str, str]], values: Any, where: str) -> None:
    if not isinstance(values, list):
        raise BackendError(f"{where}: expected ID array")
    for index, value in enumerate(values):
        add_reference(references, value, f"{where}[{index}]")


def validate_records(
    records: list[dict[str, Any]],
    record_schema: dict[str, Any],
    schema_version: str = SCHEMA_VERSION,
) -> dict[str, Any]:
    by_id: dict[str, dict[str, Any]] = {}
    semantic_keys: set[str] = set()
    expression_ids: dict[str, tuple[dict[str, Any], dict[str, Any]]] = {}
    references: list[tuple[str, str]] = []

    for record in records:
        record_type = record.get("record_type")
        if record_type not in RECORD_TYPES:
            raise BackendError(f"record {record.get('id')}: invalid record_type {record_type!r}")
        allowed, schema_required = schema_allowed_and_required(record_schema, record_type)
        required = BASE_REQUIRED | TYPE_REQUIRED[record_type] | schema_required
        missing = sorted(required - set(record))
        unexpected = sorted(set(record) - allowed)
        if missing:
            raise BackendError(f"{record_type} {record.get('id')}: missing fields {missing}")
        if unexpected:
            raise BackendError(f"{record_type} {record.get('id')}: unexpected fields {unexpected}")
        if record["schema_name"] != SCHEMA_NAME or record["schema_version"] != schema_version:
            raise BackendError(f"{record_type} {record.get('id')}: schema identity mismatch")
        record_id = record["id"]
        key = record["semantic_key"]
        if not isinstance(record_id, str) or not ID_RE.fullmatch(record_id):
            raise BackendError(f"{record_type} {record_id!r}: invalid UUID URN")
        if not isinstance(key, str) or not KEY_RE.fullmatch(key):
            raise BackendError(f"{record_type} {record_id}: invalid semantic_key")
        if record_id != record_uuid(record_type, key):
            raise BackendError(f"{record_type} {record_id}: UUIDv5 does not match semantic_key")
        if record_id in by_id:
            raise BackendError(f"duplicate record ID {record_id}")
        if key in semantic_keys:
            raise BackendError(f"duplicate semantic_key {key}")
        by_id[record_id] = record
        semantic_keys.add(key)
        aliases = record["semantic_aliases"]
        if not isinstance(aliases, list) or len(aliases) != len(set(aliases)):
            raise BackendError(f"{record_id}: semantic_aliases must be a unique array")
        if key in aliases:
            raise BackendError(f"{record_id}: current semantic_key cannot also be an alias")
        if record["supersedes_id"] is not None:
            add_reference(references, record["supersedes_id"], f"{record_id}.supersedes_id")

        rights_id = record.get("rights_id")
        if rights_id is not None:
            add_reference(references, rights_id, f"{record_id}.rights_id")

        if record_type == "program":
            add_references(references, record["course_ids"], f"{record_id}.course_ids")
        elif record_type == "course":
            add_reference(references, record["program_id"], f"{record_id}.program_id")
            add_references(references, record["prerequisite_course_ids"], f"{record_id}.prerequisite_course_ids")
            add_references(references, record["resource_ids"], f"{record_id}.resource_ids")
        elif record_type == "edition":
            add_reference(references, record["resource_id"], f"{record_id}.resource_id")
            add_reference(references, record["derivative_of_id"], f"{record_id}.derivative_of_id")
        elif record_type == "unit":
            add_reference(references, record["resource_id"], f"{record_id}.resource_id")
            add_reference(references, record["edition_id"], f"{record_id}.edition_id")
            add_reference(references, record["parent_id"], f"{record_id}.parent_id")
            add_references(references, record["concept_ids"], f"{record_id}.concept_ids")
            add_references(references, record["prerequisite_ids"], f"{record_id}.prerequisite_ids")
            binding = record["source_binding"]
            add_reference(references, binding.get("edition_id"), f"{record_id}.source_binding.edition_id")
            if record["unit_kind"] == "exercise" and "exercise_metadata" not in record:
                raise BackendError(f"{record_id}: exercise_metadata is required for exercises")
            for index, state in enumerate(record["locale_states"]):
                add_reference(references, state.get("edition_id"), f"{record_id}.locale_states[{index}].edition_id")
        elif record_type == "concept":
            for index, binding in enumerate(record["source_bindings"]):
                add_reference(references, binding.get("edition_id"), f"{record_id}.source_bindings[{index}].edition_id")
        elif record_type == "segment":
            add_reference(references, record["unit_id"], f"{record_id}.unit_id")
            add_references(references, record["concept_ids"], f"{record_id}.concept_ids")
            binding = record["source_binding"]
            add_reference(references, binding.get("edition_id"), f"{record_id}.source_binding.edition_id")
            sources = []
            for index, expression in enumerate(record["expressions"]):
                where = f"{record_id}.expressions[{index}]"
                expression_id = expression.get("expression_id")
                expression_key = expression.get("expression_key")
                if not isinstance(expression_key, str) or not KEY_RE.fullmatch(expression_key):
                    raise BackendError(f"{where}: invalid expression_key")
                if expression_id != expression_uuid(expression_key):
                    raise BackendError(f"{where}: expression UUIDv5 mismatch")
                if expression_id in by_id or expression_id in expression_ids:
                    raise BackendError(f"{where}: duplicate expression_id")
                expression_ids[expression_id] = (record, expression)
                add_reference(references, expression.get("edition_id"), f"{where}.edition_id")
                add_reference(references, expression.get("rights_id"), f"{where}.rights_id")
                if not SHA_RE.fullmatch(expression.get("content_sha256", "")):
                    raise BackendError(f"{where}: invalid content_sha256")
                actual_hash = sha256_bytes(expression.get("content", "").encode("utf-8"))
                if actual_hash != expression["content_sha256"]:
                    raise BackendError(f"{where}: content_sha256 mismatch")
                if expression.get("role") == "source":
                    sources.append(expression)
                    if expression.get("translation_of_expression_id") is not None:
                        raise BackendError(f"{where}: source cannot translate another expression")
                    if expression.get("translation_state") != "source_frozen":
                        raise BackendError(f"{where}: source must have state source_frozen")
                else:
                    add_reference(
                        references,
                        expression.get("translation_of_expression_id"),
                        f"{where}.translation_of_expression_id",
                    )
                    if expression.get("translation_state") == "source_frozen":
                        raise BackendError(f"{where}: localized expression cannot be source_frozen")
            if len(sources) != 1:
                raise BackendError(f"{record_id}: segment must contain exactly one source expression")
            if sources[0]["content_sha256"] != binding.get("content_sha256"):
                raise BackendError(f"{record_id}: source binding hash must match source expression")
        elif record_type == "term":
            add_reference(references, record["concept_id"], f"{record_id}.concept_id")
            add_references(references, record["scope_ids"], f"{record_id}.scope_ids")
        elif record_type == "asset":
            add_reference(references, record["resource_id"], f"{record_id}.resource_id")
            add_reference(references, record["edition_id"], f"{record_id}.edition_id")
            add_references(references, record["dependencies"], f"{record_id}.dependencies")
            add_reference(
                references, record["source_binding"].get("edition_id"), f"{record_id}.source_binding.edition_id"
            )
        elif record_type == "relation":
            add_reference(references, record["subject_id"], f"{record_id}.subject_id")
            add_reference(references, record["object_id"], f"{record_id}.object_id")
        elif record_type == "rights":
            add_references(references, record["scope_ids"], f"{record_id}.scope_ids")
        elif record_type == "qa_event":
            add_references(references, record["subject_ids"], f"{record_id}.subject_ids")
        elif record_type == "artifact":
            add_references(references, record["produced_from_ids"], f"{record_id}.produced_from_ids")
            add_references(references, record["manifest_ids"], f"{record_id}.manifest_ids")
        elif record_type == "correction":
            add_references(references, record["affected_ids"], f"{record_id}.affected_ids")
            delta = record["proposed_delta"]
            actual_hash = sha256_bytes(delta.get("after_content", "").encode("utf-8"))
            if delta.get("after_sha256") != actual_hash:
                raise BackendError(f"{record_id}: proposed_delta after_sha256 mismatch")

    all_ids = set(by_id) | set(expression_ids)
    for target, where in references:
        if target not in all_ids:
            raise BackendError(f"{where}: unresolved reference {target}")

    for record in records:
        record_id = record["id"]
        record_type = record["record_type"]
        rights_id = record.get("rights_id")
        if rights_id and by_id[rights_id]["record_type"] != "rights":
            raise BackendError(f"{record_id}.rights_id: target is not a rights record")
        if record_type == "edition":
            if by_id[record["resource_id"]]["record_type"] != "resource":
                raise BackendError(f"{record_id}: resource_id must target a resource")
            derivative = record["derivative_of_id"]
            if derivative and by_id[derivative]["record_type"] != "edition":
                raise BackendError(f"{record_id}: derivative_of_id must target an edition")
        elif record_type in {"unit", "asset"}:
            resource = by_id[record["resource_id"]]
            edition = by_id[record["edition_id"]]
            if resource["record_type"] != "resource" or edition["record_type"] != "edition":
                raise BackendError(f"{record_id}: resource/edition type mismatch")
            if edition["resource_id"] != resource["id"]:
                raise BackendError(f"{record_id}: edition belongs to another resource")
            if record["source_binding"]["edition_id"] != edition["id"]:
                raise BackendError(f"{record_id}: source_binding edition mismatch")
            if record_type == "unit":
                locales: set[str] = set()
                for state in record["locale_states"]:
                    if state["locale"] in locales:
                        raise BackendError(f"{record_id}: duplicate locale state {state['locale']}")
                    locales.add(state["locale"])
                    state_edition = by_id[state["edition_id"]]
                    if state_edition["record_type"] != "edition" or state_edition["locale"] != state["locale"]:
                        raise BackendError(f"{record_id}: locale state does not match its edition")
        elif record_type == "segment":
            unit = by_id[record["unit_id"]]
            if unit["record_type"] != "unit":
                raise BackendError(f"{record_id}: unit_id must target a unit")
            source_expression = next(item for item in record["expressions"] if item["role"] == "source")
            for expression in record["expressions"]:
                edition = by_id[expression["edition_id"]]
                if edition["record_type"] != "edition":
                    raise BackendError(f"{record_id}: expression edition must target an edition")
                if by_id[expression["rights_id"]]["record_type"] != "rights":
                    raise BackendError(f"{record_id}: expression rights_id must target rights")
                if expression["locale"] != edition["locale"] or expression["language"] != edition["language"]:
                    raise BackendError(f"{record_id}: expression locale/language must match its edition")
                if expression["role"] != "source" and expression["translation_of_expression_id"] != source_expression["expression_id"]:
                    raise BackendError(f"{record_id}: localized expression must link to this segment's source expression")
            if source_expression["edition_id"] != record["source_binding"]["edition_id"]:
                raise BackendError(f"{record_id}: source expression and source binding editions differ")
        elif record_type == "term":
            if by_id[record["concept_id"]]["record_type"] != "concept":
                raise BackendError(f"{record_id}: concept_id must target a concept")

    for record in records:
        if record["record_type"] == "program":
            for course_id in record["course_ids"]:
                course = by_id[course_id]
                if course["record_type"] != "course" or course["program_id"] != record["id"]:
                    raise BackendError(f"{record['id']}: course_ids is not reciprocal")
        elif record["record_type"] == "course":
            program = by_id[record["program_id"]]
            if program["record_type"] != "program" or record["id"] not in program["course_ids"]:
                raise BackendError(f"{record['id']}: program_id is not reciprocal")
            for resource_id in record["resource_ids"]:
                if by_id[resource_id]["record_type"] != "resource":
                    raise BackendError(f"{record['id']}: resource_ids must target resources")
            for course_id in record["prerequisite_course_ids"]:
                if by_id[course_id]["record_type"] != "course":
                    raise BackendError(f"{record['id']}: prerequisite_course_ids must target courses")

    validate_parent_cycles(records, by_id)
    coverage = validate_exercise_support(records, by_id)
    return {
        "entity_counts": dict(sorted(Counter(record["record_type"] for record in records).items())),
        "exercise_solution_coverage": dict(sorted(coverage.items())),
        "expression_count": len(expression_ids),
        "record_count": len(records),
    }


def validate_parent_cycles(records: list[dict[str, Any]], by_id: dict[str, dict[str, Any]]) -> None:
    parents = {record["id"]: record["parent_id"] for record in records if record["record_type"] == "unit"}
    for unit_id, parent_id in parents.items():
        if parent_id is not None and by_id[parent_id]["record_type"] != "unit":
            raise BackendError(f"{unit_id}: parent_id must target a unit")
        seen = {unit_id}
        cursor = parent_id
        while cursor is not None:
            if cursor in seen:
                raise BackendError(f"{unit_id}: cycle in unit parent chain")
            seen.add(cursor)
            cursor = parents.get(cursor)


def build_support(records: Iterable[dict[str, Any]]) -> dict[str, dict[str, list[str]]]:
    support: dict[str, dict[str, list[str]]] = defaultdict(lambda: {"hint_ids": [], "answer_ids": [], "solution_ids": []})
    field_by_predicate = {"hints": "hint_ids", "answers": "answer_ids", "solves": "solution_ids"}
    for record in records:
        if record["record_type"] == "relation" and record["predicate"] in field_by_predicate:
            support[record["object_id"]][field_by_predicate[record["predicate"]]].append(record["subject_id"])
    for item in support.values():
        for values in item.values():
            values.sort()
    return support


def inferred_solution_status(item: dict[str, list[str]]) -> str:
    if item["solution_ids"]:
        return "full_solution"
    if item["answer_ids"] and item["hint_ids"]:
        return "mixed_partial"
    if item["answer_ids"]:
        return "answer_only"
    if item["hint_ids"]:
        return "hint_only"
    return "none"


def validate_exercise_support(
    records: list[dict[str, Any]], by_id: dict[str, dict[str, Any]]
) -> Counter[str]:
    support = build_support(records)
    for record in records:
        if record["record_type"] != "relation" or record["predicate"] not in SUPPORT_KIND:
            continue
        subject = by_id[record["subject_id"]]
        target = by_id[record["object_id"]]
        if subject.get("unit_kind") != SUPPORT_KIND[record["predicate"]]:
            raise BackendError(f"{record['id']}: {record['predicate']} subject has wrong unit kind")
        if target.get("unit_kind") != "exercise":
            raise BackendError(f"{record['id']}: {record['predicate']} object must be an exercise")
    coverage: Counter[str] = Counter()
    for exercise in (record for record in records if record["record_type"] == "unit" and record["unit_kind"] == "exercise"):
        declared = exercise["exercise_metadata"]["solution_status"]
        inferred = inferred_solution_status(support[exercise["id"]])
        if declared not in {inferred, "unknown"}:
            if not (declared == "not_applicable" and inferred == "none"):
                raise BackendError(
                    f"{exercise['id']}: declared solution_status {declared!r} conflicts with relations ({inferred!r})"
                )
        coverage[declared] += 1
    return coverage


def validate_dataset(backend: Path, dataset_path: Path) -> tuple[dict[str, Any], list[dict[str, Any]], dict[str, Any]]:
    record_schema, dataset_schema, _projection_schema = validate_schema_documents(backend)
    dataset = load_json(dataset_path)
    required = {
        "schema_name",
        "schema_version",
        "dataset_id",
        "dataset_key",
        "lane_id",
        "namespace_uuid",
        "authority_status",
        "fixture",
        "generated_at",
        "workflow_id",
        "canonicalization",
        "projection_manifest",
        "record_streams",
        "resource_ids",
        "edition_ids",
    }
    missing = sorted(required - set(dataset))
    if missing:
        raise BackendError(f"dataset manifest: missing fields {missing}")
    schema_version = dataset.get("schema_version")
    declared_dataset_version = dataset_schema.get("properties", {}).get("schema_version", {}).get("const")
    declared_record_version = (
        record_schema.get("$defs", {}).get("base", {}).get("properties", {}).get("schema_version", {}).get("const")
    )
    if (
        dataset["schema_name"] != "lebl.backend.dataset"
        or not isinstance(schema_version, str)
        or schema_version != declared_dataset_version
        or schema_version != declared_record_version
    ):
        raise BackendError("dataset manifest: schema identity mismatch")
    if dataset["lane_id"] != LANE_ID or dataset["namespace_uuid"] != str(NAMESPACE_UUID):
        raise BackendError("dataset manifest: lane or namespace mismatch")
    if dataset["dataset_id"] != dataset_uuid(dataset["dataset_key"]):
        raise BackendError("dataset manifest: dataset UUIDv5 mismatch")
    if dataset.get("fixture") and dataset.get("authority_status") != "illustrative_only":
        raise BackendError("fixture dataset must be illustrative_only")
    if dataset.get("fixture") and not dataset.get("notice"):
        raise BackendError("fixture dataset must carry a notice")
    if dataset["canonicalization"] != {"csv": "ILCSV-0.1", "json": "ILJCS-0.1"}:
        raise BackendError("dataset manifest: unsupported canonicalization")

    projection_path = (dataset_path.parent / dataset["projection_manifest"]["path"]).resolve()
    projection_bytes = projection_path.read_bytes()
    if sha256_bytes(projection_bytes) != dataset["projection_manifest"]["sha256"]:
        raise BackendError("dataset manifest: projection manifest hash mismatch")
    projection_manifest = load_json(projection_path)
    validate_projection_manifest(projection_manifest, schema_version)

    records: list[dict[str, Any]] = []
    for stream in dataset["record_streams"]:
        stream_path = (dataset_path.parent / stream["path"]).resolve()
        stream_records, stream_bytes = load_records(stream_path)
        if len(stream_bytes) != stream["bytes"]:
            raise BackendError(f"{stream_path}: byte count mismatch")
        if len(stream_records) != stream["record_count"]:
            raise BackendError(f"{stream_path}: record count mismatch")
        if sha256_bytes(stream_bytes) != stream["sha256"]:
            raise BackendError(f"{stream_path}: SHA-256 mismatch")
        records.extend(stream_records)
    if records != sorted(records, key=lambda item: (item["record_type"], item["id"])):
        raise BackendError("combined record streams are not globally sorted")
    summary = validate_records(records, record_schema, schema_version)
    by_id = {record["id"]: record for record in records}
    for resource_id in dataset["resource_ids"]:
        if resource_id not in by_id or by_id[resource_id]["record_type"] != "resource":
            raise BackendError(f"dataset resource_ids contains invalid target {resource_id}")
    for edition_id in dataset["edition_ids"]:
        if edition_id not in by_id or by_id[edition_id]["record_type"] != "edition":
            raise BackendError(f"dataset edition_ids contains invalid target {edition_id}")
    summary.update(
        {
            "authority_status": dataset["authority_status"],
            "dataset_id": dataset["dataset_id"],
            "fixture": dataset["fixture"],
            "schema_documents": 3,
        }
    )
    return projection_manifest, records, summary


def get_path(value: dict[str, Any], path: str) -> Any:
    cursor: Any = value
    for part in path.split("."):
        if not isinstance(cursor, dict) or part not in cursor:
            return None
        cursor = cursor[part]
    return cursor


def scalar_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (str, int)):
        return str(value)
    raise BackendError(f"cannot scalar-project {type(value).__name__}")


def projected_value(source_object: dict[str, Any], column: dict[str, str]) -> str:
    source = column["source"]
    encoding = column["encoding"]
    if source == "$record" or source == "$exercise":
        value: Any = source_object
    elif source.startswith("$exercise."):
        value = get_path(source_object["$exercise"], source[len("$exercise.") :])
    elif source.startswith("$support."):
        value = get_path(source_object["$support"], source[len("$support.") :])
    else:
        value = get_path(source_object, source)
    if encoding == "record_json":
        return canonical_json(value)
    if encoding == "canonical_json":
        return "" if value is None else canonical_json(value)
    return scalar_text(value)


def projection_rows(projection: dict[str, Any], records: list[dict[str, Any]]) -> tuple[list[str], list[list[str]]]:
    columns = projection["columns"]
    headers = [column["name"] for column in columns]
    if projection["mode"] == "records":
        source_objects = [record for record in records if record["record_type"] in projection["record_types"]]
    else:
        support = build_support(records)
        source_objects = [
            {"$exercise": record, "$support": support[record["id"]]}
            for record in records
            if record["record_type"] == "unit" and record["unit_kind"] == "exercise"
        ]
    rows = [[projected_value(source_object, column) for column in columns] for source_object in source_objects]
    sort_indexes = [headers.index(name) for name in projection["sort_by"]]
    rows.sort(key=lambda row: tuple(row[index] for index in sort_indexes))
    return headers, rows


def csv_text(headers: list[str], rows: list[list[str]]) -> str:
    output = io.StringIO(newline="")
    writer = csv.writer(output, quoting=csv.QUOTE_ALL, lineterminator="\n")
    writer.writerow(headers)
    writer.writerows(rows)
    return output.getvalue()


def project_csvs(
    projection_manifest: dict[str, Any], records: list[dict[str, Any]], output_dir: Path, force: bool
) -> list[dict[str, Any]]:
    output_dir.mkdir(parents=True, exist_ok=True)
    receipts: list[dict[str, Any]] = []
    for projection in projection_manifest["projections"]:
        target = output_dir / projection["file_name"]
        if target.exists() and not force:
            raise BackendError(f"refusing to overwrite {target}; pass --force explicitly")
        headers, rows = projection_rows(projection, records)
        data = csv_text(headers, rows).encode("utf-8")
        target.write_bytes(data)
        receipts.append(
            {
                "bytes": len(data),
                "file": target.name,
                "rows": len(rows),
                "sha256": sha256_bytes(data),
            }
        )
    return receipts


def roundtrip_csvs(
    projection_manifest: dict[str, Any], records: list[dict[str, Any]], csv_dir: Path
) -> dict[str, Any]:
    recovered: dict[str, dict[str, Any]] = {}
    checked_files = 0
    for projection in projection_manifest["projections"]:
        target = csv_dir / projection["file_name"]
        try:
            actual = target.read_text(encoding="utf-8")
        except OSError as exc:
            raise BackendError(f"cannot read {target}: {exc}") from exc
        headers, rows = projection_rows(projection, records)
        expected = csv_text(headers, rows)
        if actual != expected:
            raise BackendError(f"{target}: bytes do not match deterministic projection")
        checked_files += 1
        if projection["mode"] != "records":
            continue
        with target.open("r", encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                record = json.loads(row["record_json"])
                record_id = record["id"]
                if record_id in recovered:
                    raise BackendError(f"round-trip duplicate record {record_id}")
                recovered[record_id] = record
    original = {record["id"]: record for record in records}
    if recovered != original:
        missing = sorted(set(original) - set(recovered))
        extra = sorted(set(recovered) - set(original))
        changed = sorted(key for key in set(original) & set(recovered) if original[key] != recovered[key])
        raise BackendError(f"round-trip mismatch; missing={missing}, extra={extra}, changed={changed}")
    return {"checked_files": checked_files, "recovered_records": len(recovered), "roundtrip": "pass"}


def resolve_dataset(argument: str) -> Path:
    return Path(argument).expanduser().resolve()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("validate", "project", "roundtrip"):
        subparser = subparsers.add_parser(command)
        subparser.add_argument("--dataset", required=True)
    project_parser = subparsers.choices["project"]
    project_parser.add_argument("--out", required=True)
    project_parser.add_argument("--force", action="store_true")
    roundtrip_parser = subparsers.choices["roundtrip"]
    roundtrip_parser.add_argument("--csv-dir", required=True)
    id_parser = subparsers.add_parser("id")
    id_parser.add_argument("--kind", choices=("record", "expression", "dataset"), required=True)
    id_parser.add_argument("--key", required=True)
    id_parser.add_argument("--record-type", choices=sorted(RECORD_TYPES))
    args = parser.parse_args()

    if args.command == "id":
        if args.kind == "record":
            if not args.record_type:
                raise BackendError("id --kind record requires --record-type")
            result = record_uuid(args.record_type, args.key)
        elif args.kind == "expression":
            result = expression_uuid(args.key)
        else:
            result = dataset_uuid(args.key)
        print(result)
        return 0

    dataset_path = resolve_dataset(args.dataset)
    self_contained_backend = dataset_path.parent
    schema_names = ("record.schema.json", "dataset.schema.json", "projection-manifest.schema.json")
    if all((self_contained_backend / "schemas" / name).is_file() for name in schema_names):
        backend = self_contained_backend
    else:
        backend = Path(__file__).resolve().parents[1]
    projection_manifest, records, summary = validate_dataset(backend, dataset_path)
    if args.command == "validate":
        print(canonical_json(summary))
    elif args.command == "project":
        receipts = project_csvs(projection_manifest, records, Path(args.out).expanduser().resolve(), args.force)
        print(canonical_json({"projection_count": len(receipts), "receipts": receipts, "validation": summary}))
    else:
        result = roundtrip_csvs(projection_manifest, records, Path(args.csv_dir).expanduser().resolve())
        print(canonical_json({"validation": summary, **result}))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BackendError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
