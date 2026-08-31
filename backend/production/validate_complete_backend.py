#!/usr/bin/env python3
"""Validate the complete backend and its lossless CSV round trip.

The complete manifest-artifact record legitimately projects to a CSV field
larger than Python's default 128 KiB parser limit.  This bounded wrapper raises
that limit, delegates to the normative backend tool, and verifies that the
validated and round-tripped record counts are identical.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


LANE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(LANE / "backend" / "tools"))
import backend_tool as bt  # noqa: E402

csv.field_size_limit(64 * 1024 * 1024)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--csv-dir")
    arguments = parser.parse_args()
    dataset_path = Path(arguments.dataset).resolve()
    dataset_root = dataset_path.parent
    projection, records, validation = bt.validate_dataset(dataset_root, dataset_path)
    csv_dir = Path(arguments.csv_dir).resolve() if arguments.csv_dir else dataset_root / "csv"
    roundtrip = bt.roundtrip_csvs(projection, records, csv_dir)
    if roundtrip.get("roundtrip") != "pass":
        raise RuntimeError(f"CSV round trip failed: {roundtrip}")
    if roundtrip.get("recovered_records") != validation.get("record_count"):
        raise RuntimeError("validated and recovered record counts differ")
    result = {
        "dataset": str(dataset_path),
        "schema_validation": "pass",
        "referential_integrity": "pass",
        "record_count": validation["record_count"],
        "entity_counts": validation["entity_counts"],
        "csv_roundtrip": roundtrip,
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
