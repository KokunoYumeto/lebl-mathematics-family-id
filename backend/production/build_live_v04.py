#!/usr/bin/env python3
"""Build the additive mixed-resource Lebl backend live checkpoint.

This bounded builder extends the retained v0.3 records with every live
manifest unit that was not present in that checkpoint.  It keeps R006, R007,
and R008 as separate resources/editions/rights identities and emits the same
deterministic JSONL/CSV envelope.  It never reads Git or the wider workspace.
"""

from __future__ import annotations

import copy
import csv
import hashlib
import io
import json
import os
import re
import shutil
import sys
import tempfile
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

LANE = Path(__file__).resolve().parents[2]
PRODUCTION = LANE / "backend" / "production"
V03 = PRODUCTION / "v0.3"
STAMP = "2026-08-24T00:00:00Z"
WORKFLOW = "01a01f57-a34b-7740-9717-596b8116910c/backend-production-v0.4-live"
OUT_DEFAULT = PRODUCTION / "v0.4-live-2026.08.24"

sys.path.insert(0, str(LANE / "backend" / "tools"))
import backend_tool as bt  # noqa: E402

NS = {"R006": "ra", "R007": "diffyqs", "R008": "ca"}
SOURCE_KEYS = {
    "R006": "lebl.ra.edition.v6-3",
    "R007": "lebl.diffyqs.edition.v6-11",
    "R008": "lebl.ca.edition.v1-9",
}
TARGET_KEYS = {
    "R006": "lebl.ra.edition.id-id-volume1-complete-2026-08-21",
    "R007": "lebl.diffyqs.edition.id-id-2026-08-20",
    "R008": "lebl.ca.edition.id-id-2026-08-20",
}
RESOURCE_KEYS = {role: f"lebl.{ns}.resource.primary" for role, ns in NS.items()}
RIGHTS_KEYS = {role: f"lebl.{ns}.rights.cc-by-sa-4.0" for role, ns in NS.items()}
TERMINOLOGY_FIELDS = (
    "term_id",
    "concept_id",
    "resource_scope",
    "source_term",
    "preferred_id",
    "variants_id",
    "rejected_id",
    "register",
    "evidence",
    "status",
    "notes",
)
TERM_REGISTERS = {"standard", "formal", "pedagogical", "historical", "specialized"}
O001_SCHEMA = "lebl-o001-solution-gap-v1"
O001_PATH = LANE / "00_control" / "O001_SOLUTION_GAP_LEDGER.jsonl"
MANIFEST_RIGHTS_KEYS = {
    "R006": "rights.ra.book.cc-by-sa-4.0",
    "R007": "rights.diffyqs.book.cc-by-sa-4.0",
    "R008": "rights.ca.book.cc-by-sa-4.0",
}


def sha(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def canon(value: object) -> bytes:
    return bt.canonical_json(value).encode("utf-8")


def slug(value: str) -> str:
    value = re.sub(r"[^a-z0-9._-]+", "-", value.casefold()).strip("-.")
    return value or "unit"


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> tuple[list[dict], bytes]:
    data = path.read_bytes()
    if not data.endswith(b"\n") or b"\r" in data:
        raise RuntimeError(f"non-canonical JSONL input: {path}")
    rows = [json.loads(line) for line in data.decode("utf-8").splitlines()]
    return rows, data


def load_optional_jsonl(path: Path) -> tuple[list[dict], bytes | None]:
    """Load an optional canonical JSONL witness without manufacturing bytes."""
    if not path.exists():
        return [], None
    data = path.read_bytes()
    if not data:
        return [], data
    if not data.endswith(b"\n") or b"\r" in data:
        raise RuntimeError(f"non-canonical JSONL input: {path}")
    rows = [json.loads(line) for line in data.decode("utf-8").splitlines()]
    return rows, data


def selector_bounds(selector: str) -> tuple[int, int]:
    match = re.search(r"\braw lines?\s+(\d+)(?:\s*[-–]\s*(\d+))?", selector)
    if match is None:
        raise RuntimeError(f"unsupported raw-line selector: {selector!r}")
    first = int(match.group(1))
    last = int(match.group(2) or match.group(1))
    if first < 1 or last < first:
        raise RuntimeError(f"invalid raw-line selector: {selector!r}")
    return first, last


def lane_path(relative_path: str) -> Path:
    candidate = (LANE / relative_path).resolve()
    try:
        candidate.relative_to(LANE.resolve())
    except ValueError as exc:
        raise RuntimeError(f"path escapes lane: {relative_path!r}") from exc
    return candidate


def selected_bytes(relative_path: str, selector: str) -> bytes:
    path = lane_path(relative_path)
    data = path.read_bytes()
    if b"\r" in data:
        raise RuntimeError(f"non-LF source for raw-line binding: {path}")
    lines = data.splitlines(keepends=True)
    first, last = selector_bounds(selector)
    if last > len(lines):
        raise RuntimeError(f"selector outside file: {relative_path}:{selector}")
    selected = b"".join(lines[first - 1 : last])
    if not selected:
        raise RuntimeError(f"empty selected content: {relative_path}:{selector}")
    return selected


def hint_selector(relative_path: str, exercise_selector: str, marker: str) -> str:
    path = lane_path(relative_path)
    lines = path.read_text(encoding="utf-8").splitlines()
    first, last = selector_bounds(exercise_selector)
    selected = lines[first - 1 : last]
    # Some frozen exercises introduce the hint after the problem statement on
    # the same physical line (for example, ``... on X.  Hint: Consider ...``).
    # Bind that whole line instead of rejecting a valid inline hint.
    starts = [index for index, line in enumerate(selected) if marker in line]
    if len(starts) != 1:
        raise RuntimeError(
            f"expected one {marker!r} in {relative_path}:{exercise_selector}, found {len(starts)}"
        )
    start_index = starts[0]
    exercise_ends = [
        index
        for index in range(start_index + 1, len(selected))
        if selected[index].lstrip().startswith(r"\end{exercise}")
    ]
    if len(exercise_ends) != 1:
        raise RuntimeError(
            f"expected exactly one subsequent exercise end in {relative_path}:{exercise_selector}, "
            f"found {len(exercise_ends)}"
        )
    end_index = exercise_ends[0] - 1
    while end_index >= start_index and not selected[end_index].strip():
        end_index -= 1
    start_line = first + start_index
    end_line = first + end_index
    return f"raw lines {start_line}-{end_line}"


def adverse_disposition(upstream_status: str) -> str:
    value = upstream_status.casefold()
    if any(
        phrase in value
        for phrase in (
            "exclude from",
            "not an author/source issue",
            "not an upstream",
            "not applicable",
        )
    ):
        return "not_applicable"
    if "issue" in value and any(
        phrase in value for phrase in ("retain", "candidate", "deduplicated", "disposition")
    ):
        return "queued_for_single_issue"
    return "not_evaluated"


def split_ledger_cell(value: str) -> list[str]:
    return list(dict.fromkeys(part.strip() for part in value.split(";") if part.strip()))


def terminology_roles(value: str) -> tuple[str, ...]:
    supplied = split_ledger_cell(value)
    if not supplied or any(role not in NS for role in supplied):
        raise RuntimeError(f"invalid terminology resource_scope: {value!r}")
    return tuple(role for role in NS if role in supplied)


def terminology_namespace(roles: tuple[str, ...]) -> str:
    return NS[roles[0]] if len(roles) == 1 else "shared"


def terminology_register(value: str) -> str:
    normalized = "specialized" if value == "qualified" else value
    if normalized not in TERM_REGISTERS:
        raise RuntimeError(f"unsupported terminology register: {value!r}")
    return normalized


def load_terminology_rows(data: bytes) -> list[dict]:
    reader = csv.DictReader(io.StringIO(data.decode("utf-8-sig"), newline=""))
    if tuple(reader.fieldnames or ()) != TERMINOLOGY_FIELDS:
        raise RuntimeError(f"unexpected terminology columns: {reader.fieldnames}")
    rows = [dict(row) for row in reader]
    term_ids: set[str] = set()
    for row in rows:
        for field in ("term_id", "concept_id", "resource_scope", "source_term", "preferred_id"):
            if not row[field]:
                raise RuntimeError(f"empty {field} in terminology row: {row}")
        if row["term_id"] in term_ids:
            raise RuntimeError(f"duplicate terminology term_id: {row['term_id']}")
        if not row["concept_id"].startswith("concept."):
            raise RuntimeError(f"invalid concept_id: {row['concept_id']}")
        if row["status"] != "admitted":
            raise RuntimeError(f"unsupported terminology status: {row['status']}")
        terminology_roles(row["resource_scope"])
        terminology_register(row["register"])
        term_ids.add(row["term_id"])
    return rows


def registry_for(*schemas: dict) -> Registry:
    registry = Registry()
    for schema in schemas:
        registry = registry.with_resource(schema["$id"], Resource.from_contents(schema))
    return registry


def validate_records(records: list[dict], schema: dict) -> None:
    validator = Draft202012Validator(schema, registry=registry_for(schema), format_checker=FormatChecker())
    errors: list[str] = []
    for index, record in enumerate(records, 1):
        for error in validator.iter_errors(record):
            errors.append(f"record {index} {record.get('semantic_key')}: {error.json_path}: {error.message}")
            if len(errors) >= 30:
                break
        if len(errors) >= 30:
            break
    if errors:
        raise RuntimeError("record schema validation failed:\n" + "\n".join(errors))


def validate_references(records: list[dict]) -> None:
    ids = {record["id"] for record in records}
    expression_ids = {
        expression["expression_id"]
        for record in records
        if record.get("record_type") == "segment"
        for expression in record.get("expressions", [])
    }
    uuid_re = re.compile(r"^urn:uuid:[0-9a-f-]{36}$")

    def walk(value: object, path: str, owner: str) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                if key in {"id", "expression_id", "dataset_id"}:
                    continue
                walk(child, f"{path}.{key}", owner)
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, f"{path}[{index}]", owner)
        elif isinstance(value, str) and uuid_re.fullmatch(value):
            if value not in ids and value not in expression_ids:
                raise RuntimeError(f"unresolved UUID reference at {owner}{path}: {value}")

    for record in records:
        walk(record, "", record["semantic_key"])


