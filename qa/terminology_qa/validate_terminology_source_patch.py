#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_name("TERMINOLOGY_SOURCE_PATCH_VALIDATION_20260831.json")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def active(text: str) -> str:
    lines = []
    for line in text.splitlines(keepends=True):
        escaped = False
        kept = []
        for char in line:
            if char == "%" and not escaped:
                break
            kept.append(char)
            escaped = char == "\\" and not escaped
            if char != "\\":
                escaped = False
        lines.append("".join(kept))
    return "".join(lines)


def dollar_math(text: str) -> list[str]:
    values: list[str] = []
    index = 0
    start: int | None = None
    delimiter = ""
    while index < len(text):
        if text[index] == "$" and (index == 0 or text[index - 1] != "\\"):
            token = "$$" if index + 1 < len(text) and text[index + 1] == "$" else "$"
            if start is None:
                delimiter = token
                start = index + len(token)
            elif token == delimiter:
                values.append(text[start:index])
                start = None
                delimiter = ""
            index += len(token)
            continue
        index += 1
    if start is not None:
        raise RuntimeError("unclosed dollar-math delimiter")
    return values


def topology(text: str) -> dict[str, object]:
    body = active(text)
    return {
        "commands": re.findall(r"\\([A-Za-z@]+)", body),
        "environments": re.findall(r"\\(?:begin|end)\{([^}]+)\}", body),
        "labels": re.findall(r"\\label\{([^}]+)\}", body),
        "references": re.findall(r"\\(?:ref|eqref|pageref|chapref|secref|thmref|propref|exampleref|exerciseref)\{([^}]+)\}", body),
        "citations": re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", body),
        "assets": re.findall(r"\\(?:includegraphics|inputpdft|myfig|myfiginpath)\*?(?:\[[^]]*\])?\{([^}]+)\}", body),
        "dollar_math": dollar_math(body),
        "open_braces": body.count("{"),
        "close_braces": body.count("}"),
    }


def check_pair(name: str, old: Path, new: Path) -> dict[str, object]:
    old_text = old.read_text(encoding="utf-8")
    new_text = new.read_text(encoding="utf-8")
    before = topology(old_text)
    after = topology(new_text)
    for key in ("commands", "environments", "labels", "references", "citations", "assets", "dollar_math"):
        if before[key] != after[key]:
            raise RuntimeError(f"{name}: ordered {key} changed")
    if before["open_braces"] != before["close_braces"] or after["open_braces"] != after["close_braces"]:
        raise RuntimeError(f"{name}: unbalanced braces")
    if before["open_braces"] != after["open_braces"]:
        raise RuntimeError(f"{name}: brace topology changed")
    return {
        "old_path": old.relative_to(ROOT).as_posix(),
        "old_bytes": old.stat().st_size,
        "old_sha256": sha(old),
        "new_path": new.relative_to(ROOT).as_posix(),
        "new_bytes": new.stat().st_size,
        "new_sha256": sha(new),
        "commands": len(after["commands"]),
        "environment_boundaries": len(after["environments"]),
        "labels": len(after["labels"]),
        "references": len(after["references"]),
        "citations": len(after["citations"]),
        "assets": len(after["assets"]),
        "math_spans": len(after["dollar_math"]),
        "braces": after["open_braces"],
        "topology": "identical",
    }


def main() -> None:
    r007_new = ROOT / "translation/diffyqs/ch-first-order-ode.tex"
    r007_old = ROOT / "repository/translation/diffyqs/ch-first-order-ode.tex"
    r008_new = ROOT / "translation/complex-analysis/ca.tex"
    r008_old = ROOT / "repository/translation/complex-analysis/ca.tex"
    results = {
        "R007": check_pair("R007", r007_old, r007_new),
        "R008": check_pair("R008", r008_old, r008_new),
    }
    r007 = r007_new.read_text(encoding="utf-8")
    if any(term in r007 for term in ("persamaan terpisahkan", "faktor pengintegrasi")):
        raise RuntimeError("R007 rejected terminology remains")
    if r007.lower().count("separabel") != 8 or r007.lower().count("faktor integrasi") != 8:
        raise RuntimeError("R007 corrected occurrence count differs from 8/8")
    r008 = r008_new.read_text(encoding="utf-8")
    if len(re.findall(r"\bentire\b", r008, flags=re.I)) != 1:
        raise RuntimeError("R008 must retain exactly one defining English entire occurrence")
    if any(term in r008 for term in ("fungsi menyeluruh", "fungsi holomorfik menyeluruh", "fungsi holomorfik seluruh", "fungsi seluruh")):
        raise RuntimeError("R008 superseded entire-function variants remain")
    if r008.count("fungsi penuh") != 37:
        raise RuntimeError("R008 fungsi penuh occurrence count differs from 37")
    glossary = ROOT / "00_control/TERMINOLOGY.csv"
    with glossary.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    ids = [row["term_id"] for row in rows]
    if len(rows) != 804 or len(ids) != len(set(ids)):
        raise RuntimeError("glossary row count or ID uniqueness failed")
    by_id = {row["term_id"]: row for row in rows}
    if by_id["LEBL-TERM-0320"]["preferred_id"] != "faktor integrasi":
        raise RuntimeError("integrating-factor glossary row mismatch")
    if by_id["LEBL-TERM-0803"]["preferred_id"] != "persamaan diferensial separabel":
        raise RuntimeError("separable-equation glossary row mismatch")
    if by_id["LEBL-TERM-0804"]["preferred_id"] != "fungsi penuh":
        raise RuntimeError("entire-function glossary row mismatch")
    receipt = {
        "schema": "lebl-native-id-terminology-source-patch-qa-v1",
        "status": "pass",
        "files": results,
        "glossary": {
            "path": glossary.relative_to(ROOT).as_posix(),
            "rows": len(rows),
            "unique_ids": len(set(ids)),
            "bytes": glossary.stat().st_size,
            "sha256": sha(glossary),
        },
        "checks": {
            "ordered_tex_commands_identical": True,
            "environment_label_reference_citation_asset_topology_identical": True,
            "ordered_math_payloads_identical": True,
            "braces_balanced_and_count_preserved": True,
            "rejected_terminology_absent": True,
            "corrected_occurrence_counts_exact": True,
        },
        "provenance": "OpenAI Codex gpt-5.6-sol, Ultra acting on the user's request",
    }
    OUT.write_text(json.dumps(receipt, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
