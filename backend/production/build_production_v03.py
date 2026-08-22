#!/usr/bin/env python3
"""Build the deterministic Lebl production-backend v0.3 snapshot.

This generator is intentionally fail-closed until ``FROZEN_EXPECTATIONS`` is
populated after the live R006 controls have been frozen.  It reads the four
named live controls plus the immutable v0.2 record stream as a metadata seed,
and writes only to the explicitly selected output directory.

The v0.3 additions keep every live manifest component, terminology-ledger row,
and adverse-ledger row losslessly attached to schema-validated records.  They
do not mutate source or translation files and they do not replace v0.1/v0.2.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import os
import re
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource


PRODUCTION = Path(__file__).resolve().parent
BACKEND = PRODUCTION.parent
LANE = BACKEND.parent
V02 = PRODUCTION / "v0.2"
V02_RECORDS = V02 / "records.jsonl"

sys.path.insert(0, str(BACKEND / "tools"))
import backend_tool as bt  # noqa: E402


SCHEMA_VERSION = "0.3.0"
STAMP = "2026-08-21T00:00:00Z"
WORKFLOW = "01a01f57-a34b-7740-9717-596b8116910c/backend-production-v0.3-r006-live"
V02_RECORDS_EXPECTED = {
    "bytes": 1_116_969,
    "sha256": "c0e97748bda5d50be56e0799362dd47e08861c68334c9b4a39d1d301871db06c",
    "rows": 526,
}

# Populated only after the parent sends the exact freeze signal.  Leaving any
# value as None makes the builder stop before creating its output directory.
FROZEN_EXPECTATIONS: dict[str, dict[str, Any]] = {
    "manifest": {
        "source": LANE / "translation" / "TRANSLATION_MANIFEST.jsonl",
        "snapshot": "TRANSLATION_MANIFEST.jsonl",
        "bytes": 209_274,
        "sha256": "aa49b93adf9708aeb648b1213eb4632a553769799232318463ad6729d6068041",
        "rows": 167,
    },
    "terminology": {
        "source": LANE / "00_control" / "TERMINOLOGY.csv",
        "snapshot": "TERMINOLOGY.csv",
        "bytes": 55_861,
        "sha256": "edf93094bcf3e19941799183293629aaa09b41ec05d2f30a6cf846271c8e9ddc",
        "rows": 440,
    },
    "adverse": {
        "source": LANE / "00_control" / "ADVERSE_LEDGER.jsonl",
        "snapshot": "ADVERSE_LEDGER.jsonl",
        "bytes": 78_423,
        "sha256": "e6e80131e479a19afd56d702ddd8ce14716d1b507739f3c4ac9082708dba81dc",
        "rows": 94,
    },
    "receipt": {
        "source": LANE / "qa" / "R006_VOLUME1_COMPLETE_CHECKPOINT_20260821.md",
        "snapshot": "R006_VOLUME1_COMPLETE_CHECKPOINT_20260821.md",
        "bytes": 5_789,
        "sha256": "82cba4bdec2dad69ce471550cdf0959c8200b58a9a6836ceed603451745df06a",
        "rows": 1,
    },
}

REQUIRED_MANIFEST_KEYS = {
    "schema",
    "unit_id",
    "resource_id",
    "edition_id",
    "locale",
    "title_source",
    "title_target",
    "state",
    "rights_id",
    "source_components",
    "target_components",
    "qa",
    "translated_at",
    "notes",
}
TERMINOLOGY_HEADERS = [
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
]
REQUIRED_ADVERSE_KEYS = {
    "event_id",
    "date",
    "resource_id",
    "edition_id",
    "kind",
    "severity",
    "authority_location",
    "finding",
    "target_action",
    "content_change",
    "upstream_status",
    "qa_status",
}
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
KEY_FRAGMENT_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
RECEIPT_ARTIFACTS = {
    "realanal-volume1-id.pdf": (
        2_871_094,
        "18aad665c92f5a15e76bedd412f5694e800e8d48c6e150e6d7916dc6bebf4483",
    ),
    "realanal-out.xml": (
        1_654_092,
        "2199e5881abe8082b0ab6b90ea96acc78a18ce99039c92dec4a541d2d64c044b",
    ),
    "realanal.log": (
        111_771,
        "c511ddbfdd5c04cae09dc59603d1a93f4a07b31e569133e88cccb51741973d68",
    ),
    "pdflatex-pass-5.console.log": (
        36_233,
        "fccc105786fb2f92f1c74050cc7cb4cdf7521e3ba464c31a44aa96741a19e351",
    ),
    "converter.console.log": (
        1_464_436,
        "d552780b6e997f031a834eadbfc5183ef38173199f5bf76dd550fea32190d3e3",
    ),
    "alttexts.txt": (
        64_162,
        "8c2f0692aec7daa6435a3d453f992603aa78d8661b187e2eaff4eb7361cb9471",
    ),
    "translation/ra/convert-to-mbx.pl": (
        52_543,
        "3237805eafa1e024e1e0b0637fd0975dcc5d05894e8512dec65f449c297bacfb",
    ),
}


def sha_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha(data: bytes) -> str:
    return "sha256:" + sha_hex(data)


def sha_text(text: str) -> str:
    return sha(text.encode("utf-8"))


def canonical_bytes(value: Any) -> bytes:
    return (bt.canonical_json(value) + "\n").encode("utf-8")


def pretty_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def slug(value: str) -> str:
    cleaned = re.sub(r"[^a-z0-9._-]+", "-", value.casefold()).strip("-.")
    if not cleaned:
        raise RuntimeError(f"cannot create semantic slug from {value!r}")
    return cleaned


def read_jsonl_bytes(data: bytes, label: str) -> tuple[list[dict[str, Any]], list[str]]:
    if not data.endswith(b"\n") or b"\r" in data:
        raise RuntimeError(f"{label}: expected LF-terminated UTF-8 JSONL")
    lines = data.decode("utf-8").splitlines()
    try:
        rows = [json.loads(line) for line in lines]
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"{label}: invalid JSONL: {exc}") from exc
    if not all(isinstance(row, dict) for row in rows):
        raise RuntimeError(f"{label}: every row must be an object")
    return rows, lines


def freeze_gate() -> None:
    missing: list[str] = []
    for name, spec in FROZEN_EXPECTATIONS.items():
        for field in ("bytes", "sha256", "rows"):
            value = spec.get(field)
            if value is None or (field == "sha256" and not SHA_RE.fullmatch(str(value))):
                missing.append(f"{name}.{field}")
    if missing:
        raise RuntimeError(
            "v0.3 freeze gate is unset; pin exact live controls first: " + ", ".join(missing)
        )


def read_frozen_inputs() -> dict[str, Any]:
    freeze_gate()
    raw: dict[str, bytes] = {}
    for name, spec in FROZEN_EXPECTATIONS.items():
        data = Path(spec["source"]).read_bytes()
        if len(data) != spec["bytes"] or sha_hex(data) != spec["sha256"]:
            raise RuntimeError(
                f"{name}: frozen-input mismatch; bytes={len(data)}, sha256={sha_hex(data)}"
            )
        raw[name] = data

    manifest_rows, manifest_lines = read_jsonl_bytes(raw["manifest"], "manifest")
    expected_manifest = int(FROZEN_EXPECTATIONS["manifest"]["rows"])
    if len(manifest_rows) != expected_manifest:
        raise RuntimeError(f"manifest: expected {expected_manifest} rows, found {len(manifest_rows)}")
    unit_ids = [row.get("unit_id") for row in manifest_rows]
    if len(set(unit_ids)) != len(unit_ids) or any(not isinstance(value, str) or not value for value in unit_ids):
        raise RuntimeError("manifest: unit_id values must be nonempty and unique")
    if any(not KEY_FRAGMENT_RE.fullmatch(value) for value in unit_ids):
        raise RuntimeError("manifest: unit_id values must already satisfy the stable semantic-key alphabet")
    if any(not value.startswith("ra.") for value in unit_ids):
        raise RuntimeError("manifest: every R006 unit_id must use the ra. namespace")
    for index, row in enumerate(manifest_rows, 1):
        if set(row) != REQUIRED_MANIFEST_KEYS:
            raise RuntimeError(f"manifest row {index}: unexpected key set")
        if row["schema"] != "lebl-translation-unit-v1" or row["resource_id"] != "R006":
            raise RuntimeError(f"manifest row {index}: unexpected schema/resource")
        if row["locale"] != "id-ID" or not row["state"].startswith("structurally_verified"):
            raise RuntimeError(f"manifest row {index}: unexpected locale/state")
        if not row["title_source"] or not row["title_target"]:
            raise RuntimeError(f"manifest row {index}: source and target titles are required")
        for side in ("source_components", "target_components"):
            components = row[side]
            if not isinstance(components, list) or not components:
                raise RuntimeError(f"manifest row {index}: {side} must be nonempty")
            for component in components:
                if set(component) != {"path", "selector", "sha256"}:
                    raise RuntimeError(f"manifest row {index}: malformed {side} component")
                if not component["path"] or not component["selector"] or not SHA_RE.fullmatch(component["sha256"]):
                    raise RuntimeError(f"manifest row {index}: invalid {side} component value")
        if len(row["source_components"]) != len(row["target_components"]):
            raise RuntimeError(f"manifest row {index}: source/target component count differs")

    terminology_bytes = raw["terminology"]
    if (
        terminology_bytes.startswith(b"\xef\xbb\xbf")
        or not terminology_bytes.endswith(b"\n")
        or b"\r" in terminology_bytes
    ):
        raise RuntimeError("terminology: expected BOM-free UTF-8 with LF endings and a final LF")
    terminology_text = terminology_bytes.decode("utf-8")
    term_reader = csv.DictReader(io.StringIO(terminology_text, newline=""))
    if term_reader.fieldnames != TERMINOLOGY_HEADERS:
        raise RuntimeError(f"terminology: unexpected headers {term_reader.fieldnames!r}")
    term_rows = list(term_reader)
    expected_terms = int(FROZEN_EXPECTATIONS["terminology"]["rows"])
    if len(term_rows) != expected_terms:
        raise RuntimeError(f"terminology: expected {expected_terms} rows, found {len(term_rows)}")
    if any(None in row or set(row) != set(TERMINOLOGY_HEADERS) for row in term_rows):
        raise RuntimeError("terminology: missing or extra CSV fields")
    if any(any(value is None for value in row.values()) for row in term_rows):
        raise RuntimeError("terminology: null CSV values are forbidden")
    expected_term_ids = [f"LEBL-TERM-{index:04d}" for index in range(1, expected_terms + 1)]
    if [row["term_id"] for row in term_rows] != expected_term_ids:
        raise RuntimeError("terminology: term IDs are not the exact contiguous sequence")
    if any(row["resource_scope"] != "R006" or row["status"] != "admitted" for row in term_rows):
        raise RuntimeError("terminology: every frozen row must be admitted in R006 scope")
    if any(not row["concept_id"] or not row["source_term"] or not row["preferred_id"] for row in term_rows):
        raise RuntimeError("terminology: concept, source term, and preferred term are required")
    if any(not KEY_FRAGMENT_RE.fullmatch(row["concept_id"]) for row in term_rows):
        raise RuntimeError("terminology: concept_id must satisfy the stable semantic-key alphabet")
    if any(not row["concept_id"].startswith("concept.") for row in term_rows):
        raise RuntimeError("terminology: every concept_id must use the concept. namespace")
    canonical_csv = io.StringIO(newline="")
    canonical_writer = csv.DictWriter(
        canonical_csv,
        fieldnames=TERMINOLOGY_HEADERS,
        extrasaction="raise",
        lineterminator="\n",
        quoting=csv.QUOTE_MINIMAL,
    )
    canonical_writer.writeheader()
    canonical_writer.writerows(term_rows)
    if canonical_csv.getvalue().encode("utf-8") != terminology_bytes:
        raise RuntimeError("terminology: bytes are not the canonical RFC-4180-style LF projection")

    adverse_rows, adverse_lines = read_jsonl_bytes(raw["adverse"], "adverse ledger")
    expected_adverse = int(FROZEN_EXPECTATIONS["adverse"]["rows"])
    if len(adverse_rows) != expected_adverse:
        raise RuntimeError(f"adverse ledger: expected {expected_adverse} rows, found {len(adverse_rows)}")
    expected_event_ids = [f"LEBL-ID-ADV-{index:04d}" for index in range(1, expected_adverse + 1)]
    if [row.get("event_id") for row in adverse_rows] != expected_event_ids:
        raise RuntimeError("adverse ledger: event IDs are not the exact contiguous sequence")
    for index, row in enumerate(adverse_rows, 1):
        if set(row) != REQUIRED_ADVERSE_KEYS:
            raise RuntimeError(f"adverse row {index}: unexpected key set")
        if row["resource_id"] != "R006" or not isinstance(row["content_change"], bool):
            raise RuntimeError(f"adverse row {index}: unexpected resource/content_change")
        string_fields = REQUIRED_ADVERSE_KEYS - {"content_change"}
        if any(not isinstance(row[field], str) or not row[field].strip() for field in string_fields):
            raise RuntimeError(f"adverse row {index}: every textual field must be nonempty")

    receipt_text = raw["receipt"].decode("utf-8")
    required_receipt_fragments = (
        "The Indonesian translation of R006 Volume I",
        "does **not** claim that R006 is complete",
        "334 Letter pages",
        "32,740 elements",
        "672 unique IDs",
        "952 cross-references",
        "All 142 font rows are embedded",
        "The PDF is not structurally tagged",
        "zero clipping, overlap, broken or missing page",
    )
    missing_fragments = [value for value in required_receipt_fragments if value not in receipt_text]
    if missing_fragments:
        raise RuntimeError(f"receipt: required claims missing: {missing_fragments}")
    artifact_pattern = re.compile(
        r"^\| `([^`]+)` \| ([0-9,]+) \| `([0-9a-f]{64})` \|$", re.MULTILINE
    )
    receipt_artifacts = [
        {"path": match.group(1), "bytes": int(match.group(2).replace(",", "")), "sha256": match.group(3)}
        for match in artifact_pattern.finditer(receipt_text)
    ]
    parsed_artifacts = {
        item["path"]: (item["bytes"], item["sha256"]) for item in receipt_artifacts
    }
    if len(receipt_artifacts) != len(parsed_artifacts):
        raise RuntimeError("receipt: artifact paths must be unique")
    if parsed_artifacts != RECEIPT_ARTIFACTS:
        raise RuntimeError("receipt: exact seven-artifact path/byte/hash inventory does not match")

    return {
        "raw": raw,
        "manifest_rows": manifest_rows,
        "manifest_lines": manifest_lines,
        "term_rows": term_rows,
        "adverse_rows": adverse_rows,
        "adverse_lines": adverse_lines,
        "receipt_text": receipt_text,
        "receipt_artifacts": receipt_artifacts,
    }


def load_seed_records() -> tuple[list[dict[str, Any]], bytes]:
    data = V02_RECORDS.read_bytes()
    expected = V02_RECORDS_EXPECTED
    if len(data) != expected["bytes"] or sha_hex(data) != expected["sha256"]:
        raise RuntimeError("v0.2 record-stream seed does not match its frozen identity")
    rows, lines = read_jsonl_bytes(data, "v0.2 record stream")
    if len(rows) != expected["rows"] or any(bt.canonical_json(row) != line for row, line in zip(rows, lines)):
        raise RuntimeError("v0.2 record-stream seed is not the expected canonical record set")
    return rows, data


def deep_bump(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: deep_bump(item) for key, item in value.items()}
    if isinstance(value, list):
        return [deep_bump(item) for item in value]
    if isinstance(value, str):
        if value == "0.2.0":
            return SCHEMA_VERSION
        return value.replace(":0.2.0", ":" + SCHEMA_VERSION)
    return value


def add_projection_columns(projection: dict[str, Any], columns: list[dict[str, str]]) -> None:
    at = next(index for index, column in enumerate(projection["columns"]) if column["name"] == "record_json")
    projection["columns"][at:at] = columns


def versioned_schemas() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    record_schema = deep_bump(json.loads((V02 / "schemas" / "record.schema.json").read_text(encoding="utf-8")))
    dataset_schema = deep_bump(json.loads((V02 / "schemas" / "dataset.schema.json").read_text(encoding="utf-8")))
    projection_schema = deep_bump(
        json.loads((V02 / "schemas" / "projection-manifest.schema.json").read_text(encoding="utf-8"))
    )
    projection = deep_bump(json.loads((V02 / "projection_manifest.json").read_text(encoding="utf-8")))

    record_schema["$defs"]["manifestComponent"] = {
        "additionalProperties": False,
        "properties": {
            "path": {"minLength": 1, "type": "string"},
            "selector": {"minLength": 1, "type": "string"},
            # The source manifest stores lowercase bare hex, while canonical
            # backend entity hashes use the ``sha256:`` prefix.
            "sha256": {"pattern": "^[0-9a-f]{64}$", "type": "string"},
        },
        "required": ["path", "selector", "sha256"],
        "type": "object",
    }
    record_schema["$defs"]["manifestBinding"] = {
        "additionalProperties": False,
        "properties": {
            "edition_key": {"minLength": 1, "type": "string"},
            "input_schema": {"const": "lebl-translation-unit-v1"},
            "locale": {"$ref": "#/$defs/languageTag"},
            "notes": {"type": "string"},
            "qa": {"minLength": 1, "type": "string"},
            "resource_key": {"minLength": 1, "type": "string"},
            "rights_key": {"minLength": 1, "type": "string"},
            "source_components": {
                "items": {"$ref": "#/$defs/manifestComponent"},
                "minItems": 1,
                "type": "array",
            },
            "state": {"minLength": 1, "type": "string"},
            "target_components": {
                "items": {"$ref": "#/$defs/manifestComponent"},
                "minItems": 1,
                "type": "array",
            },
            "title_target": {"minLength": 1, "type": "string"},
            "translated_at": {"format": "date", "type": "string"},
        },
        "required": [
            "input_schema",
            "resource_key",
            "edition_key",
            "locale",
            "title_target",
            "state",
            "rights_key",
            "source_components",
            "target_components",
            "qa",
            "translated_at",
            "notes",
        ],
        "type": "object",
    }
    record_schema["$defs"]["terminologyLedgerBinding"] = {
        "additionalProperties": False,
        "properties": {name: {"type": "string"} for name in TERMINOLOGY_HEADERS},
        "required": TERMINOLOGY_HEADERS,
        "type": "object",
    }
    adverse_properties = {name: {"minLength": 1, "type": "string"} for name in REQUIRED_ADVERSE_KEYS}
    adverse_properties["content_change"] = {"type": "boolean"}
    adverse_properties["date"] = {"format": "date", "type": "string"}
    record_schema["$defs"]["adverseLedgerBinding"] = {
        "additionalProperties": False,
        "properties": adverse_properties,
        "required": sorted(REQUIRED_ADVERSE_KEYS),
        "type": "object",
    }
    record_schema["$defs"]["authorityResolution"] = {
        "additionalProperties": False,
        "properties": {
            "matched_unit_ids": {"$ref": "#/$defs/idArray"},
            "method": {
                "enum": ["edition_fallback", "exact_path_line", "special_override"],
                "type": "string",
            },
            "note": {"minLength": 1, "type": "string"},
            "scope": {"enum": ["source_edition", "unit"], "type": "string"},
        },
        "required": ["scope", "method", "matched_unit_ids", "note"],
        "type": "object",
    }
    unit_shape = record_schema["$defs"]["unit"]["allOf"][-1]
    unit_shape["properties"]["manifest_binding"] = {"$ref": "#/$defs/manifestBinding"}
    unit_shape["required"].append("manifest_binding")
    term_shape = record_schema["$defs"]["term"]["allOf"][-1]
    term_shape["properties"]["ledger_binding"] = {"$ref": "#/$defs/terminologyLedgerBinding"}
    term_shape["required"].append("ledger_binding")
    correction_shape = record_schema["$defs"]["correction"]["allOf"][-1]
    correction_shape["properties"]["ledger_binding"] = {"$ref": "#/$defs/adverseLedgerBinding"}
    correction_shape["properties"]["authority_resolution"] = {"$ref": "#/$defs/authorityResolution"}
    correction_shape["required"].extend(["ledger_binding", "authority_resolution"])

    metrics = record_schema["$defs"]["qaEvent"]["allOf"][-1]["properties"]["metrics"]
    metrics["properties"]["metric_schema"]["enum"] = [
        "accessibility_pdf_v1",
        "converter_topology_v1",
        "pdf_build_v1",
        "visual_page_set_v1",
    ]
    for name in (
        "cross_references",
        "duplicate_ids",
        "elements",
        "embedded_font_rows",
        "font_rows",
        "overfull_hboxes",
        "overfull_vboxes",
        "render_bytes",
        "rendered_pages",
        "unicode_unmapped_rows",
        "unresolved_cross_references",
    ):
        metrics["properties"][name] = {"minimum": 0, "type": "integer"}

    by_file = {item["file_name"]: item for item in projection["projections"]}
    add_projection_columns(
        by_file["units.csv"],
        [
            {"name": "manifest_state", "source": "manifest_binding.state", "encoding": "scalar"},
            {"name": "manifest_title_target", "source": "manifest_binding.title_target", "encoding": "scalar"},
            {"name": "manifest_translated_at", "source": "manifest_binding.translated_at", "encoding": "scalar"},
            {
                "name": "manifest_source_components_json",
                "source": "manifest_binding.source_components",
                "encoding": "canonical_json",
            },
            {
                "name": "manifest_target_components_json",
                "source": "manifest_binding.target_components",
                "encoding": "canonical_json",
            },
            {"name": "manifest_qa", "source": "manifest_binding.qa", "encoding": "scalar"},
            {"name": "manifest_notes", "source": "manifest_binding.notes", "encoding": "scalar"},
            {
                "name": "manifest_binding_json",
                "source": "manifest_binding",
                "encoding": "canonical_json",
            },
        ],
    )
    add_projection_columns(
        by_file["terms.csv"],
        [
            {"name": "ledger_term_id", "source": "ledger_binding.term_id", "encoding": "scalar"},
            {"name": "source_term", "source": "ledger_binding.source_term", "encoding": "scalar"},
            {"name": "ledger_status", "source": "ledger_binding.status", "encoding": "scalar"},
            {"name": "ledger_binding_json", "source": "ledger_binding", "encoding": "canonical_json"},
        ],
    )
    add_projection_columns(
        by_file["corrections.csv"],
        [
            {"name": "ledger_event_id", "source": "ledger_binding.event_id", "encoding": "scalar"},
            {"name": "event_kind", "source": "ledger_binding.kind", "encoding": "scalar"},
            {"name": "severity", "source": "ledger_binding.severity", "encoding": "scalar"},
            {"name": "content_change", "source": "ledger_binding.content_change", "encoding": "scalar"},
            {
                "name": "authority_location",
                "source": "ledger_binding.authority_location",
                "encoding": "scalar",
            },
            {"name": "qa_status", "source": "ledger_binding.qa_status", "encoding": "scalar"},
            {"name": "upstream_status", "source": "ledger_binding.upstream_status", "encoding": "scalar"},
            {
                "name": "authority_resolution_json",
                "source": "authority_resolution",
                "encoding": "canonical_json",
            },
            {"name": "ledger_binding_json", "source": "ledger_binding", "encoding": "canonical_json"},
        ],
    )
    return record_schema, dataset_schema, projection_schema, projection


def base(record_type: str, semantic_key: str) -> dict[str, Any]:
    return {
        "id": bt.record_uuid(record_type, semantic_key),
        "record_type": record_type,
        "recorded_at": STAMP,
        "schema_name": bt.SCHEMA_NAME,
        "schema_version": SCHEMA_VERSION,
        "semantic_aliases": [],
        "semantic_key": semantic_key,
        "status": "active",
        "supersedes_id": None,
        "workflow_id": WORKFLOW,
    }


def aggregate_component_sha(components: list[dict[str, str]]) -> str:
    return sha(bt.canonical_json(components).encode("utf-8"))


def split_ledger_value(value: str) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in re.split(r"[;|]", value) if item.strip()]


def map_translation_state(value: str) -> str:
    if value.startswith("structurally_verified"):
        return "structurally_verified"
    allowed = {
        "source_frozen",
        "queued",
        "draft",
        "translated",
        "mathematically_reviewed",
        "language_reviewed",
        "built",
        "visually_checked",
        "published",
        "superseded",
        "blocked",
    }
    return value if value in allowed else "draft"


def unit_kind(row: dict[str, Any]) -> str:
    unit_id = row["unit_id"]
    if "notation" in unit_id or "glossary" in unit_id:
        return "notation"
    if "reader" in unit_id:
        return "other"
    if unit_id.endswith(".exercises"):
        return "subsection"
    return "subsection" if "/" in row["title_source"] else "section"


def nearest_parent(unit_id: str, all_units: set[str]) -> str | None:
    candidate = unit_id
    while "." in candidate:
        candidate = candidate.rsplit(".", 1)[0]
        if candidate in all_units:
            return candidate
    return None


SPECIAL_AFFECTED = {
    "LEBL-ID-ADV-0001": "ra.v1.reader.chrome-license",
    "LEBL-ID-ADV-0002": "ra.v1.intro.basic-set-theory.functions",
    "LEBL-ID-ADV-0003": "ra.combined.reader.chrome-license-ptx",
    "LEBL-ID-ADV-0004": "ra.shared.notation-glossary",
    "LEBL-ID-ADV-0005": "ra.shared.notation-glossary",
    "LEBL-ID-ADV-0006": "ra.v1.real-numbers.absolute-value-bounded-functions",
    "LEBL-ID-ADV-0007": "ra.v1.real-numbers.intervals-size-r",
    "LEBL-ID-ADV-0008": "ra.v1.real-numbers.decimal-representation",
    "LEBL-ID-ADV-0009": "ra.v1.sequences-series.sequences-limits.basics",
    "LEBL-ID-ADV-0078": "ra.v1.sequences-series.sequences-limits.tail",
    "LEBL-ID-ADV-0079": "ra.v1.continuous-functions.continuity.discontinuous-functions",
    "LEBL-ID-ADV-0080": "ra.v1.continuous-functions.limits-at-infinity.exercises",
    "LEBL-ID-ADV-0081": "ra.combined.reader.chrome-license-ptx",
}


def selector_range(selector: str) -> tuple[int, int] | None:
    match = re.search(r"lines? (\d+)-(\d+)", selector, re.IGNORECASE)
    return (int(match.group(1)), int(match.group(2))) if match else None


def affected_unit_ids(
    adverse: dict[str, Any], manifest_rows: list[dict[str, Any]], unit_ids: dict[str, str]
) -> tuple[list[str], str]:
    special = SPECIAL_AFFECTED.get(adverse["event_id"])
    if special in unit_ids:
        return [unit_ids[special]], "special_override"
    location = adverse["authority_location"].replace("\\", "/")
    matches: set[str] = set()
    for row in manifest_rows:
        for component in row["source_components"] + row["target_components"]:
            path = component["path"].replace("\\", "/")
            # Require a bounded exact component token and an explicit line.
            # Shared files without a line cannot safely identify one unit.
            location_match = re.search(
                r"(?<![A-Za-z0-9_.-])" + re.escape(path) + r":(\d+)(?!\d)",
                location,
            )
            if location_match is None:
                continue
            line = int(location_match.group(1))
            selected = selector_range(component["selector"])
            if selected is not None and selected[0] <= line <= selected[1]:
                matches.add(row["unit_id"])
    resolved = sorted(unit_ids[value] for value in matches if value in unit_ids)
    if len(resolved) == 1:
        return resolved, "exact_path_line"
    return [], "edition_fallback"


def upstream_disposition(text: str) -> str:
    folded = text.casefold()
    if "exclude" in folded or "not applicable" in folded or "derivative" in folded:
        return "not_applicable"
    if "retain" in folded or "candidate" in folded:
        return "queued_for_single_issue"
    return "not_evaluated"


def qa_check_type(kind: str) -> str:
    folded = kind.casefold()
    if "render" in folded:
        return "visual"
    if "accessibility" in folded:
        return "accessibility"
    if "build" in folded:
        return "build"
    return "source"


def qa_result(status: str) -> str:
    folded = status.casefold()
    if any(token in folded for token in ("fail", "blocked", "unresolved error")):
        return "fail"
    if any(token in folded for token in ("pending", "not run", "not yet", "partial")):
        return "partial"
    explicit_pass = (
        "pass",
        "completed",
        "verified",
        "validated",
        "zero ",
        "clean",
        "preserved",
        "confirmed",
        "converged",
    )
    return "pass" if any(token in folded for token in explicit_pass) else "partial"


def receipt_artifact_path(path: str) -> str:
    if path.startswith("translation/"):
        return path
    return "qa/builds/ra-id-volume1-complete-20260821-final/" + path


def build(out: Path) -> dict[str, Any]:
    publish_out = out
    if publish_out.exists():
        raise RuntimeError(f"refusing existing output path: {publish_out}")
    inputs = read_frozen_inputs()
    seed_rows, seed_bytes = load_seed_records()
    manifest_rows: list[dict[str, Any]] = inputs["manifest_rows"]
    term_rows: list[dict[str, str]] = inputs["term_rows"]
    adverse_rows: list[dict[str, Any]] = inputs["adverse_rows"]

    records = [
        copy.deepcopy(record)
        for record in seed_rows
        if record["record_type"] in {"resource", "edition", "rights", "asset"}
    ]
    for record in records:
        record["schema_version"] = SCHEMA_VERSION
    by_key = {record["semantic_key"]: record for record in records}

    ra_resource = by_key["lebl.ra.resource.primary"]
    ra_source_edition = by_key["lebl.ra.edition.v6-3"]
    old_target_edition = by_key["lebl.ra.edition.id-id-2026-08-20"]
    ra_rights = by_key["lebl.ra.rights.cc-by-sa-4.0"]
    meta_rights = by_key["lebl.shared.rights.editorial-metadata-unspecified"]
    old_target_edition["status"] = "superseded"

    target_key = "lebl.ra.edition.id-id-volume1-complete-2026-08-21"
    target_edition = base("edition", target_key)
    target_edition.update(
        {
            "build_entrypoints": copy.deepcopy(old_target_edition["build_entrypoints"]),
            "derivative_of_id": ra_source_edition["id"],
            "edition_kind": "local_derivative",
            "language": "id",
            "locale": "id-ID",
            "resource_id": ra_resource["id"],
            "revision": {
                "archive_sha256": None,
                "commit_id": None,
                "kind": "local",
                "tree_id": None,
                "value": f"manifest-{len(manifest_rows)}-{sha_hex(inputs['raw']['manifest'])}",
            },
            "rights_id": ra_rights["id"],
            "supersedes_id": old_target_edition["id"],
            # Volume I is complete, but the aggregate R006 two-volume edition
            # remains intentionally draft until all Volume II units are done.
            "translation_state": "draft",
        }
    )
    records.append(target_edition)
    by_key[target_key] = target_edition

    concept_rows: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in term_rows:
        concept_rows[row["concept_id"]].append(row)
    concept_semantic_keys = {
        concept_key: "lebl.ra.concept.ledger." + slug(concept_key.removeprefix("concept."))
        for concept_key in concept_rows
    }
    if len(set(concept_semantic_keys.values())) != len(concept_semantic_keys):
        raise RuntimeError("terminology: concept identifiers collide after semantic-key normalization")
    concept_ids: dict[str, str] = {}
    for concept_key, rows in sorted(concept_rows.items()):
        semantic_key = concept_semantic_keys[concept_key]
        concept = base("concept", semantic_key)
        concept.update(
            {
                "definition": "",
                "label": rows[0]["source_term"],
                "notation": [],
                "rights_id": ra_rights["id"],
                "source_bindings": [],
            }
        )
        records.append(concept)
        concept_ids[concept_key] = concept["id"]

    term_record_ids: dict[str, str] = {}
    allowed_registers = {"standard", "formal", "pedagogical", "historical", "specialized"}
    for row in term_rows:
        semantic_key = "lebl.ra.term.ledger." + row["term_id"].casefold() + ".id-id"
        term = base("term", semantic_key)
        term.update(
            {
                "concept_id": concept_ids[row["concept_id"]],
                "evidence": [
                    {
                        "locator": "backend/production/v0.3/inputs/TERMINOLOGY.csv:" + row["term_id"],
                        "sha256": sha_text(bt.canonical_json(row)),
                    }
                ],
                "examples": [],
                "language": "id",
                "ledger_binding": copy.deepcopy(row),
                "locale": "id-ID",
                "preferred": row["preferred_id"],
                "register": row["register"] if row["register"] in allowed_registers else "specialized",
                "rejected_forms": split_ledger_value(row["rejected_id"]),
                "rights_id": ra_rights["id"],
                "scope_ids": [target_edition["id"]],
                "variants": split_ledger_value(row["variants_id"]),
            }
        )
        records.append(term)
        term_record_ids[row["term_id"]] = term["id"]

    manifest_unit_keys = {
        row["unit_id"]: "lebl.ra.unit.manifest." + slug(row["unit_id"]) for row in manifest_rows
    }
    if len(set(manifest_unit_keys.values())) != len(manifest_unit_keys):
        raise RuntimeError("manifest: unit identifiers collide after semantic-key normalization")
    unit_record_ids = {
        unit_id: bt.record_uuid("unit", semantic_key) for unit_id, semantic_key in manifest_unit_keys.items()
    }
    all_unit_names = set(unit_record_ids)
    title_concepts: dict[str, list[str]] = {}
    for row in manifest_rows:
        folded = row["title_source"].casefold()
        found: set[str] = set()
        for concept_key, rows in concept_rows.items():
            for term_row in rows:
                term_text = term_row["source_term"].casefold().strip()
                if term_text and re.search(r"(?<!\w)" + re.escape(term_text) + r"(?!\w)", folded):
                    found.add(concept_ids[concept_key])
                    break
        title_concepts[row["unit_id"]] = sorted(found)

    segment_record_ids: dict[str, str] = {}
    expression_pairs: dict[str, tuple[str, str]] = {}
    for ordinal, row in enumerate(manifest_rows, 1):
        unit_id = row["unit_id"]
        parent_name = nearest_parent(unit_id, all_unit_names)
        binding = {
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
        unit = base("unit", manifest_unit_keys[unit_id])
        unit.update(
            {
                "concept_ids": title_concepts[unit_id],
                "edition_id": ra_source_edition["id"],
                "label": row["title_target"],
                "locale_states": [
                    {"edition_id": ra_source_edition["id"], "locale": "en", "state": "source_frozen"},
                    {
                        "edition_id": target_edition["id"],
                        "locale": "id-ID",
                        "state": map_translation_state(row["state"]),
                    },
                ],
                "manifest_binding": binding,
                "order_key": f"{ordinal:04d}",
                "parent_id": unit_record_ids[parent_name] if parent_name else None,
                "prerequisite_ids": [],
                "resource_id": ra_resource["id"],
                "rights_id": ra_rights["id"],
                "source_binding": {
                    "content_sha256": aggregate_component_sha(row["source_components"]),
                    "edition_id": ra_source_edition["id"],
                    "locator": "ordered component aggregate from v0.3 translation manifest",
                    "source_path": row["source_components"][0]["path"],
                },
                "source_local_id": unit_id,
                "title": row["title_source"],
                "unit_kind": unit_kind(row),
            }
        )
        records.append(unit)

        segment_key = "lebl.ra.segment.manifest-title." + slug(unit_id)
        source_expression_key = segment_key + ".expression.en-source"
        target_expression_key = segment_key + ".expression.id-id"
        source_expression_id = bt.expression_uuid(source_expression_key)
        target_expression_id = bt.expression_uuid(target_expression_key)
        segment = base("segment", segment_key)
        segment.update(
            {
                "concept_ids": title_concepts[unit_id],
                "expressions": [
                    {
                        "content": row["title_source"],
                        "content_format": "plaintext",
                        "content_sha256": sha_text(row["title_source"]),
                        "edition_id": ra_source_edition["id"],
                        "expression_id": source_expression_id,
                        "expression_key": source_expression_key,
                        "language": "en",
                        "locale": "en",
                        "provenance": {
                            "method": "source_copy",
                            "note": "Exact source title from the frozen live manifest row.",
                            "responsible_workflow": WORKFLOW,
                        },
                        "rights_id": ra_rights["id"],
                        "role": "source",
                        "translation_of_expression_id": None,
                        "translation_state": "source_frozen",
                    },
                    {
                        "content": row["title_target"],
                        "content_format": "plaintext",
                        "content_sha256": sha_text(row["title_target"]),
                        "edition_id": target_edition["id"],
                        "expression_id": target_expression_id,
                        "expression_key": target_expression_key,
                        "language": "id",
                        "locale": "id-ID",
                        "provenance": {
                            "method": "machine_assisted",
                            "note": "Exact Indonesian title from the frozen live manifest row.",
                            "responsible_workflow": WORKFLOW,
                        },
                        "rights_id": ra_rights["id"],
                        "role": "translation",
                        "translation_of_expression_id": source_expression_id,
                        "translation_state": map_translation_state(row["state"]),
                    },
                ],
                "order_key": f"{ordinal:04d}.0001",
                "rights_id": ra_rights["id"],
                "segment_kind": "heading",
                "source_binding": {
                    "content_sha256": sha_text(row["title_source"]),
                    "edition_id": ra_source_edition["id"],
                    "locator": "title_source in frozen v0.3 translation manifest",
                    "source_path": row["source_components"][0]["path"],
                },
                "unit_id": unit["id"],
            }
        )
        records.append(segment)
        segment_record_ids[unit_id] = segment["id"]
        expression_pairs[unit_id] = (target_expression_id, source_expression_id)

    correction_ids: dict[str, str] = {}
    correction_affected: dict[str, list[str]] = {}
    for row in adverse_rows:
        affected, resolution_method = affected_unit_ids(row, manifest_rows, unit_record_ids)
        if not affected:
            # The adverse ledger explicitly binds every event to the frozen
            # upstream edition.  Ambiguous or non-line-specific locators stay
            # at that honest edition scope rather than fabricating unit scope.
            affected = [ra_source_edition["id"]]
            authority_resolution = {
                "matched_unit_ids": [],
                "method": "edition_fallback",
                "note": "No unique exact path-and-line manifest unit resolved; scope retained at the ledger's explicit source edition.",
                "scope": "source_edition",
            }
        else:
            authority_resolution = {
                "matched_unit_ids": affected,
                "method": resolution_method,
                "note": "Authority locator resolved to one explicit manifest unit.",
                "scope": "unit",
            }
        semantic_key = "lebl.ra.correction.ledger." + row["event_id"].casefold()
        correction = base("correction", semantic_key)
        correction.update(
            {
                "affected_ids": affected,
                "authority_resolution": authority_resolution,
                "defect_summary": row["finding"],
                "evidence": [
                    {
                        "locator": "backend/production/v0.3/inputs/ADVERSE_LEDGER.jsonl:" + row["event_id"],
                        "sha256": sha_text(bt.canonical_json(row)),
                    }
                ],
                "ledger_binding": copy.deepcopy(row),
                "proposed_delta": {
                    "after_content": row["target_action"],
                    "after_sha256": sha_text(row["target_action"]),
                    "before_sha256": sha_text(row["finding"]),
                },
                "rationale": row["qa_status"],
                "rights_id": ra_rights["id"],
                "upstream_disposition": upstream_disposition(row["upstream_status"]),
            }
        )
        records.append(correction)
        correction_ids[row["event_id"]] = correction["id"]
        correction_affected[row["event_id"]] = affected

    manifest_artifact_key = "lebl.ra.artifact.translation-manifest-v0.3-r006-live-checkpoint"
    terminology_artifact_key = "lebl.ra.artifact.terminology-v0.3-r006-live-checkpoint"
    adverse_artifact_key = "lebl.ra.artifact.adverse-ledger-v0.3-r006-live-checkpoint"
    receipt_artifact_key = "lebl.ra.artifact.volume1-complete-receipt-2026-08-21"

    def artifact(
        semantic_key: str,
        kind: str,
        path: str,
        data: bytes,
        produced_from_ids: list[str],
        rights_id: str,
        toolchain: list[str],
        manifest_ids: list[str] | None = None,
    ) -> dict[str, Any]:
        record = base("artifact", semantic_key)
        record.update(
            {
                "artifact_kind": kind,
                "bytes": len(data),
                "manifest_ids": manifest_ids or [],
                "path": path,
                "produced_from_ids": produced_from_ids,
                "rights_id": rights_id,
                "sha256": sha(data),
                "toolchain": toolchain,
            }
        )
        records.append(record)
        return record

    manifest_artifact = artifact(
        manifest_artifact_key,
        "jsonl",
        "backend/production/v0.3/inputs/TRANSLATION_MANIFEST.jsonl",
        inputs["raw"]["manifest"],
        [unit_record_ids[row["unit_id"]] for row in manifest_rows],
        meta_rights["id"],
        ["exact frozen live-manifest byte snapshot"],
    )
    terminology_artifact = artifact(
        terminology_artifact_key,
        "csv",
        "backend/production/v0.3/inputs/TERMINOLOGY.csv",
        inputs["raw"]["terminology"],
        list(term_record_ids.values()),
        meta_rights["id"],
        ["exact frozen admitted-terminology byte snapshot"],
    )
    adverse_artifact = artifact(
        adverse_artifact_key,
        "jsonl",
        "backend/production/v0.3/inputs/ADVERSE_LEDGER.jsonl",
        inputs["raw"]["adverse"],
        list(correction_ids.values()),
        meta_rights["id"],
        ["exact frozen adverse-ledger byte snapshot"],
    )
    receipt_artifact = artifact(
        receipt_artifact_key,
        "markdown",
        "backend/production/v0.3/inputs/R006_VOLUME1_COMPLETE_CHECKPOINT_20260821.md",
        inputs["raw"]["receipt"],
        [target_edition["id"]],
        meta_rights["id"],
        ["exact Volume I build, converter, structural, and visual receipt"],
        [manifest_artifact["id"]],
    )

    build_artifacts: dict[str, dict[str, Any]] = {}
    for item in inputs["receipt_artifacts"]:
        path = receipt_artifact_path(item["path"])
        suffix = Path(item["path"]).suffix.casefold()
        kind = "pdf" if suffix == ".pdf" else ("json" if suffix == ".json" else "other")
        semantic_key = "lebl.ra.artifact.volume1-final." + slug(item["path"])
        record = base("artifact", semantic_key)
        record.update(
            {
                "artifact_kind": kind,
                "bytes": item["bytes"],
                "manifest_ids": [manifest_artifact["id"]],
                "path": path,
                "produced_from_ids": [target_edition["id"]],
                "rights_id": ra_rights["id"],
                "sha256": "sha256:" + item["sha256"],
                "toolchain": ["identity imported from the exact Volume I completion receipt"],
            }
        )
        records.append(record)
        build_artifacts[item["path"]] = record

    solution_gap = json.loads((V02 / "solution_gap_summary.json").read_text(encoding="utf-8"))
    solution_gap["schema_version"] = SCHEMA_VERSION
    solution_gap["production_seed_boundary"] = {
        "adverse_events": len(adverse_rows),
        "append_policy": "v0.3 adds exact live-control bindings without modifying retained v0.1/v0.2 bytes.",
        "included_manifest_units": [row["unit_id"] for row in manifest_rows],
        "terminology_rows": len(term_rows),
        "through": "R006 Volume I complete; R006 Volume II admitted through Chapter 1 / The derivative including exercises; R007/R008 remain queued.",
        "volume1_receipt_sha256": sha(inputs["raw"]["receipt"]),
    }
    solution_gap_bytes = pretty_bytes(solution_gap)
    solution_artifact = artifact(
        "lebl.shared.artifact.solution-gap-summary-v0.3-volume1-checkpoint",
        "json",
        "backend/production/v0.3/solution_gap_summary.json",
        solution_gap_bytes,
        [by_key[f"lebl.{name}.resource.primary"]["id"] for name in ("ra", "diffyqs", "ca")],
        meta_rights["id"],
        ["v0.2 solution-gap summary with the exact v0.3 R006 boundary appended"],
    )
    _ = solution_artifact

    artifact(
        "lebl.shared.artifact.v0.2-record-stream-seed-for-v0.3",
        "jsonl",
        "backend/production/v0.2/records.jsonl",
        seed_bytes,
        [],
        meta_rights["id"],
        ["immutable v0.2 metadata seed; only resource, edition, rights, and asset records imported"],
    )
    artifact(
        "lebl.shared.artifact.backend-builder-v0.3",
        "other",
        "backend/production/build_production_v03.py",
        Path(__file__).read_bytes(),
        [],
        meta_rights["id"],
        ["deterministic Python 3 builder"],
    )

    def add_qa(
        semantic_key: str,
        check_type: str,
        subject_ids: list[str],
        result: str,
        witness: dict[str, Any],
        toolchain: list[str],
        note: str,
        metrics: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        record = base("qa_event", semantic_key)
        record.update(
            {
                "check_type": check_type,
                "note": note,
                "result": result,
                "subject_ids": subject_ids,
                "toolchain": toolchain,
                "witness": witness,
            }
        )
        if metrics is not None:
            record["metrics"] = metrics
        records.append(record)
        return record

    input_artifacts = {
        "manifest": manifest_artifact,
        "terminology": terminology_artifact,
        "adverse": adverse_artifact,
        "receipt": receipt_artifact,
    }
    input_subjects = {
        "manifest": [unit_record_ids[row["unit_id"]] for row in manifest_rows],
        "terminology": list(term_record_ids.values()),
        "adverse": list(correction_ids.values()),
        "receipt": [target_edition["id"]],
    }
    for name, record in input_artifacts.items():
        add_qa(
            "lebl.ra.qa.v0.3-input-integrity." + name,
            "source",
            input_subjects[name],
            "pass",
            {"kind": "file", "locator": record["path"], "sha256": record["sha256"]},
            ["exact byte count, SHA-256 binding, deterministic parse, and invariant validation"],
            f"Frozen {name} input passed its exact v0.3 identity and structural gate.",
        )

    manifest_line_by_id = {
        row["unit_id"]: line for row, line in zip(manifest_rows, inputs["manifest_lines"])
    }
    for row in manifest_rows:
        add_qa(
            "lebl.ra.qa.manifest-topology." + slug(row["unit_id"]),
            "topology",
            [unit_record_ids[row["unit_id"]]],
            "pass",
            {
                "kind": "file",
                "locator": "backend/production/v0.3/inputs/TRANSLATION_MANIFEST.jsonl:" + row["unit_id"],
                "sha256": sha_text(manifest_line_by_id[row["unit_id"]]),
            },
            [row["qa"]],
            row["notes"],
        )

    adverse_line_by_id = {
        row["event_id"]: line for row, line in zip(adverse_rows, inputs["adverse_lines"])
    }
    for row in adverse_rows:
        add_qa(
            "lebl.ra.qa.adverse-ledger." + row["event_id"].casefold(),
            qa_check_type(row["kind"]),
            correction_affected[row["event_id"]],
            qa_result(row["qa_status"]),
            {
                "kind": "file",
                "locator": "backend/production/v0.3/inputs/ADVERSE_LEDGER.jsonl:" + row["event_id"],
                "sha256": sha_text(adverse_line_by_id[row["event_id"]]),
            },
            ["adverse-ledger admission and recorded QA replay"],
            row["qa_status"],
        )

    receipt_witness = {
        "kind": "file",
        "locator": receipt_artifact["path"],
        "sha256": receipt_artifact["sha256"],
    }
    add_qa(
        "lebl.ra.qa.volume1-complete.converter-2026-08-21",
        "topology",
        [build_artifacts["realanal-out.xml"]["id"]],
        "pass",
        receipt_witness,
        ["exact Volume I completion receipt"],
        "Well-formed id-ID PreTeXt: zero converter errors, duplicate IDs, or unresolved cross-references.",
        {
            "cross_references": 952,
            "duplicate_ids": 0,
            "elements": 32740,
            "errors": 0,
            "metric_schema": "converter_topology_v1",
            "resolving_xrefs": 952,
            "unique_ids": 672,
            "unresolved_cross_references": 0,
        },
    )
    add_qa(
        "lebl.ra.qa.volume1-complete.pdf-build-2026-08-21",
        "build",
        [build_artifacts["realanal-volume1-id.pdf"]["id"]],
        "pass",
        receipt_witness,
        ["five pdflatex passes; four makeindex/makeglossaries rounds"],
        "The 334-page Volume I PDF passed the exact structural and converged-log gate.",
        {
            "errors": 0,
            "fatal_errors": 0,
            "metric_schema": "pdf_build_v1",
            "pages": 334,
            "rerun_markers": 0,
            "undefined_references": 0,
        },
    )
    add_qa(
        "lebl.ra.qa.volume1-complete.visual-2026-08-21",
        "visual",
        [build_artifacts["realanal-volume1-id.pdf"]["id"]],
        "pass",
        receipt_witness,
        ["all-page 72-dpi render review plus direct high-resolution checks of changed pages"],
        "All 334 pages passed with zero clipping, overlap, broken/missing page, figure, glyph, or running-element defect.",
        {
            "metric_schema": "visual_page_set_v1",
            "render_bytes": 39525828,
            "rendered_pages": 334,
        },
    )
    add_qa(
        "lebl.ra.qa.volume1-complete.accessibility-2026-08-21",
        "accessibility",
        [
            build_artifacts["realanal-volume1-id.pdf"]["id"],
            build_artifacts["realanal-out.xml"]["id"],
        ],
        "partial",
        receipt_witness,
        ["PDF metadata/font inspection and PreTeXt accessibility-boundary review"],
        "All 142 PDF font rows are embedded, but the PDF is untagged and 95 rows lack Unicode maps; accessible HTML remains a later full-edition gate.",
        {
            "embedded_font_rows": 142,
            "font_rows": 142,
            "metric_schema": "accessibility_pdf_v1",
            "unicode_unmapped_rows": 95,
        },
    )

    relation_counter = 0
    relation_keys: set[str] = set()

    def add_relation(token: str, subject_id: str, predicate: str, object_id: str) -> None:
        nonlocal relation_counter
        relation_counter += 1
        semantic_key = "lebl.ra.relation.v0.3." + slug(token)
        if semantic_key in relation_keys:
            raise RuntimeError(f"relation semantic-key collision: {semantic_key}")
        relation_keys.add(semantic_key)
        record = base("relation", semantic_key)
        record.update(
            {
                "object_id": object_id,
                "order_key": f"{relation_counter:04d}",
                "predicate": predicate,
                "rights_id": meta_rights["id"],
                "subject_id": subject_id,
            }
        )
        records.append(record)

    for row in manifest_rows:
        unit_id = row["unit_id"]
        add_relation(
            "unit-contains-title-" + unit_id,
            unit_record_ids[unit_id],
            "contains",
            segment_record_ids[unit_id],
        )
        target_expression_id, source_expression_id = expression_pairs[unit_id]
        add_relation(
            "title-translates-" + unit_id,
            target_expression_id,
            "translates",
            source_expression_id,
        )
    for left, right in zip(manifest_rows, manifest_rows[1:]):
        add_relation(
            "precedes-" + left["unit_id"] + "-to-" + right["unit_id"],
            unit_record_ids[left["unit_id"]],
            "precedes",
            unit_record_ids[right["unit_id"]],
        )
    for event_id, affected in correction_affected.items():
        for ordinal, object_id in enumerate(affected, 1):
            add_relation(
                f"correction-{event_id}-{ordinal}",
                correction_ids[event_id],
                "corrects",
                object_id,
            )

    records.sort(key=lambda record: (record["record_type"], record["id"]))
    if len({record["id"] for record in records}) != len(records):
        raise RuntimeError("duplicate record ID")
    if len({record["semantic_key"] for record in records}) != len(records):
        raise RuntimeError("duplicate semantic key")

    record_schema, dataset_schema, projection_schema, projection = versioned_schemas()
    schema_registry = Registry().with_resource(record_schema["$id"], Resource.from_contents(record_schema))
    schema_errors: list[str] = []
    format_checker = FormatChecker()
    for index, record in enumerate(records, 1):
        for error in Draft202012Validator(
            record_schema,
            registry=schema_registry,
            format_checker=format_checker,
        ).iter_errors(record):
            schema_errors.append(f"record[{index}] {error.json_path}: {error.message}")
    if schema_errors:
        raise RuntimeError("v0.3 record schema validation failed:\n" + "\n".join(schema_errors[:30]))

    for record in (item for item in records if item["record_type"] == "correction"):
        resolution = record["authority_resolution"]
        matched = resolution["matched_unit_ids"]
        if resolution["scope"] == "unit":
            if not matched or matched != record["affected_ids"]:
                raise RuntimeError(f"{record['semantic_key']}: unit-scope authority resolution mismatch")
        elif matched or record["affected_ids"] != [ra_source_edition["id"]]:
            raise RuntimeError(f"{record['semantic_key']}: edition-fallback authority resolution mismatch")

    normalized = copy.deepcopy(records)
    for record in normalized:
        record["schema_version"] = bt.SCHEMA_VERSION
        if record["record_type"] == "qa_event":
            record.pop("metrics", None)
        if record["record_type"] == "unit":
            record.pop("manifest_binding", None)
        if record["record_type"] in {"term", "correction"}:
            record.pop("ledger_binding", None)
        if record["record_type"] == "correction":
            record.pop("authority_resolution", None)
    old_record_schema = json.loads((BACKEND / "schemas" / "record.schema.json").read_text(encoding="utf-8"))
    reference_summary = bt.validate_records(normalized, old_record_schema)

    manifest_roundtrip: list[dict[str, Any]] = []
    for record in sorted(
        (item for item in records if item["record_type"] == "unit" and "manifest_binding" in item),
        key=lambda item: item["order_key"],
    ):
        binding = record["manifest_binding"]
        manifest_roundtrip.append(
            {
                "schema": binding["input_schema"],
                "unit_id": record["source_local_id"],
                "resource_id": binding["resource_key"],
                "edition_id": binding["edition_key"],
                "locale": binding["locale"],
                "title_source": record["title"],
                "title_target": binding["title_target"],
                "state": binding["state"],
                "rights_id": binding["rights_key"],
                "source_components": binding["source_components"],
                "target_components": binding["target_components"],
                "qa": binding["qa"],
                "translated_at": binding["translated_at"],
                "notes": binding["notes"],
            }
        )
    term_roundtrip = [
        record["ledger_binding"]
        for record in sorted(
            (item for item in records if item["record_type"] == "term"),
            key=lambda item: item["ledger_binding"]["term_id"],
        )
    ]
    adverse_roundtrip = [
        record["ledger_binding"]
        for record in sorted(
            (item for item in records if item["record_type"] == "correction"),
            key=lambda item: item["ledger_binding"]["event_id"],
        )
    ]
    if manifest_roundtrip != manifest_rows or term_roundtrip != term_rows or adverse_roundtrip != adverse_rows:
        raise RuntimeError("lossless live-control record round-trip failed")

    record_stream = b"".join(canonical_bytes(record) for record in records)
    projection_bytes = pretty_bytes(projection)
    dataset_key = "lebl.shared.dataset.production-v0.3-r006-live-checkpoint-2026-08-21"
    resource_ids = sorted(record["id"] for record in records if record["record_type"] == "resource")
    edition_ids = sorted(record["id"] for record in records if record["record_type"] == "edition")
    dataset = {
        "authority_status": "authoritative",
        "canonicalization": {"csv": "ILCSV-0.1", "json": "ILJCS-0.1"},
        "dataset_id": bt.dataset_uuid(dataset_key),
        "dataset_key": dataset_key,
        "edition_ids": edition_ids,
        "fixture": False,
        "generated_at": STAMP,
        "lane_id": bt.LANE_ID,
        "namespace_uuid": str(bt.NAMESPACE_UUID),
        "notice": (
            "Additive v0.3 checkpoint bound to the exact live R006 manifest, admitted terminology, "
            "adverse ledger, and Volume I completion receipt; the aggregate two-volume R006 edition "
            "remains draft while Volume II is incomplete; v0.1/v0.2 remain unchanged historical snapshots."
        ),
        "projection_manifest": {"path": "projection_manifest.json", "sha256": sha(projection_bytes)},
        "record_streams": [
            {
                "bytes": len(record_stream),
                "path": "records.jsonl",
                "record_count": len(records),
                "sha256": sha(record_stream),
            }
        ],
        "resource_ids": resource_ids,
        "schema_name": "lebl.backend.dataset",
        "schema_version": SCHEMA_VERSION,
        "workflow_id": WORKFLOW,
    }
    dataset_bytes = pretty_bytes(dataset)
    for name, schema, value in (
        ("dataset", dataset_schema, dataset),
        ("projection", projection_schema, projection),
    ):
        for error in Draft202012Validator(
            schema,
            registry=schema_registry,
            format_checker=format_checker,
        ).iter_errors(value):
            schema_errors.append(f"{name} {error.json_path}: {error.message}")
    if schema_errors:
        raise RuntimeError("v0.3 schema validation failed:\n" + "\n".join(schema_errors[:30]))

    # All semantic validation above completes before bytes are emitted.  Stage
    # the complete tree beside the destination and publish it with one rename,
    # so a late projection or I/O failure never leaves a poisoned v0.3 path.
    publish_out.parent.mkdir(parents=True, exist_ok=True)
    stage_context = tempfile.TemporaryDirectory(
        prefix=f".{publish_out.name}.staging-",
        dir=str(publish_out.parent),
    )
    out = Path(stage_context.name)
    out_inputs = out / "inputs"
    out_inputs.mkdir(parents=True, exist_ok=True)
    for name, spec in FROZEN_EXPECTATIONS.items():
        (out_inputs / spec["snapshot"]).write_bytes(inputs["raw"][name])
    schema_dir = out / "schemas"
    schema_dir.mkdir(parents=True, exist_ok=True)
    (schema_dir / "record.schema.json").write_bytes(pretty_bytes(record_schema))
    (schema_dir / "dataset.schema.json").write_bytes(pretty_bytes(dataset_schema))
    (schema_dir / "projection-manifest.schema.json").write_bytes(pretty_bytes(projection_schema))
    (out / "projection_manifest.json").write_bytes(projection_bytes)
    (out / "records.jsonl").write_bytes(record_stream)
    (out / "dataset.json").write_bytes(dataset_bytes)
    (out / "solution_gap_summary.json").write_bytes(solution_gap_bytes)

    csv_dir = out / "csv"
    csv_receipts = bt.project_csvs(projection, records, csv_dir, force=True)
    roundtrip = bt.roundtrip_csvs(projection, records, csv_dir)
    if len(csv_receipts) != 15 or roundtrip != {
        "checked_files": 15,
        "recovered_records": len(records),
        "roundtrip": "pass",
    }:
        raise RuntimeError("CSV projection/round-trip invariant failed")

    inventory_entries: list[dict[str, Any]] = []
    for path in sorted(
        (item for item in out.rglob("*") if item.is_file() and item.name != "VALIDATION.json"),
        key=lambda item: item.relative_to(out).as_posix(),
    ):
        data = path.read_bytes()
        inventory_entries.append(
            {
                "bytes": len(data),
                "path": path.relative_to(out).as_posix(),
                "sha256": sha(data),
            }
        )
    inventory_text = "\n".join(
        f"{item['path']}\t{item['bytes']}\t{item['sha256']}" for item in inventory_entries
    ).encode("utf-8")
    type_counts = dict(sorted(Counter(record["record_type"] for record in records).items()))
    authority_resolution_counts = dict(
        sorted(
            Counter(
                record["authority_resolution"]["method"]
                for record in records
                if record["record_type"] == "correction"
            ).items()
        )
    )
    validation = {
        "authority_resolution_counts": authority_resolution_counts,
        "control_roundtrip": {
            "adverse_rows": len(adverse_roundtrip),
            "manifest_rows": len(manifest_roundtrip),
            "result": "pass",
            "terminology_rows": len(term_roundtrip),
        },
        "edition_state": {
            "edition_id": target_edition["id"],
            "reason": "Volume I is complete, but the aggregate R006 two-volume edition remains incomplete in Volume II.",
            "state": "draft",
        },
        "csv_projection": {"count": len(csv_receipts), "receipts": csv_receipts},
        "dataset_sha256": sha(dataset_bytes),
        "frozen_inputs": {
            name: {
                "bytes": len(inputs["raw"][name]),
                "path": "inputs/" + spec["snapshot"],
                "sha256": sha(inputs["raw"][name]),
            }
            for name, spec in sorted(FROZEN_EXPECTATIONS.items())
        },
        "generated_at": STAMP,
        "inventory": {"entry_count": len(inventory_entries), "sha256": sha(inventory_text)},
        "lane_id": bt.LANE_ID,
        "record_count": len(records),
        "record_stream_bytes": len(record_stream),
        "record_stream_sha256": sha(record_stream),
        "record_type_counts": type_counts,
        "referential_integrity": reference_summary,
        "roundtrip": roundtrip,
        "schema_documents": 3,
        "schema_name": "lebl.backend.validation",
        "schema_validation": "pass",
        "schema_version": SCHEMA_VERSION,
        "seed": {
            "imported_record_types": ["asset", "edition", "resource", "rights"],
            "record_stream_bytes": len(seed_bytes),
            "record_stream_sha256": sha(seed_bytes),
        },
        "typed_qa_metrics": {
            "accessibility": {"embedded_font_rows": 142, "font_rows": 142, "unicode_unmapped_rows": 95},
            "converter": {
                "cross_references": 952,
                "duplicate_ids": 0,
                "elements": 32740,
                "errors": 0,
                "unique_ids": 672,
                "unresolved_cross_references": 0,
            },
            "pdf_checkpoint": {
                "errors": 0,
                "fatal_errors": 0,
                "pages": 334,
                "rerun_markers": 0,
                "undefined_references": 0,
            },
            "visual": {"render_bytes": 39525828, "rendered_pages": 334},
        },
        "workflow_id": WORKFLOW,
    }
    validation_bytes = pretty_bytes(validation)
    (out / "VALIDATION.json").write_bytes(validation_bytes)
    os.replace(out, publish_out)
    stage_context.cleanup()
    return {
        "dataset_sha256": sha(dataset_bytes),
        "output": str(publish_out),
        "record_count": len(records),
        "record_stream_bytes": len(record_stream),
        "record_stream_sha256": sha(record_stream),
        "record_type_counts": type_counts,
        "validation_sha256": sha(validation_bytes),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=str(PRODUCTION / "v0.3"))
    args = parser.parse_args()
    result = build(Path(args.out).resolve())
    print(bt.canonical_json(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
