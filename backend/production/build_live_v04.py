#!/usr/bin/env python3
"""Build the additive mixed-resource Lebl backend live checkpoint.

This bounded builder extends the retained v0.3 records with every live
manifest unit that was not present in that checkpoint.  It keeps R006, R007,
and R008 as separate resources/editions/rights identities and emits the same
deterministic JSONL/CSV envelope.  It never reads Git or the wider workspace.
"""

from __future__ import annotations

import copy
import hashlib
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
STAMP = "2026-08-23T00:00:00Z"
WORKFLOW = "01a01f57-a34b-7740-9717-596b8116910c/backend-production-v0.4-live"
OUT_DEFAULT = PRODUCTION / "v0.4-live-2026.08.23"

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
    # Terminology is CSV, not JSONL; retain it byte-for-byte as an input witness.
    terminology_path = LANE / "00_control" / "TERMINOLOGY.csv"
    terminology_bytes = terminology_path.read_bytes()
    adverse_path = LANE / "00_control" / "ADVERSE_LEDGER.jsonl"
    adverse_bytes = adverse_path.read_bytes()

    old_records, _ = load_jsonl(V03 / "records.jsonl")
    records = [copy.deepcopy(record) for record in old_records]
    by_key = {record["semantic_key"]: record for record in records}
    templates = {kind: next(record for record in records if record["record_type"] == kind) for kind in ("unit", "segment", "qa_event", "artifact")}
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
        # The retained v0.3 records already cover the first R006 boundary.
        if row["unit_id"] in existing_units:
            live_unit_ids[row["unit_id"]] = existing_units[row["unit_id"]]["id"]
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

    manifest_artifact_key = "lebl.shared.artifact.translation-manifest-live-2026-08-23"
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

    projection = load_json(V03 / "projection_manifest.json")
    dataset = copy.deepcopy(load_json(V03 / "dataset.json"))
    projection_bytes = (json.dumps(projection, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    dataset.update(
        {
            "dataset_id": bt.dataset_uuid("lebl.shared.dataset.production-v0.4-live-2026-08-23"),
            "dataset_key": "lebl.shared.dataset.production-v0.4-live-2026-08-23",
            "generated_at": STAMP,
            "workflow_id": WORKFLOW,
            "notice": "Additive mixed-resource live checkpoint for the R006/R007/R008 Lebl family. Retained v0.3 bytes are preserved; newer manifest units are represented with locale-neutral unit, segment, and QA records. The exact runtime provenance is OpenAI Codex gpt-5.6-sol, Ultra.",
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
        for name in ("record.schema.json", "dataset.schema.json", "projection-manifest.schema.json"):
            shutil.copy2(V03 / "schemas" / name, stage / "schemas" / name)
        (stage / "records.jsonl").write_bytes(record_bytes)
        (stage / "dataset.json").write_bytes(dataset_bytes)
        (stage / "projection_manifest.json").write_bytes(projection_bytes)
        receipts = bt.project_csvs(projection, records, stage / "csv", force=True)
        roundtrip = bt.roundtrip_csvs(projection, records, stage / "csv")
        if roundtrip.get("roundtrip") != "pass" or roundtrip.get("recovered_records") != len(records):
            raise RuntimeError(f"CSV round-trip failed: {roundtrip}")
        readme = (
            "# Lebl modular backend v0.4 live checkpoint\n\n"
            f"Generated at {STAMP}. Scope: {len(live_manifest)} live translation units "
            f"(R006/R007/R008), with {added_units} units added beyond retained v0.3.\n\n"
            "This is a locale-neutral machine projection; reader-facing TeX remains in the lane's `translation/` directory. "
            "Separate resource, edition, rights, source, target, and provenance identities are preserved.\n\n"
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
            "added_unit_rows": added_units,
            "record_count": len(records),
            "record_stream": {"bytes": len(record_bytes), "sha256": sha(record_bytes)},
            "manifest": {"bytes": len(manifest_bytes), "sha256": sha(manifest_bytes)},
            "csv_projection": {"receipts": receipts, "roundtrip": roundtrip},
            "inventory": inventory,
            "workflow_id": WORKFLOW,
            "translation_runtime": "OpenAI Codex gpt-5.6-sol, Ultra",
        }
        (stage / "VALIDATION.json").write_bytes((json.dumps(validation, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8"))
        os.replace(stage, out)
    return {"output": str(out), "live_manifest_rows": len(live_manifest), "added_units": added_units, "record_count": len(records), "record_stream_sha256": sha(record_bytes)}


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=str(OUT_DEFAULT))
    args = parser.parse_args()
    print(bt.canonical_json(build(Path(args.out).resolve())))