def unit_kind(row: dict) -> str:
    # Keep exercise blocks as subsections unless a future unit supplies the
    # richer exercise metadata required by the schema.
    return "subsection" if "/" in row["title_source"] or row["unit_id"].endswith("exercises") else "section"


def source_binding(row: dict, source_edition: dict) -> dict:
    components = row["source_components"]
    return {
        "content_sha256": sha(canon(components)),
        "edition_id": source_edition["id"],
        "locator": "ordered component aggregate from live translation manifest",
        "source_path": components[0]["path"],
    }


def manifest_binding(row: dict) -> dict:
    return {
        "edition_key": row["edition_id"],
        "input_schema": row["schema"],
        "locale": row["locale"],
        "notes": row["notes"],
        "qa": row["qa"],
        "resource_key": row["resource_id"],
        "rights_key": row["rights_id"],
        "source_components": copy.deepcopy(row["source_components"]),
        "state": row["state"],
        "target_components": copy.deepcopy(row["target_components"]),
        "title_target": row["title_target"],
        "translated_at": row["translated_at"],
    }


def build(out: Path = OUT_DEFAULT) -> dict:
    if out.exists():
        raise RuntimeError(f"refusing existing output path: {out}")
    live_manifest, manifest_bytes = load_jsonl(LANE / "translation" / "TRANSLATION_MANIFEST.jsonl")
    manifest_component_checks = 0
    unresolved_legacy_components = 0
    stale_manifest_components: list[str] = []
    for row in live_manifest:
        for side in ("source_components", "target_components"):
            for component in row[side]:
                path = lane_path(component["path"])
                if not path.is_file() or not re.search(r"\braw lines?\s+\d+", component["selector"]):
                    # Early imported manifest rows retain source-relative paths
                    # that require their edition root.  They remain represented,
                    # but only directly resolvable live paths are byte-checked.
                    unresolved_legacy_components += 1
                    continue
                actual = hashlib.sha256(selected_bytes(component["path"], component["selector"])).hexdigest()
                manifest_component_checks += 1
                if actual != component["sha256"]:
                    stale_manifest_components.append(
                        f"{row['unit_id']}:{side}:{component['path']}:{component['selector']} "
                        f"expected {component['sha256']} actual {actual}"
                    )
    if stale_manifest_components:
        raise RuntimeError(
            "stale directly resolvable live-manifest components:\n"
            + "\n".join(stale_manifest_components[:30])
        )
    # Terminology is CSV, not JSONL; retain it byte-for-byte as an input witness.
    terminology_path = LANE / "00_control" / "TERMINOLOGY.csv"
    terminology_bytes = terminology_path.read_bytes()
    terminology_rows = load_terminology_rows(terminology_bytes)
    adverse_path = LANE / "00_control" / "ADVERSE_LEDGER.jsonl"
    adverse_rows, adverse_bytes = load_jsonl(adverse_path)
    adverse_event_ids = [row.get("event_id") for row in adverse_rows]
    if any(not isinstance(event_id, str) or not event_id for event_id in adverse_event_ids):
        raise RuntimeError("adverse ledger row missing event_id")
    if len(adverse_event_ids) != len(set(adverse_event_ids)):
        raise RuntimeError("duplicate adverse-ledger event_id")
    o001_rows, o001_bytes = load_optional_jsonl(O001_PATH)
    o001_gap_ids = [row.get("gap_id") for row in o001_rows]
    if any(not isinstance(gap_id, str) or not gap_id for gap_id in o001_gap_ids):
        raise RuntimeError("O001 ledger row missing gap_id")
    if len(o001_gap_ids) != len(set(o001_gap_ids)):
        raise RuntimeError("duplicate O001 gap_id")
    o001_exercise_ids = [row.get("exercise_id") for row in o001_rows]
    if any(not isinstance(exercise_id, str) or not exercise_id for exercise_id in o001_exercise_ids):
        raise RuntimeError("O001 ledger row missing exercise_id")
    if len(o001_exercise_ids) != len(set(o001_exercise_ids)):
        raise RuntimeError("duplicate O001 exercise_id")
    o001_logical_bindings: list[tuple[str, str, int, int]] = []
    for row in o001_rows:
        resource_id = row.get("resource_id")
        source_path = row.get("source_path")
        source_selector = row.get("source_selector")
        if not all(isinstance(value, str) and value for value in (resource_id, source_path, source_selector)):
            raise RuntimeError("O001 row has incomplete logical source binding")
        first, last = selector_bounds(source_selector)
        normalized_source_path = (
            lane_path(source_path).relative_to(LANE.resolve()).as_posix().casefold()
        )
        o001_logical_bindings.append((resource_id, normalized_source_path, first, last))
    if len(o001_logical_bindings) != len(set(o001_logical_bindings)):
        raise RuntimeError("duplicate O001 logical source binding")

    old_records, _ = load_jsonl(V03 / "records.jsonl")
    records = [copy.deepcopy(record) for record in old_records]
    by_key = {record["semantic_key"]: record for record in records}
    templates = {
        kind: next(record for record in records if record["record_type"] == kind)
        for kind in (
            "unit",
            "segment",
            "qa_event",
            "artifact",
            "asset",
            "concept",
            "term",
            "correction",
            "relation",
        )
    }
    existing_units = {record.get("source_local_id"): record for record in records if record["record_type"] == "unit"}
    resources = {role: by_key[RESOURCE_KEYS[role]] for role in NS}
    sources = {role: by_key[SOURCE_KEYS[role]] for role in NS}
    targets = {role: by_key[TARGET_KEYS[role]] for role in NS}
    rights = {role: by_key[RIGHTS_KEYS[role]] for role in NS}
    live_unit_ids: dict[str, str] = {}
    added_units = 0

    for ordinal, row in enumerate(live_manifest, 1):
        role = row["resource_id"]
        if role not in NS:
            raise RuntimeError(f"unknown resource role in manifest: {role}")
        # Retained v0.3 units keep their stable identities and content, while
        # their live-manifest witness metadata is refreshed deterministically.
        if row["unit_id"] in existing_units:
            retained_unit = existing_units[row["unit_id"]]
            retained_unit["manifest_binding"] = manifest_binding(row)
            live_unit_ids[row["unit_id"]] = retained_unit["id"]
            continue
        ns = NS[role]
        source = sources[role]
        target = targets[role]
        right = rights[role]
        unit_key = f"lebl.{ns}.unit.live-manifest.{slug(row['unit_id'])}"
        if unit_key in by_key:
            raise RuntimeError(f"semantic key collision: {unit_key}")
        unit = copy.deepcopy(templates["unit"])
        unit.update(
            {
                "id": bt.record_uuid("unit", unit_key),
                "semantic_key": unit_key,
                "recorded_at": STAMP,
                "workflow_id": WORKFLOW,
                "resource_id": resources[role]["id"],
                "edition_id": source["id"],
                "rights_id": right["id"],
                "label": row["title_target"],
                "title": row["title_source"],
                "source_local_id": row["unit_id"],
                "order_key": f"{ordinal:04d}",
                "unit_kind": unit_kind(row),
                "concept_ids": [],
                "parent_id": None,
                "prerequisite_ids": [],
                "source_binding": source_binding(row, source),
                "manifest_binding": manifest_binding(row),
                "locale_states": [
                    {"edition_id": source["id"], "locale": "en", "state": "source_frozen"},
                    {"edition_id": target["id"], "locale": "id-ID", "state": "structurally_verified"},
                ],
            }
        )
        records.append(unit)
        by_key[unit_key] = unit
        live_unit_ids[row["unit_id"]] = unit["id"]
        added_units += 1

        segment_key = f"lebl.{ns}.segment.live-title.{slug(row['unit_id'])}"
        source_expression_key = segment_key + ".expression.en-source"
        target_expression_key = segment_key + ".expression.id-id"
        source_expression_id = bt.expression_uuid(source_expression_key)
        target_expression_id = bt.expression_uuid(target_expression_key)
        segment = copy.deepcopy(templates["segment"])
        segment.update(
            {
                "id": bt.record_uuid("segment", segment_key),
                "semantic_key": segment_key,
                "recorded_at": STAMP,
                "workflow_id": WORKFLOW,
                "unit_id": unit["id"],
                "order_key": f"{ordinal:04d}.0001",
                "concept_ids": [],
                "rights_id": right["id"],
                "source_binding": {
                    "content_sha256": sha(row["title_source"].encode("utf-8")),
                    "edition_id": source["id"],
                    "locator": "title_source in live translation manifest",
                    "source_path": row["source_components"][0]["path"],
                },
                "expressions": [
                    {
                        "content": row["title_source"],
                        "content_format": "plaintext",
                        "content_sha256": sha(row["title_source"].encode("utf-8")),
                        "edition_id": source["id"],
                        "expression_id": source_expression_id,
                        "expression_key": source_expression_key,
                        "language": "en",
                        "locale": "en",
                        "provenance": {"method": "source_copy", "note": "Live manifest title.", "responsible_workflow": WORKFLOW},
                        "rights_id": right["id"],
                        "role": "source",
                        "translation_of_expression_id": None,
                        "translation_state": "source_frozen",
                    },
                    {
                        "content": row["title_target"],
                        "content_format": "plaintext",
                        "content_sha256": sha(row["title_target"].encode("utf-8")),
                        "edition_id": target["id"],
                        "expression_id": target_expression_id,
                        "expression_key": target_expression_key,
                        "language": "id",
                        "locale": "id-ID",
                        "provenance": {"method": "machine_assisted", "note": "Live manifest title.", "responsible_workflow": WORKFLOW},
                        "rights_id": right["id"],
                        "role": "translation",
                        "translation_of_expression_id": source_expression_id,
                        "translation_state": "structurally_verified",
                    },
                ],
            }
        )
        records.append(segment)
        by_key[segment_key] = segment

        qa_key = f"lebl.{ns}.qa.live-manifest.{slug(row['unit_id'])}"
        qa = copy.deepcopy(templates["qa_event"])
        qa.update(
            {
                "id": bt.record_uuid("qa_event", qa_key),
                "semantic_key": qa_key,
                "recorded_at": STAMP,
                "workflow_id": WORKFLOW,
                "subject_ids": [unit["id"]],
                "result": "pass",
                "check_type": "topology",
                "note": row["qa"],
                "toolchain": ["bounded unit QA", "OpenAI Codex gpt-5.6-sol, Ultra"],
                "witness": {"kind": "file", "locator": f"translation/TRANSLATION_MANIFEST.jsonl:{row['unit_id']}", "sha256": sha(canon(row))},
            }
        )
        records.append(qa)
        by_key[qa_key] = qa

    if len(live_unit_ids) != len(live_manifest):
        raise RuntimeError("live manifest unit coverage is not count-complete")
    unit_records_by_id = {
        record["id"]: record for record in records if record["record_type"] == "unit"
    }
    for row in live_manifest:
        unit = unit_records_by_id[live_unit_ids[row["unit_id"]]]
        if unit.get("manifest_binding") != manifest_binding(row):
            raise RuntimeError(f"stale live manifest binding: {row['unit_id']}")
    manifest_binding_checks = len(live_manifest)

    # Preserve every retained v0.3 record, then add a count-complete live
    # terminology view.  Changed retained rows receive versioned superseding
    # term records; the historical records remain byte-identical.
    by_id = {record["id"]: record for record in records}
    if len(by_id) != len(records) or len(by_key) != len(records):
        raise RuntimeError("duplicate retained/generated record identity")

    existing_terms: dict[str, dict] = {}
    concept_by_ledger_id: dict[str, dict] = {}
    for record in records:
        if record["record_type"] != "term":
            continue
        ledger_term_id = record["ledger_binding"]["term_id"]
        if ledger_term_id in existing_terms:
            raise RuntimeError(f"duplicate retained ledger term_id: {ledger_term_id}")
        existing_terms[ledger_term_id] = record

        ledger_concept_id = record["ledger_binding"]["concept_id"]
        concept = by_id.get(record["concept_id"])
        if concept is None or concept["record_type"] != "concept":
            raise RuntimeError(f"invalid retained concept reference: {ledger_term_id}")
        prior = concept_by_ledger_id.get(ledger_concept_id)
        if prior is not None and prior["id"] != concept["id"]:
            raise RuntimeError(f"split concept identity: {ledger_concept_id}")
        concept_by_ledger_id[ledger_concept_id] = concept

    shared_right = by_key["lebl.shared.rights.editorial-metadata-unspecified"]
    added_concepts = 0
    added_terms = 0
    superseding_terms = 0

    def append_unique(record: dict) -> None:
        if record["semantic_key"] in by_key:
            raise RuntimeError(f"semantic key collision: {record['semantic_key']}")
        if record["id"] in by_id:
            raise RuntimeError(f"UUID collision: {record['id']}")
        records.append(record)
        by_key[record["semantic_key"]] = record
        by_id[record["id"]] = record

    # Bind the complete direct dependency closure of the accepted R007
    # nonlinear-systems chapter.  The former live backend represented all 20
    # stable text units but omitted their 28 figure files, the one localized
    # overlay, and the two cited bibliography spans.  Derive the bindings from
    # the frozen source and live manifest so that future source drift fails
    # closed instead of silently producing stale asset metadata.
    r007_chapter_path = "source/diffyqs-v6.11/ch-nonlin-systems.tex"
    r007_source_lines = lane_path(r007_chapter_path).read_text(encoding="utf-8").splitlines()
    r007_rows = [
        row
        for row in live_manifest
        if row["resource_id"] == "R007"
        and any(component["path"] == r007_chapter_path for component in row["source_components"])
    ]
    if len(r007_rows) != 20:
        raise RuntimeError(f"expected 20 nonlinear-systems manifest units, found {len(r007_rows)}")

    def r007_unit_at(line_number: int) -> str:
        matches = []
        for row in r007_rows:
            for component in row["source_components"]:
                if component["path"] != r007_chapter_path:
                    continue
                first, last = selector_bounds(component["selector"])
                if first <= line_number <= last:
                    matches.append(row["unit_id"])
        matches = list(dict.fromkeys(matches))
        if len(matches) != 1:
            raise RuntimeError(f"R007 source line {line_number} maps to {len(matches)} units: {matches}")
        return matches[0]

    figure_patterns = (
        ("inputpdft", re.compile(r"\\inputpdft\{([^{}]+)\}")),
        (
            "diffyincludegraphics",
            re.compile(r"\\diffyincludegraphics\{[^{}]*\}\{[^{}]*\}\{([^{}]+)\}"),
        ),
    )
    figure_occurrences: list[tuple[int, str, str, str]] = []
    for line_number, line in enumerate(r007_source_lines, 1):
        for command, pattern in figure_patterns:
            for match in pattern.finditer(line):
                figure_occurrences.append((line_number, command, match.group(1), r007_unit_at(line_number)))
    figure_pairs = {(command, base) for _, command, base, _ in figure_occurrences}
    if len(figure_occurrences) != 26 or len(figure_pairs) != 25:
        raise RuntimeError(
            "R007 nonlinear figure closure mismatch: "
            f"{len(figure_occurrences)} occurrences / {len(figure_pairs)} command-base pairs"
        )
    if sum(command == "inputpdft" for command, _ in figure_pairs) != 3:
        raise RuntimeError("R007 nonlinear inputpdft closure mismatch")
    if sum(command == "diffyincludegraphics" for command, _ in figure_pairs) != 22:
        raise RuntimeError("R007 nonlinear diffyincludegraphics closure mismatch")

    pair_units: dict[tuple[str, str], set[str]] = {}
    for _, command, base, unit_id in figure_occurrences:
        pair_units.setdefault((command, base), set()).add(unit_id)

    source_asset_specs: list[dict] = []
    for command, base in sorted(figure_pairs):
        extensions = (".pdf", ".pdf_t") if command == "inputpdft" else (".pdf",)
        for extension in extensions:
            relative_path = f"source/diffyqs-v6.11/figures/{base}{extension}"
            if not lane_path(relative_path).is_file():
                raise RuntimeError(f"missing R007 nonlinear figure dependency: {relative_path}")
            source_asset_specs.append(
                {
                    "base": base,
                    "extension": extension,
                    "path": relative_path,
                    "unit_ids": sorted(pair_units[(command, base)]),
                }
            )
    if len(source_asset_specs) != 28 or len({spec["path"] for spec in source_asset_specs}) != 28:
        raise RuntimeError("R007 nonlinear figure file closure is not exactly 28 unique files")

    source_asset_ids = {
        spec["path"]: bt.record_uuid(
            "asset",
            "lebl.diffyqs.asset.nonlinear-systems.figure."
            + slug(spec["base"])
            + (".pdf-t.en" if spec["extension"] == ".pdf_t" else ".pdf.en"),
        )
        for spec in source_asset_specs
    }
    added_r007_asset_rows = 0
    added_r007_asset_relation_rows = 0
    r007_relation_order = 0

    def append_r007_relation(subject_id: str, predicate: str, object_id: str, suffix: str) -> None:
        nonlocal added_r007_asset_relation_rows, r007_relation_order
        r007_relation_order += 1
        relation_key = f"lebl.diffyqs.relation.nonlinear-systems.asset.{slug(suffix)}"
        relation = copy.deepcopy(templates["relation"])
        relation.update(
            {
                "id": bt.record_uuid("relation", relation_key),
                "semantic_key": relation_key,
                "recorded_at": STAMP,
                "workflow_id": WORKFLOW,
                "subject_id": subject_id,
                "predicate": predicate,
                "object_id": object_id,
                "order_key": f"0900.{r007_relation_order:04d}",
                "rights_id": rights["R007"]["id"],
            }
        )
        append_unique(relation)
        added_r007_asset_relation_rows += 1

    for spec in source_asset_specs:
        data = lane_path(spec["path"]).read_bytes()
        asset_key = (
            "lebl.diffyqs.asset.nonlinear-systems.figure."
            + slug(spec["base"])
            + (".pdf-t.en" if spec["extension"] == ".pdf_t" else ".pdf.en")
        )
        dependencies = []
        if spec["extension"] == ".pdf_t":
            dependencies = [source_asset_ids[spec["path"].removesuffix("_t")]]
        asset = copy.deepcopy(templates["asset"])
        asset.update(
            {
                "id": source_asset_ids[spec["path"]],
                "semantic_key": asset_key,
                "recorded_at": STAMP,
                "workflow_id": WORKFLOW,
                "resource_id": resources["R007"]["id"],
                "edition_id": sources["R007"]["id"],
                "asset_kind": "figure",
                "path": spec["path"],
                "mime_type": (
                    "application/x-fig-overlay" if spec["extension"] == ".pdf_t" else "application/pdf"
                ),
                "sha256": sha(data),
                "source_binding": {
                    "content_sha256": sha(data),
                    "edition_id": sources["R007"]["id"],
                    "locator": "entire file",
                    "source_path": spec["path"],
                },
                "dependencies": dependencies,
                "rights_id": rights["R007"]["id"],
            }
        )
        append_unique(asset)
        added_r007_asset_rows += 1
        for unit_id in spec["unit_ids"]:
            append_r007_relation(
                live_unit_ids[unit_id],
                "illustrates",
                asset["id"],
                f"{unit_id}-illustrates-{Path(spec['path']).name}-en",
            )

    source_pend_pdf_path = "source/diffyqs-v6.11/figures/nlin-pend.pdf"
    source_pend_overlay_path = "source/diffyqs-v6.11/figures/nlin-pend.pdf_t"
    target_pend_overlay_path = "translation/diffyqs/figures/nlin-pend.pdf_t"
    source_pend_overlay = lane_path(source_pend_overlay_path).read_bytes()
    target_pend_overlay = lane_path(target_pend_overlay_path).read_bytes()
    if source_pend_overlay == target_pend_overlay:
        raise RuntimeError("localized nlin-pend overlay unexpectedly equals its English source")
    target_asset_key = "lebl.diffyqs.asset.nonlinear-systems.figure.nlin-pend.pdf-t.id-id"
    target_asset = copy.deepcopy(templates["asset"])
    target_asset.update(
        {
            "id": bt.record_uuid("asset", target_asset_key),
            "semantic_key": target_asset_key,
            "recorded_at": STAMP,
            "workflow_id": WORKFLOW,
            "resource_id": resources["R007"]["id"],
            "edition_id": targets["R007"]["id"],
            "asset_kind": "figure",
            "path": target_pend_overlay_path,
            "mime_type": "application/x-fig-overlay",
            "sha256": sha(target_pend_overlay),
            "source_binding": {
                "content_sha256": sha(source_pend_overlay),
                "edition_id": sources["R007"]["id"],
                "locator": "entire source overlay; geometry and TeX commands preserved",
                "source_path": source_pend_overlay_path,
            },
            "dependencies": [
                source_asset_ids[source_pend_pdf_path],
                source_asset_ids[source_pend_overlay_path],
            ],
            "rights_id": rights["R007"]["id"],
        }
    )
    append_unique(target_asset)
    added_r007_asset_rows += 1
    pendulum_units = sorted(pair_units[("inputpdft", "nlin-pend")])
    if pendulum_units != ["diffyqs.v6.11.nonlinear-systems.applications.pendulum"]:
        raise RuntimeError(f"unexpected nlin-pend unit binding: {pendulum_units}")
    append_r007_relation(
        target_asset["id"],
        "adapts",
        source_asset_ids[source_pend_overlay_path],
        "nlin-pend-pdf-t-id-id-adapts-en",
    )
    append_r007_relation(
        live_unit_ids[pendulum_units[0]],
        "illustrates",
        target_asset["id"],
        f"{pendulum_units[0]}-illustrates-nlin-pend-pdf-t-id-id",
    )

    bibliography_specs = {
        "BD": ("raw lines 377-386", "Boyce-DiPrima-Meade"),
        "EP": ("raw lines 387-394", "Edwards-Penney"),
    }
    bibliography_path = "source/diffyqs-v6.11/diffyqs.tex"
    bibliography_assets: dict[str, dict] = {}
    for key, (selector, label) in bibliography_specs.items():
        data = selected_bytes(bibliography_path, selector)
        asset_key = f"lebl.diffyqs.asset.bibliography.{slug(key)}.{slug(label)}.en"
        asset = copy.deepcopy(templates["asset"])
        asset.update(
            {
                "id": bt.record_uuid("asset", asset_key),
                "semantic_key": asset_key,
                "recorded_at": STAMP,
                "workflow_id": WORKFLOW,
                "resource_id": resources["R007"]["id"],
                "edition_id": sources["R007"]["id"],
                "asset_kind": "build_dependency",
                "path": bibliography_path,
                "mime_type": "application/x-tex",
                "sha256": sha(data),
                "source_binding": {
                    "content_sha256": sha(data),
                    "edition_id": sources["R007"]["id"],
                    "locator": selector,
                    "source_path": bibliography_path,
                },
                "dependencies": [],
                "rights_id": rights["R007"]["id"],
            }
        )
        append_unique(asset)
        bibliography_assets[key] = asset
        added_r007_asset_rows += 1

    citation_occurrences: list[tuple[int, str, str]] = []
    for line_number, line in enumerate(r007_source_lines, 1):
        for match in re.finditer(r"\\cite\{([^{}]+)\}", line):
            for key in (part.strip() for part in match.group(1).split(",")):
                if key in bibliography_assets:
                    citation_occurrences.append((line_number, key, r007_unit_at(line_number)))
    if len(citation_occurrences) != 10:
        raise RuntimeError(f"expected 10 R007 nonlinear bibliography citations, found {len(citation_occurrences)}")
    for key in bibliography_assets:
        if sum(citation_key == key for _, citation_key, _ in citation_occurrences) != 5:
            raise RuntimeError(f"expected five R007 nonlinear citations for {key}")
    for occurrence, (_, key, unit_id) in enumerate(citation_occurrences, 1):
        append_r007_relation(
            live_unit_ids[unit_id],
            "depends-on",
            bibliography_assets[key]["id"],
            f"{unit_id}-depends-on-{key}-{occurrence:02d}",
        )

    for row in terminology_rows:
        roles = terminology_roles(row["resource_scope"])
        namespace = terminology_namespace(roles)
        right = rights[roles[0]] if len(roles) == 1 else shared_right

        ledger_concept_id = row["concept_id"]
        concept = concept_by_ledger_id.get(ledger_concept_id)
        if concept is None:
            concept_suffix = slug(ledger_concept_id.removeprefix("concept."))
            concept_key = f"lebl.{namespace}.concept.ledger.{concept_suffix}"
            concept = copy.deepcopy(templates["concept"])
            concept.update(
                {
                    "id": bt.record_uuid("concept", concept_key),
                    "semantic_key": concept_key,
                    "semantic_aliases": [],
                    "status": "active",
                    "recorded_at": STAMP,
                    "workflow_id": WORKFLOW,
                    "supersedes_id": None,
                    "label": row["source_term"],
                    "definition": "",
                    "notation": [],
                    "source_bindings": [],
                    "rights_id": right["id"],
                }
            )
            append_unique(concept)
            concept_by_ledger_id[ledger_concept_id] = concept
            added_concepts += 1

        retained = existing_terms.get(row["term_id"])
        if retained is not None and retained["ledger_binding"] == row:
            continue

        term_key = f"lebl.{namespace}.term.ledger.{slug(row['term_id'])}.id-id"
        supersedes_id = None
        if retained is not None:
            revision = hashlib.sha256(canon(row)).hexdigest()[:16]
            term_key += f".revision-{revision}"
            supersedes_id = retained["id"]
            superseding_terms += 1

        term = copy.deepcopy(templates["term"])
        term.update(
            {
                "id": bt.record_uuid("term", term_key),
                "semantic_key": term_key,
                "semantic_aliases": [],
                "status": "active",
                "recorded_at": STAMP,
                "workflow_id": WORKFLOW,
                "supersedes_id": supersedes_id,
                "concept_id": concept["id"],
                "language": "id",
                "locale": "id-ID",
                "preferred": row["preferred_id"],
                "variants": split_ledger_cell(row["variants_id"]),
                "rejected_forms": split_ledger_cell(row["rejected_id"]),
                "scope_ids": [resources[role]["id"] for role in roles],
                "register": terminology_register(row["register"]),
                "evidence": [
                    {
                        "locator": f"inputs/TERMINOLOGY.csv:{row['term_id']}",
                        "sha256": sha(canon(row)),
                    }
                ],
                "examples": [],
                "rights_id": right["id"],
                "ledger_binding": copy.deepcopy(row),
            }
        )
        append_unique(term)
        added_terms += 1

    def normalized_manifest_path(value: str) -> str:
        return value.replace("\\", "/").removeprefix("./").strip("/").casefold()

    def manifest_ids_for_range(role: str, relative_path: str, first: int, last: int) -> list[str]:
        normalized_path = normalized_manifest_path(relative_path)
        matched: set[str] = set()
        for manifest_row in live_manifest:
            if manifest_row["resource_id"] != role:
                continue
            for component in manifest_row["source_components"]:
                if normalized_manifest_path(component["path"]) != normalized_path:
                    continue
                try:
                    component_first, component_last = selector_bounds(component["selector"])
                except RuntimeError:
                    continue
                if component_first <= first and last <= component_last:
                    unit_id = live_unit_ids.get(manifest_row["unit_id"])
                    if unit_id is not None:
                        matched.add(unit_id)
        return sorted(matched)

    def resolve_manifest_component_path(role: str, locator_path: str) -> str | None:
        locator = normalized_manifest_path(locator_path)
        role_paths = {
            normalized_manifest_path(component["path"])
            for manifest_row in live_manifest
            if manifest_row["resource_id"] == role
            for component in manifest_row["source_components"]
        }
        if "/" in locator:
            return locator if locator in role_paths else None
        basename_matches = {path for path in role_paths if Path(path).name == locator}
        return next(iter(basename_matches)) if len(basename_matches) == 1 else None

    def adverse_manifest_resolution(event: dict) -> tuple[list[str], list[dict]]:
        """Resolve only explicit, unambiguous path-and-line authority locators."""
        location = event["authority_location"]
        file_pattern = re.compile(
            r"[A-Za-z0-9_.+/\\-]+\.(?:tex|sty|bib|xml|pdf_t)", re.IGNORECASE
        )
        file_matches = list(file_pattern.finditer(location))
        if not file_matches:
            return [], []
        matched: set[str] = set()
        source_slices: list[dict] = []
        for index, file_match in enumerate(file_matches):
            segment_end = file_matches[index + 1].start() if index + 1 < len(file_matches) else len(location)
            locator_tail = location[file_match.end() : segment_end].split(";", 1)[0]
            line_match = re.match(
                r"\s*(?::|(?:raw\s+)?lines?\b)\s*"
                r"([0-9]+(?:\s*[-–]\s*[0-9]+)?(?:\s*,\s*[0-9]+(?:\s*[-–]\s*[0-9]+)?)*)",
                locator_tail,
                re.IGNORECASE,
            )
            if line_match is None:
                return [], []
            resolved_path = resolve_manifest_component_path(event["resource_id"], file_match.group())
            if resolved_path is None:
                return [], []
            ranges: list[tuple[int, int]] = []
            for range_text in line_match.group(1).split(","):
                range_match = re.fullmatch(r"\s*(\d+)(?:\s*[-–]\s*(\d+))?\s*", range_text)
                if range_match is None:
                    return [], []
                first = int(range_match.group(1))
                last = int(range_match.group(2) or range_match.group(1))
                if first < 1 or last < first:
                    return [], []
                ranges.append((first, last))
            for first, last in ranges:
                range_ids = manifest_ids_for_range(event["resource_id"], resolved_path, first, last)
                if len(range_ids) != 1:
                    return [], []
                matched.update(range_ids)
                source_path = lane_path(resolved_path)
                if source_path.is_file():
                    selector = f"raw lines {first}-{last}"
                    data = selected_bytes(resolved_path, selector)
                    source_slices.append(
                        {
                            "path": resolved_path,
                            "selector": selector,
                            "sha256": sha(data),
                        }
                    )
        return sorted(matched), source_slices

    def correction_delta(event: dict, source_slices: list[dict]) -> tuple[dict, str, list[dict]]:
        after_descriptor = bt.canonical_json(
            {
                "event_id": event["event_id"],
                "kind": "target_action_descriptor",
                "target_action": event["target_action"],
            }
        )
        evidence = [
            {
                "locator": f"inputs/ADVERSE_LEDGER.jsonl:{event['event_id']}",
                "sha256": sha(canon(event)),
            }
        ]
        evidence.extend(
            {
                "locator": f"{item['path']}:{item['selector']}",
                "sha256": item["sha256"],
            }
            for item in source_slices
        )
        if len(source_slices) == 1:
            before_sha256 = source_slices[0]["sha256"]
            before_scope = "exact source slice bytes"
        elif source_slices:
            before_sha256 = sha(canon(source_slices))
            before_scope = "canonical aggregate of exact source-slice witnesses"
        else:
            before_descriptor = {
                "event_id": event["event_id"],
                "finding": event["finding"],
                "kind": "source_finding_descriptor",
            }
            before_sha256 = sha(canon(before_descriptor))
            before_scope = "canonical source-finding descriptor; no source bytes claimed"
        rationale = (
            f"{event['qa_status']} Hash scope: before={before_scope}; "
            "after=canonical target-action descriptor; no target-file bytes are claimed."
        )
        return (
            {
                "before_sha256": before_sha256,
                "after_content": after_descriptor,
                "after_sha256": sha(after_descriptor.encode("utf-8")),
            },
            rationale,
            evidence,
        )

    # Retained v0.3 correction records stay untouched.  Every newer exact
    # adverse-ledger event becomes one deterministic correction record.  A
    # changed event supersedes its retained chain head; an event removed from
    # the live ledger receives a deprecated tombstone that supersedes the stale
    # active head while preserving all historical bytes.
    retained_corrections = [record for record in records if record["record_type"] == "correction"]
    retained_superseded_ids = {
        record["supersedes_id"]
        for record in retained_corrections
        if record["supersedes_id"] is not None
    }
    retained_heads_by_event: dict[str, list[dict]] = {}
    for record in retained_corrections:
        if record["id"] in retained_superseded_ids:
            continue
        retained_heads_by_event.setdefault(record["ledger_binding"]["event_id"], []).append(record)
    if any(len(heads) != 1 for heads in retained_heads_by_event.values()):
        raise RuntimeError("retained correction history has multiple current chain heads")

    added_corrections = 0
    revised_corrections = 0
    removed_corrections = 0
    fallback_corrections = 0
    for event in adverse_rows:
        event_id = event["event_id"]
        retained_head = retained_heads_by_event.get(event_id, [None])[0]
        if retained_head is not None and retained_head["ledger_binding"] == event and retained_head["status"] == "active":
            continue
        role = event["resource_id"]
        if role not in NS:
            raise RuntimeError(f"unknown adverse-ledger resource role: {role}")
        matched_unit_ids, source_slices = adverse_manifest_resolution(event)
        if matched_unit_ids:
            affected_ids = matched_unit_ids
            authority_resolution = {
                "scope": "unit",
                "method": "exact_path_line",
                "matched_unit_ids": matched_unit_ids,
                "note": (
                    f"Every explicit path-and-line locator resolved unambiguously to "
                    f"{len(matched_unit_ids)} live manifest unit(s); no narrative digits were interpreted as lines."
                ),
            }
        else:
            affected_ids = [sources[role]["id"]]
            authority_resolution = {
                "scope": "source_edition",
                "method": "edition_fallback",
                "matched_unit_ids": [],
                "note": "No exact path-and-line live manifest unit resolved; scope retained at the ledger's explicit source edition.",
            }
            fallback_corrections += 1
        correction_key = f"lebl.{NS[role]}.correction.ledger.{slug(event_id)}"
        supersedes_id = None
        if retained_head is not None:
            revision = hashlib.sha256(canon(event)).hexdigest()[:16]
            correction_key += f".revision-{revision}"
            supersedes_id = retained_head["id"]
            revised_corrections += 1
        proposed_delta, rationale, evidence = correction_delta(event, source_slices)
        correction = copy.deepcopy(templates["correction"])
        correction.update(
            {
                "id": bt.record_uuid("correction", correction_key),
                "semantic_key": correction_key,
                "semantic_aliases": [],
                "status": "active",
                "recorded_at": f"{event['date']}T00:00:00Z",
                "workflow_id": WORKFLOW,
                "supersedes_id": supersedes_id,
                "affected_ids": affected_ids,
                "defect_summary": event["finding"],
                "proposed_delta": proposed_delta,
                "rationale": rationale,
                "evidence": evidence,
                "upstream_disposition": adverse_disposition(event["upstream_status"]),
                "rights_id": rights[role]["id"],
                "ledger_binding": copy.deepcopy(event),
                "authority_resolution": authority_resolution,
            }
        )
        append_unique(correction)
        added_corrections += 1

    live_adverse_ids = set(adverse_event_ids)
    live_ledger_sha = hashlib.sha256(adverse_bytes).hexdigest()
    for event_id, heads in retained_heads_by_event.items():
        if event_id in live_adverse_ids:
            continue
        retained_head = heads[0]
        role = retained_head["ledger_binding"]["resource_id"]
        removal_descriptor = bt.canonical_json(
            {
                "event_id": event_id,
                "kind": "removed_from_live_adverse_ledger",
                "live_ledger_sha256": f"sha256:{live_ledger_sha}",
            }
        )
        tombstone_key = (
            f"lebl.{NS[role]}.correction.ledger.{slug(event_id)}.removed-{live_ledger_sha[:16]}"
        )
        tombstone = copy.deepcopy(templates["correction"])
        tombstone.update(
            {
                "id": bt.record_uuid("correction", tombstone_key),
                "semantic_key": tombstone_key,
                "semantic_aliases": [],
                "status": "deprecated",
                "recorded_at": STAMP,
                "workflow_id": WORKFLOW,
                "supersedes_id": retained_head["id"],
                "affected_ids": copy.deepcopy(retained_head["affected_ids"]),
                "defect_summary": (
                    f"Historical adverse event {event_id} is absent from the current live adverse ledger."
                ),
                "proposed_delta": {
                    "before_sha256": sha(canon(retained_head["ledger_binding"])),
                    "after_content": removal_descriptor,
                    "after_sha256": sha(removal_descriptor.encode("utf-8")),
                },
                "rationale": (
                    "The before hash covers the canonical retained ledger binding and the after hash covers "
                    "the canonical removal descriptor; neither hash claims source or target file bytes."
                ),
                "evidence": [
                    {
                        "locator": f"inputs/ADVERSE_LEDGER.jsonl:absence:{event_id}",
                        "sha256": sha(adverse_bytes),
                    }
                ],
                "upstream_disposition": "not_applicable",
                "rights_id": retained_head["rights_id"],
                "ledger_binding": copy.deepcopy(retained_head["ledger_binding"]),
                "authority_resolution": copy.deepcopy(retained_head["authority_resolution"]),
            }
        )
        append_unique(tombstone)
        added_corrections += 1
        removed_corrections += 1

    correction_records = [record for record in records if record["record_type"] == "correction"]
    superseded_correction_ids = {
        record["supersedes_id"]
        for record in correction_records
        if record["supersedes_id"] is not None
    }
    current_active_corrections = [
        record
        for record in correction_records
        if record["id"] not in superseded_correction_ids and record["status"] == "active"
    ]
    current_corrections_by_event: dict[str, dict] = {}
    for record in current_active_corrections:
        event_id = record["ledger_binding"]["event_id"]
        if event_id in current_corrections_by_event:
            raise RuntimeError(f"multiple current correction records for live event: {event_id}")
        current_corrections_by_event[event_id] = record
    if set(current_corrections_by_event) != live_adverse_ids:
        raise RuntimeError("current correction coverage does not exactly equal live adverse ledger")
    for event in adverse_rows:
        if current_corrections_by_event[event["event_id"]]["ledger_binding"] != event:
            raise RuntimeError(f"stale current adverse binding: {event['event_id']}")

    # Materialize the O001 exercise-support ledger without inventing answers
    # or solutions.  The exact ledger row is retained as canonical JSON in the
    # required manifest binding, and the original JSONL bytes are copied below.
    added_o001_exercises = 0
    added_o001_hints = 0
    added_o001_relations = 0
    for ordinal, gap in enumerate(o001_rows, 1):
        if gap.get("schema") != O001_SCHEMA or gap.get("mapping_target") != "O001":
            raise RuntimeError(f"unsupported O001 row: {gap.get('gap_id')}")
        role = gap.get("resource_id")
        if role not in NS:
            raise RuntimeError(f"unknown O001 resource role: {role}")
        if gap.get("status") != "open_solution_gap":
            raise RuntimeError(f"unsupported O001 gap status: {gap.get('status')!r}")
        if not isinstance(gap.get("hint_present"), bool) or not isinstance(gap.get("source_solution_present"), bool):
            raise RuntimeError(f"invalid O001 support flags: {gap.get('gap_id')}")
        if ordinal > 1999:
            raise RuntimeError("too many O001 rows for reserved order-key range")

        source_content = selected_bytes(gap["source_path"], gap["source_selector"])
        target_content = selected_bytes(gap["target_path"], gap["target_selector"])
        source_first, source_last = selector_bounds(gap["source_selector"])
        parent_candidates = manifest_ids_for_range(role, gap["source_path"], source_first, source_last)
        parent_id = parent_candidates[0] if len(parent_candidates) == 1 else None
        state = "structurally_verified_source_corrected" if "LEBL-ID-ADV-" in gap["notes"] else "structurally_verified"
        order_key = f"{8000 + ordinal:04d}"
        target_label = f"Latihan O001 {ordinal:02d}"

        def o001_manifest_binding(
            title_target: str,
            source_path: str,
            source_selector: str,
            source_data: bytes,
            target_path: str,
            target_selector: str,
            target_data: bytes,
        ) -> dict:
            return {
                "input_schema": "lebl-translation-unit-v1",
                "resource_key": role,
                "edition_key": TARGET_KEYS[role],
                "locale": "id-ID",
                "title_target": title_target,
                "state": state,
                "rights_key": MANIFEST_RIGHTS_KEYS[role],
                "source_components": [
                    {
                        "path": source_path,
                        "selector": source_selector,
                        "sha256": hashlib.sha256(source_data).hexdigest(),
                    }
                ],
                "target_components": [
                    {
                        "path": target_path,
                        "selector": target_selector,
                        "sha256": hashlib.sha256(target_data).hexdigest(),
                    }
                ],
                "qa": "Exact O001 source/target slice binding; no answer or solution invented.",
                "translated_at": STAMP[:10],
                "notes": bt.canonical_json(gap),
            }

        exercise_key = f"lebl.{NS[role]}.unit.o001.{slug(gap['exercise_id'])}"
        exercise = copy.deepcopy(templates["unit"])
        exercise.update(
            {
                "id": bt.record_uuid("unit", exercise_key),
                "semantic_key": exercise_key,
                "semantic_aliases": [],
                "status": "active",
                "recorded_at": STAMP,
                "workflow_id": WORKFLOW,
                "supersedes_id": None,
                "resource_id": resources[role]["id"],
                "edition_id": sources[role]["id"],
                "unit_kind": "exercise",
                "source_local_id": gap["exercise_id"],
                "parent_id": parent_id,
                "order_key": order_key,
                "label": target_label,
                "title": gap["notes"],
                "source_binding": {
                    "edition_id": sources[role]["id"],
                    "source_path": gap["source_path"],
                    "locator": gap["source_selector"],
                    "content_sha256": sha(source_content),
                },
                "locale_states": [
                    {"edition_id": sources[role]["id"], "locale": "en", "state": "source_frozen"},
                    {"edition_id": targets[role]["id"], "locale": "id-ID", "state": "structurally_verified"},
                ],
                "concept_ids": [],
                "prerequisite_ids": [],
                "rights_id": rights[role]["id"],
                "manifest_binding": o001_manifest_binding(
                    target_label,
                    gap["source_path"],
                    gap["source_selector"],
                    source_content,
                    gap["target_path"],
                    gap["target_selector"],
                    target_content,
                ),
                "exercise_metadata": {
                    "response_expected": True,
                    "answer_format": "proof",
                    "solution_status": "unknown" if gap["source_solution_present"] else ("hint_only" if gap["hint_present"] else "none"),
                    "source_number": gap["source_label"] or gap["gap_id"],
                },
            }
        )
        append_unique(exercise)
        added_o001_exercises += 1

        if not gap["hint_present"]:
            continue
        declared_source_hint_selector = gap.get("source_hint_selector")
        declared_target_hint_selector = gap.get("target_hint_selector")
        if (declared_source_hint_selector is None) != (declared_target_hint_selector is None):
            raise RuntimeError(
                f"incomplete contextual hint selector pair: {gap.get('gap_id')}"
            )
        if declared_source_hint_selector is None:
            source_hint_selector = hint_selector(
                gap["source_path"], gap["source_selector"], "Hint:"
            )
            target_hint_selector = hint_selector(
                gap["target_path"], gap["target_selector"], "Petunjuk:"
            )
        else:
            if not all(
                isinstance(value, str) and value
                for value in (declared_source_hint_selector, declared_target_hint_selector)
            ):
                raise RuntimeError(
                    f"invalid contextual hint selectors: {gap.get('gap_id')}"
                )
            source_hint_selector = declared_source_hint_selector
            target_hint_selector = declared_target_hint_selector
        source_hint_content = selected_bytes(gap["source_path"], source_hint_selector)
        target_hint_content = selected_bytes(gap["target_path"], target_hint_selector)
        for key, content in (
            ("source_hint_sha256", source_hint_content),
            ("target_hint_sha256", target_hint_content),
        ):
            declared_hash = gap.get(key)
            if declared_hash is not None and declared_hash != hashlib.sha256(content).hexdigest():
                raise RuntimeError(
                    f"contextual hint hash mismatch for {gap.get('gap_id')}:{key}"
                )
        hint_key = f"lebl.{NS[role]}.unit.o001.{slug(gap['exercise_id'])}.hint"
        hint = copy.deepcopy(templates["unit"])
        hint.pop("exercise_metadata", None)
        hint.update(
            {
                "id": bt.record_uuid("unit", hint_key),
                "semantic_key": hint_key,
                "semantic_aliases": [],
                "status": "active",
                "recorded_at": STAMP,
                "workflow_id": WORKFLOW,
                "supersedes_id": None,
                "resource_id": resources[role]["id"],
                "edition_id": sources[role]["id"],
                "unit_kind": "hint",
                "source_local_id": f"{gap['exercise_id']}.hint",
                "parent_id": exercise["id"],
                "order_key": f"{order_key}.0001",
                "label": "Petunjuk",
                "title": f"Hint for {gap['exercise_id']}",
                "source_binding": {
                    "edition_id": sources[role]["id"],
                    "source_path": gap["source_path"],
                    "locator": source_hint_selector,
                    "content_sha256": sha(source_hint_content),
                },
                "locale_states": [
                    {"edition_id": sources[role]["id"], "locale": "en", "state": "source_frozen"},
                    {"edition_id": targets[role]["id"], "locale": "id-ID", "state": "structurally_verified"},
                ],
                "concept_ids": [],
                "prerequisite_ids": [],
                "rights_id": rights[role]["id"],
                "manifest_binding": o001_manifest_binding(
                    "Petunjuk",
                    gap["source_path"],
                    source_hint_selector,
                    source_hint_content,
                    gap["target_path"],
                    target_hint_selector,
                    target_hint_content,
                ),
            }
        )
        append_unique(hint)
        added_o001_hints += 1

        relation_key = f"lebl.{NS[role]}.relation.o001.{slug(gap['gap_id'])}.hints"
        relation = copy.deepcopy(templates["relation"])
        relation.update(
            {
                "id": bt.record_uuid("relation", relation_key),
                "semantic_key": relation_key,
                "semantic_aliases": [],
                "status": "active",
                "recorded_at": STAMP,
                "workflow_id": WORKFLOW,
                "supersedes_id": None,
                "subject_id": hint["id"],
                "predicate": "hints",
                "object_id": exercise["id"],
                "order_key": f"{order_key}.0001",
                "rights_id": rights[role]["id"],
            }
        )
        append_unique(relation)
        added_o001_relations += 1

    for identity_field in ("id", "semantic_key"):
        values = [record[identity_field] for record in records]
        if len(values) != len(set(values)):
            raise RuntimeError(f"duplicate {identity_field}")

    term_records = [record for record in records if record["record_type"] == "term"]
    superseded_term_ids = {
        record["supersedes_id"]
        for record in term_records
        if record["supersedes_id"] is not None
    }
    current_terms = [record for record in term_records if record["id"] not in superseded_term_ids]
    current_by_ledger_id = {
        record["ledger_binding"]["term_id"]: record for record in current_terms
    }
    live_by_ledger_id = {row["term_id"]: row for row in terminology_rows}
    if len(current_by_ledger_id) != len(current_terms):
        raise RuntimeError("duplicate current logical terminology ID")
    if set(current_by_ledger_id) != set(live_by_ledger_id):
        raise RuntimeError("current logical terminology coverage mismatch")
    for term_id, row in live_by_ledger_id.items():
        if current_by_ledger_id[term_id]["ledger_binding"] != row:
            raise RuntimeError(f"stale current terminology row: {term_id}")

    manifest_artifact_key = "lebl.shared.artifact.translation-manifest-live-2026-08-24"
    artifact = copy.deepcopy(templates["artifact"])
    artifact.update(
        {
            "id": bt.record_uuid("artifact", manifest_artifact_key),
            "semantic_key": manifest_artifact_key,
            "recorded_at": STAMP,
            "workflow_id": WORKFLOW,
            "path": "translation/TRANSLATION_MANIFEST.jsonl",
            "bytes": len(manifest_bytes),
            "sha256": sha(manifest_bytes),
            "artifact_kind": "jsonl",
            "produced_from_ids": sorted(live_unit_ids.values()),
            "manifest_ids": [],
            "rights_id": by_key["lebl.shared.rights.editorial-metadata-unspecified"]["id"],
            "toolchain": ["exact live-manifest byte snapshot"],
        }
    )
    records.append(artifact)

    records.sort(key=lambda record: (record["record_type"], record["id"]))
    validate_records(records, load_json(V03 / "schemas" / "record.schema.json"))
    validate_references(records)
    record_bytes = b"".join(canon(record) + b"\n" for record in records)

    projection = copy.deepcopy(load_json(V03 / "projection_manifest.json"))
    term_projections = [
        item for item in projection["projections"] if item["name"] == "terms"
    ]
    if len(term_projections) != 1:
        raise RuntimeError("expected exactly one terms projection")
    term_columns = term_projections[0]["columns"]
    if any(column["name"] == "supersedes_id" for column in term_columns):
        raise RuntimeError("unexpected pre-existing supersedes_id projection")
    record_json_index = next(
        index for index, column in enumerate(term_columns)
        if column["name"] == "record_json"
    )
    term_columns.insert(
        record_json_index,
        {
            "encoding": "scalar",
            "name": "supersedes_id",
            "source": "supersedes_id",
        },
    )
    dataset = copy.deepcopy(load_json(V03 / "dataset.json"))
    projection_bytes = (json.dumps(projection, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    dataset.update(
        {
            "dataset_id": bt.dataset_uuid("lebl.shared.dataset.production-v0.4-live-2026-08-24"),
            "dataset_key": "lebl.shared.dataset.production-v0.4-live-2026-08-24",
            "generated_at": STAMP,
            "workflow_id": WORKFLOW,
            "notice": "Additive mixed-resource live checkpoint for the R006/R007/R008 Lebl family. Retained v0.3 stable identities and non-binding fields are preserved while live manifest bindings are refreshed from the bundled witness; newer manifest units are represented with locale-neutral unit, segment, and QA records. The exact runtime provenance is OpenAI Codex gpt-5.6-sol, Ultra.",
            "projection_manifest": {"path": "projection_manifest.json", "sha256": sha(projection_bytes)},
            "record_streams": [{"path": "records.jsonl", "bytes": len(record_bytes), "record_count": len(records), "sha256": sha(record_bytes)}],
        }
    )
    dataset_bytes = (json.dumps(dataset, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    dataset_schema = load_json(V03 / "schemas" / "dataset.schema.json")
    dataset_validator = Draft202012Validator(dataset_schema, registry=registry_for(dataset_schema, load_json(V03 / "schemas" / "record.schema.json")), format_checker=FormatChecker())
    dataset_errors = list(dataset_validator.iter_errors(dataset))
    if dataset_errors:
        raise RuntimeError("dataset schema validation failed: " + "; ".join(error.message for error in dataset_errors[:10]))

    parent = out.parent
    parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f".{out.name}-", dir=str(parent)) as stage_name:
        stage = Path(stage_name)
        (stage / "inputs").mkdir()
        (stage / "schemas").mkdir()
        (stage / "csv").mkdir()
        (stage / "inputs" / "TRANSLATION_MANIFEST.jsonl").write_bytes(manifest_bytes)
        (stage / "inputs" / "TERMINOLOGY.csv").write_bytes(terminology_bytes)
        (stage / "inputs" / "ADVERSE_LEDGER.jsonl").write_bytes(adverse_bytes)
        if o001_bytes is not None:
            (stage / "inputs" / "O001_SOLUTION_GAP_LEDGER.jsonl").write_bytes(o001_bytes)
        for name in ("record.schema.json", "dataset.schema.json", "projection-manifest.schema.json"):
            shutil.copy2(V03 / "schemas" / name, stage / "schemas" / name)
        (stage / "records.jsonl").write_bytes(record_bytes)
        (stage / "dataset.json").write_bytes(dataset_bytes)
        (stage / "projection_manifest.json").write_bytes(projection_bytes)
        receipts = bt.project_csvs(projection, records, stage / "csv", force=True)
        with (stage / "csv" / "terms.csv").open(encoding="utf-8", newline="") as stream:
            projected_terms = list(csv.DictReader(stream))
        projected_superseded_ids = {
            row["supersedes_id"] for row in projected_terms if row["supersedes_id"]
        }
        projected_current_terms = [
            row for row in projected_terms if row["id"] not in projected_superseded_ids
        ]
        projected_current_ids = {
            row["ledger_term_id"] for row in projected_current_terms
        }
        if len(projected_terms) != len(term_records):
            raise RuntimeError("projected physical terminology count mismatch")
        if len(projected_current_terms) != len(terminology_rows):
            raise RuntimeError("projected current terminology count mismatch")
        if projected_current_ids != set(live_by_ledger_id):
            raise RuntimeError("projected current terminology IDs mismatch")
        roundtrip = bt.roundtrip_csvs(projection, records, stage / "csv")
        if roundtrip.get("roundtrip") != "pass" or roundtrip.get("recovered_records") != len(records):
            raise RuntimeError(f"CSV round-trip failed: {roundtrip}")
        _validated_projection, _validated_records, full_validation = bt.validate_dataset(
            stage, stage / "dataset.json"
        )
        if full_validation.get("record_count") != len(records):
            raise RuntimeError("full backend validator record count mismatch")
        readme = (
            "# Lebl modular backend v0.4 live checkpoint\n\n"
            f"Generated at {STAMP}. Scope: {len(live_manifest)} live translation units "
            f"(R006/R007/R008), with {added_units} units added beyond retained v0.3.\n\n"
            f"Manifest byte checks: {manifest_component_checks} directly resolvable raw-line components pass; "
            f"{unresolved_legacy_components} early source-relative components remain represented but require "
            "their edition-root resolver. "
            f"Live manifest bindings: {manifest_binding_checks} of {len(live_manifest)} exact.\n\n"
            "This is a locale-neutral machine projection; reader-facing TeX remains in the lane's `translation/` directory. "
            "Separate resource, edition, rights, source, target, and provenance identities are preserved.\n\n"
            f"Terminology: {len(term_records)} physical records preserve history; "
            f"{len(current_terms)} current logical terms exactly reproduce the live terminology ledger. "
            "A term is current when its record ID is not named by another term's `supersedes_id`.\n\n"
            f"Corrections: {len(adverse_rows)} current adverse-ledger events are represented, "
            f"with exactly {len(current_active_corrections)} active current records. "
            f"The build adds {added_corrections} correction-history records beyond retained v0.3 "
            f"({revised_corrections} live revisions and {removed_corrections} removal tombstones); "
            f"{fallback_corrections} new records use explicit source-edition fallback scope.\n\n"
            f"O001 solution-gap mapping: {len(o001_rows)} ledger rows, "
            f"{added_o001_exercises} exercise units, {added_o001_hints} hint units, and "
            f"{added_o001_relations} `hints` relations. No answer or solution is invented.\n\n"
            f"R007 nonlinear-systems dependencies: {added_r007_asset_rows} asset records "
            f"(28 frozen figure files, one localized overlay, and two cited bibliography spans) "
            f"with {added_r007_asset_relation_rows} unit/dependency relations derived from "
            f"{len(figure_occurrences)} figure calls and {len(citation_occurrences)} citations.\n\n"
            "Terminology QA evidence: `authority/terminology_evidence/2026-08-22-indonesian-field-usage-qa/TERMINOLOGY_QA_REPORT.md`.\n"
            "Translation/runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`, acting on the user's request.\n"
        ).encode("utf-8")
        (stage / "README.md").write_bytes(readme)
        inventory = []
        for path in sorted(item for item in stage.rglob("*") if item.is_file()):
            data = path.read_bytes()
            inventory.append({"path": path.relative_to(stage).as_posix(), "bytes": len(data), "sha256": sha(data)})
        validation = {
            "schema_validation": "pass",
            "referential_integrity": "pass",
            "live_manifest_rows": len(live_manifest),
            "manifest_binding_checks": manifest_binding_checks,
            "manifest_component_checks": manifest_component_checks,
            "unresolved_legacy_manifest_components": unresolved_legacy_components,
            "added_unit_rows": added_units,
            "record_count": len(records),
            "added_concept_rows": added_concepts,
            "added_term_rows": added_terms,
            "superseding_term_rows": superseding_terms,
            "physical_term_rows": len(term_records),
            "current_logical_term_rows": len(current_terms),
            "adverse_ledger_rows": len(adverse_rows),
            "current_active_correction_rows": len(current_active_corrections),
            "added_correction_rows": added_corrections,
            "revised_correction_rows": revised_corrections,
            "removed_correction_rows": removed_corrections,
            "fallback_correction_rows": fallback_corrections,
            "o001_ledger": {
                "present": o001_bytes is not None,
                "rows": len(o001_rows),
                "bytes": len(o001_bytes) if o001_bytes is not None else 0,
                "sha256": sha(o001_bytes) if o001_bytes is not None else None,
            },
            "added_o001_exercise_rows": added_o001_exercises,
            "added_o001_hint_rows": added_o001_hints,
            "added_o001_relation_rows": added_o001_relations,
            "r007_nonlinear_dependencies": {
                "figure_occurrences": len(figure_occurrences),
                "figure_command_base_pairs": len(figure_pairs),
                "source_figure_files": len(source_asset_specs),
                "localized_overlay_files": 1,
                "bibliography_spans": len(bibliography_assets),
                "citation_occurrences": len(citation_occurrences),
                "added_asset_rows": added_r007_asset_rows,
                "added_relation_rows": added_r007_asset_relation_rows,
            },
            "record_stream": {"bytes": len(record_bytes), "sha256": sha(record_bytes)},
            "manifest": {"bytes": len(manifest_bytes), "sha256": sha(manifest_bytes)},
            "csv_projection": {"receipts": receipts, "roundtrip": roundtrip},
            "inventory": inventory,
            "workflow_id": WORKFLOW,
            "translation_runtime": "OpenAI Codex gpt-5.6-sol, Ultra",
        }
        (stage / "VALIDATION.json").write_bytes((json.dumps(validation, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8"))
        os.replace(stage, out)
    return {
        "output": str(out),
        "live_manifest_rows": len(live_manifest),
        "manifest_binding_checks": manifest_binding_checks,
        "manifest_component_checks": manifest_component_checks,
        "unresolved_legacy_manifest_components": unresolved_legacy_components,
        "added_units": added_units,
        "added_concepts": added_concepts,
        "added_terms": added_terms,
        "superseding_terms": superseding_terms,
        "physical_terms": len(term_records),
        "current_logical_terms": len(current_terms),
        "adverse_ledger_rows": len(adverse_rows),
        "current_active_corrections": len(current_active_corrections),
        "added_corrections": added_corrections,
        "revised_corrections": revised_corrections,
        "removed_corrections": removed_corrections,
        "fallback_corrections": fallback_corrections,
        "o001_ledger_rows": len(o001_rows),
        "added_o001_exercises": added_o001_exercises,
        "added_o001_hints": added_o001_hints,
        "added_o001_relations": added_o001_relations,
        "added_r007_asset_rows": added_r007_asset_rows,
        "added_r007_asset_relations": added_r007_asset_relation_rows,
        "record_count": len(records),
        "record_stream_sha256": sha(record_bytes),
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=str(OUT_DEFAULT))
    args = parser.parse_args()
    print(bt.canonical_json(build(Path(args.out).resolve())))
