#!/usr/bin/env python3
"""Finalize the Lebl-family translation manifest with complete TeX coverage.

The historical manifest contains fine-grained translation units accumulated
through production.  This bounded utility preserves those stable units,
refreshes every directly resolvable raw-line hash against the current files,
and appends one deterministic coverage unit for every canonical reader TeX
file in R006, R007, and R008.  Intermediate sprint packets, slides, fragments
that are not used by the final readers, and generated build files are excluded
by an explicit allowlist rather than by a recursive discovery heuristic.

The tool never edits reader-facing TeX.  It writes only the manifest path
passed with ``--out`` (the live manifest by default).
"""

from __future__ import annotations

import argparse
import bisect
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path


LANE = Path(__file__).resolve().parents[2]
MANIFEST = LANE / "translation" / "TRANSLATION_MANIFEST.jsonl"
SCHEMA = "lebl-translation-unit-v1"
TRANSLATED_AT = "2026-08-30"
COVERAGE_KIND = "canonical_tex_file"
INDEX_KIND = "logical_tex_unit"
NONFINAL_STATES = {
    "structurally_verified_checkpoint_build",
    "structurally_verified_build_pending",
}

# These are already recorded source corrections in ADVERSE_LEDGER.jsonl.  They
# have no upstream peer event, so they remain represented by correction records
# plus complete-file coverage rather than being falsely paired as translations.
DECLARED_TARGET_ONLY_EVENTS = {
    ("R006", "ch-one-dim-ints-sv.tex", "hint", "hint", 1930),
    ("R006", "ch-approximate.tex", "environment", "remark", 4654),
}

RESOURCE_METADATA = {
    "R006": {
        "namespace": "ra.v6.3",
        "edition_id": "lebl.ra.edition.id-id-volume1-complete-2026-08-21",
        "rights_id": "rights.ra.book.cc-by-sa-4.0",
        "source_root": "source/ra-v6.3",
        "target_root": "translation/ra",
        "files": (
            "ch-approximate.tex",
            "ch-contfunc.tex",
            "ch-der.tex",
            "ch-metric.tex",
            "ch-multivar-int.tex",
            "ch-one-dim-ints-sv.tex",
            "ch-real-nums.tex",
            "ch-riemann.tex",
            "ch-seq-funcs.tex",
            "ch-seq-ser.tex",
            "ch-several-vars-ders.tex",
            "ch-vol1-intro.tex",
            "frag-vol2-intro.tex",
            "notations.tex",
            "realanal.tex",
            "realanal12.tex",
            "realanal2.tex",
        ),
    },
    "R007": {
        "namespace": "diffyqs.v6.11",
        "edition_id": "lebl.diffyqs.edition.id-id-2026-08-20",
        "rights_id": "rights.diffyqs.book.cc-by-sa-4.0",
        "source_root": "source/diffyqs-v6.11",
        "target_root": "translation/diffyqs",
        "files": (
            "ap-laplace-list.tex",
            "ap-linear-algebra.tex",
            "ch-eigenvalue-probs.tex",
            "ch-first-order-ode.tex",
            "ch-fourier-and-pde.tex",
            "ch-higher-order-ode.tex",
            "ch-intro.tex",
            "ch-laplace.tex",
            "ch-nonlin-systems.tex",
            "ch-power-ser.tex",
            "ch-systems.tex",
            "diffyqs.tex",
        ),
    },
    "R008": {
        "namespace": "ca.v1.9",
        "edition_id": "lebl.ca.edition.id-id-2026-08-20",
        "rights_id": "rights.ca.book.cc-by-sa-4.0",
        "source_root": "source/ca-v1.9",
        "target_root": "translation/complex-analysis",
        "files": ("ca.tex", "notations.tex"),
    },
}

# This file is deliberately introduced by the Indonesian derivative and has no
# one-to-one upstream file.  The upstream reader driver is the provenance
# anchor; the manifest notes the asymmetric relationship explicitly.
DERIVATIVE_SUPPORT = (
    {
        "resource_id": "R007",
        "unit_id": "diffyqs.v6.11.canonical-file.id-localization-tex",
        "title_source": "Diffy Qs reader driver (upstream provenance anchor)",
        "title_target": "Lapisan lokalisasi id-ID Diffy Qs",
        "source_path": "source/diffyqs-v6.11/diffyqs.tex",
        "target_path": "translation/diffyqs/id-localization.tex",
    },
)

CONTENT_FILES = {
    "R006": (
        "ch-vol1-intro.tex",
        "ch-real-nums.tex",
        "ch-seq-ser.tex",
        "ch-contfunc.tex",
        "ch-der.tex",
        "ch-riemann.tex",
        "ch-seq-funcs.tex",
        "ch-metric.tex",
        "frag-vol2-intro.tex",
        "ch-several-vars-ders.tex",
        "ch-one-dim-ints-sv.tex",
        "ch-multivar-int.tex",
        "ch-approximate.tex",
    ),
    "R007": (
        "ch-intro.tex",
        "ch-first-order-ode.tex",
        "ch-higher-order-ode.tex",
        "ch-systems.tex",
        "ch-fourier-and-pde.tex",
        "ch-eigenvalue-probs.tex",
        "ch-laplace.tex",
        "ch-power-ser.tex",
        "ch-nonlin-systems.tex",
        "ap-linear-algebra.tex",
        "ap-laplace-list.tex",
    ),
    "R008": ("ca.tex",),
}

HEADING_LEVELS = {"chapter": 1, "section": 2, "subsection": 3, "subsubsection": 4}
SEMANTIC_ENVIRONMENTS = {
    "defn": "definition",
    "definition": "definition",
    "thm": "theorem",
    "theorem": "theorem",
    "lemma": "lemma",
    "prop": "proposition",
    "proposition": "proposition",
    "cor": "corollary",
    "corollary": "corollary",
    "proof": "proof",
    "example": "example",
    "exercise": "exercise",
    "remark": "remark",
    "exnote": "hint",
    "myfigureht": "figure",
    "myfig": "figure",
    "mywrapfig": "figure",
    "mywrapfigsimp": "figure",
    "figure": "figure",
    "floatingfigure": "figure",
    "table": "table",
    "longtable": "table",
}
INDONESIAN_KIND = {
    "chapter": "Bab",
    "section": "Bagian",
    "subsection": "Subbagian",
    "definition": "Definisi",
    "theorem": "Teorema",
    "lemma": "Lema",
    "proposition": "Proposisi",
    "corollary": "Korolari",
    "proof": "Bukti",
    "example": "Contoh",
    "exercise": "Latihan",
    "hint": "Petunjuk",
    "solution": "Solusi",
    "figure": "Gambar",
    "table": "Tabel",
    "remark": "Catatan",
    "other": "Unit",
}


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def lane_path(relative: str) -> Path:
    path = (LANE / relative).resolve()
    path.relative_to(LANE.resolve())
    return path


def file_lines(path: Path) -> list[bytes]:
    data = path.read_bytes()
    lines = data.splitlines(keepends=True)
    if not lines:
        raise RuntimeError(f"empty canonical TeX file: {path}")
    return lines


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def raw_bounds(selector: str) -> tuple[int, int] | None:
    match = re.search(r"\braw lines?\s+(\d+)(?:\s*[-–]\s*(\d+))?", selector)
    if match is None:
        return None
    first = int(match.group(1))
    last = int(match.group(2) or match.group(1))
    if first < 1 or last < first:
        raise RuntimeError(f"invalid raw-line selector: {selector!r}")
    return first, last


def selected_bytes(path: Path, selector: str) -> bytes:
    bounds = raw_bounds(selector)
    if bounds is None:
        raise RuntimeError(f"selector is not raw-line resolvable: {selector!r}")
    first, last = bounds
    lines = file_lines(path)
    if last > len(lines):
        raise RuntimeError(f"selector exceeds current file: {path}:{selector}")
    return b"".join(lines[first - 1 : last])


def coverage_component(relative: str) -> dict[str, str]:
    path = lane_path(relative)
    lines = file_lines(path)
    selector = f"raw lines 1-{len(lines)} inclusive; complete canonical TeX file"
    return {"path": relative, "selector": selector, "sha256": digest(b"".join(lines))}


def slug(filename: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", filename.casefold()).strip("-")


def escaped(text: str, position: int) -> bool:
    backslashes = 0
    position -= 1
    while position >= 0 and text[position] == "\\":
        backslashes += 1
        position -= 1
    return backslashes % 2 == 1


def mask_comments(text: str) -> str:
    """Replace active TeX comments with spaces while preserving offsets."""
    output: list[str] = []
    for line in text.splitlines(keepends=True):
        chars = list(line)
        for index, char in enumerate(chars):
            if char == "%" and not escaped(line, index):
                for masked in range(index, len(chars)):
                    if chars[masked] not in "\r\n":
                        chars[masked] = " "
                break
        output.extend(chars)
    return "".join(output)


def group_end(masked: str, opening: int) -> int:
    if opening >= len(masked) or masked[opening] != "{":
        raise RuntimeError("group parser did not start at an opening brace")
    depth = 0
    for position in range(opening, len(masked)):
        char = masked[position]
        if escaped(masked, position):
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return position
            if depth < 0:
                break
    raise RuntimeError(f"unclosed TeX group at byte/character offset {opening}")


def line_starts(text: str) -> list[int]:
    return [0] + [match.end() for match in re.finditer("\n", text)]


def line_number(starts: list[int], position: int) -> int:
    return bisect.bisect_right(starts, position)


def clean_title(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip() or "Untitled"


def extract_structural_events(path: Path, locale: str) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    masked = mask_comments(text)
    starts = line_starts(text)
    events: list[dict] = []

    heading_pattern = re.compile(
        r"\\(chapter|section|subsection|subsubsection)\*?"
        r"(?:\[[^\]\n]*\])?\s*(\{)"
    )
    for match in heading_pattern.finditer(masked):
        closing = group_end(masked, match.start(2))
        tail = masked[closing + 1 : closing + 501]
        label_match = re.match(r"\s*\\label\{([^{}]+)\}", tail)
        events.append(
            {
                "event_type": "heading",
                "event_subtype": match.group(1),
                "unit_kind": "subsection" if match.group(1) == "subsubsection" else match.group(1),
                "heading_level": HEADING_LEVELS[match.group(1)],
                "title": clean_title(text[match.start(2) + 1 : closing]),
                "labels": [label_match.group(1)] if label_match else [],
                "start_offset": match.start(),
                "end_offset": closing,
                "first_line": line_number(starts, match.start()),
                "last_line": line_number(starts, closing),
            }
        )

    token_pattern = re.compile(r"\\(begin|end)\{([^{}]+)\}")
    stack: list[tuple[str, int, int]] = []
    semantic_events: list[dict] = []
    for match in token_pattern.finditer(masked):
        action, environment = match.group(1), match.group(2)
        if action == "begin":
            stack.append((environment, match.start(), match.end()))
            continue
        if not stack or stack[-1][0] != environment:
            owner = stack[-1][0] if stack else "<empty>"
            raise RuntimeError(
                f"misnested environment in {path}: end {environment!r} with stack top {owner!r}"
            )
        opened_environment, opened, _opened_end = stack.pop()
        content = masked[opened : match.end()]
        if opened_environment in SEMANTIC_ENVIRONMENTS:
            semantic_kind = SEMANTIC_ENVIRONMENTS[opened_environment]
        elif opened_environment == "center" and r"\inputpdft{1-1-fig}" in content:
            # The final Indonesian reader deliberately reflows the source's
            # wrapping Figure 2 into a centered block.  It remains the same
            # typed logical figure and is still hash-bound on both sides.
            semantic_kind = "figure"
        else:
            continue
        labels = re.findall(r"\\label\{([^{}]+)\}", content)
        semantic_events.append(
            {
                "event_type": "environment",
                "event_subtype": opened_environment,
                "unit_kind": semantic_kind,
                "heading_level": None,
                "title": "",
                "labels": labels,
                "start_offset": opened,
                "end_offset": match.end() - 1,
                "first_line": line_number(starts, opened),
                "last_line": line_number(starts, match.end() - 1),
            }
        )
    if stack:
        raise RuntimeError(f"unclosed environment in {path}: {stack[-1][0]!r}")
    semantic_events.sort(key=lambda event: (event["start_offset"], -event["end_offset"]))

    exercise_ordinal = 0
    for event in semantic_events:
        if event["unit_kind"] != "exercise":
            continue
        exercise_ordinal += 1
        event["exercise_ordinal"] = exercise_ordinal
        marker = (
            r"\b(?:Another\s+hint|Hints?)\s*:"
            if locale == "en"
            else r"\b(?:Petunjuk(?:\s+lain)?)\s*:"
        )
        exercise_text = masked[event["start_offset"] : event["end_offset"] + 1]
        for hint_ordinal, hint in enumerate(re.finditer(marker, exercise_text), 1):
            hint_start = event["start_offset"] + hint.start()
            events.append(
                {
                    "event_type": "hint",
                    "event_subtype": "inline-hint",
                    "unit_kind": "hint",
                    "heading_level": None,
                    "title": "",
                    "labels": [],
                    "exercise_ordinal": exercise_ordinal,
                    "hint_ordinal": hint_ordinal,
                    "start_offset": hint_start,
                    "end_offset": event["end_offset"],
                    "first_line": line_number(starts, hint_start),
                    "last_line": event["last_line"],
                }
            )
    events.extend(semantic_events)

    solution_ordinal = 0
    for match in re.finditer(r"\\exsol\s*(\{)", masked):
        closing = group_end(masked, match.start(1))
        solution_ordinal += 1
        preceding = [
            event
            for event in semantic_events
            if event["unit_kind"] == "exercise" and event["end_offset"] < match.start()
        ]
        parent_exercise = preceding[-1].get("exercise_ordinal") if preceding else None
        events.append(
            {
                "event_type": "solution",
                "event_subtype": "exsol",
                "unit_kind": "solution",
                "heading_level": None,
                "title": "",
                "labels": [],
                "solution_ordinal": solution_ordinal,
                "parent_exercise_ordinal": parent_exercise,
                "start_offset": match.start(),
                "end_offset": closing,
                "first_line": line_number(starts, match.start()),
                "last_line": line_number(starts, closing),
            }
        )

    events.sort(
        key=lambda event: (
            event["start_offset"],
            {"heading": 0, "environment": 1, "hint": 2, "solution": 3}[event["event_type"]],
            -event["end_offset"],
        )
    )
    return events


def component_for_range(relative: str, first: int, last: int) -> dict[str, str]:
    path = lane_path(relative)
    lines = file_lines(path)
    if first < 1 or last < first or last > len(lines):
        raise RuntimeError(f"logical-unit range outside file: {relative}:{first}-{last}")
    data = b"".join(lines[first - 1 : last])
    return {
        "path": relative,
        "selector": f"raw lines {first}-{last} inclusive; deterministic logical TeX unit",
        "sha256": digest(data),
    }


def logical_rows() -> list[dict]:
    rows: list[dict] = []
    resource_ordinal = {role: 0 for role in RESOURCE_METADATA}
    for role in ("R006", "R007", "R008"):
        metadata = RESOURCE_METADATA[role]
        for filename in CONTENT_FILES[role]:
            source_path = f"{metadata['source_root']}/{filename}"
            target_path = f"{metadata['target_root']}/{filename}"
            source_events = extract_structural_events(lane_path(source_path), "en")
            target_events = extract_structural_events(lane_path(target_path), "id-ID")
            target_events = [
                event
                for event in target_events
                if (
                    role,
                    filename,
                    event["event_type"],
                    event["unit_kind"],
                    event["first_line"],
                )
                not in DECLARED_TARGET_ONLY_EVENTS
            ]
            def signature(event: dict) -> tuple[str, str, str]:
                # Figure-wrapper changes (for example mywrapfig -> centered
                # myfig) are an intentional reader-layout adaptation.  Match
                # semantic environment kind while retaining exact source and
                # target wrapper names in the file-bound hashes.
                subtype = (
                    event["unit_kind"]
                    if event["event_type"] == "environment"
                    else event["event_subtype"]
                )
                return event["event_type"], subtype, event["unit_kind"]

            source_signatures = [signature(event) for event in source_events]
            target_signatures = [signature(event) for event in target_events]
            if source_signatures != target_signatures:
                mismatch = next(
                    (
                        index
                        for index, pair in enumerate(zip(source_signatures, target_signatures), 1)
                        if pair[0] != pair[1]
                    ),
                    min(len(source_signatures), len(target_signatures)) + 1,
                )
                raise RuntimeError(
                    f"source/target logical event mismatch in {filename} at event {mismatch}; "
                    f"source={len(source_events)} target={len(target_events)}"
                )

            aligned: list[tuple[dict, dict, dict]] = []
            for source_event, target_event in zip(source_events, target_events):
                if source_event["labels"] != target_event["labels"]:
                    raise RuntimeError(
                        f"source/target label mismatch in {filename}: "
                        f"{source_event['labels']} != {target_event['labels']}"
                    )
                resource_ordinal[role] += 1
                unit_id = f"{metadata['namespace']}.logical.u{resource_ordinal[role]:06d}"
                aligned.append((source_event, target_event, {"unit_id": unit_id}))

            heading_stack: dict[int, str] = {}
            active: list[tuple[int, str, str]] = []
            exercise_ids: dict[int, str] = {}
            for source_event, target_event, identity in aligned:
                start = source_event["start_offset"]
                active = [item for item in active if item[0] >= start]
                parent_unit_id: str | None = None
                if source_event["event_type"] == "heading":
                    level = source_event["heading_level"]
                    parent_levels = [candidate for candidate in heading_stack if candidate < level]
                    if parent_levels:
                        parent_unit_id = heading_stack[max(parent_levels)]
                    heading_stack = {
                        candidate: unit_id
                        for candidate, unit_id in heading_stack.items()
                        if candidate < level
                    }
                    heading_stack[level] = identity["unit_id"]
                elif source_event["event_type"] == "solution":
                    parent_unit_id = exercise_ids.get(source_event.get("parent_exercise_ordinal"))
                    if parent_unit_id is None and heading_stack:
                        parent_unit_id = heading_stack[max(heading_stack)]
                elif source_event["event_type"] == "hint":
                    parent_unit_id = exercise_ids.get(source_event.get("exercise_ordinal"))
                else:
                    enclosing = [item for item in active if item[0] >= source_event["end_offset"]]
                    if enclosing:
                        parent_unit_id = min(enclosing, key=lambda item: item[0])[1]
                    elif heading_stack:
                        parent_unit_id = heading_stack[max(heading_stack)]

                if source_event["unit_kind"] == "exercise":
                    exercise_ids[source_event["exercise_ordinal"]] = identity["unit_id"]

                label = source_event["labels"][0] if source_event["labels"] else ""
                source_kind = source_event["unit_kind"].replace("_", " ").title()
                target_kind = INDONESIAN_KIND.get(source_event["unit_kind"], "Unit")
                if source_event["event_type"] == "heading":
                    title_source = source_event["title"]
                    title_target = target_event["title"]
                else:
                    suffix = f": {label}" if label else f" {identity['unit_id'].rsplit('.', 1)[-1]}"
                    title_source = source_kind + suffix
                    title_target = target_kind + suffix
                row = {
                    "schema": SCHEMA,
                    "unit_id": identity["unit_id"],
                    "resource_id": role,
                    "edition_id": metadata["edition_id"],
                    "locale": "id-ID",
                    "title_source": title_source,
                    "title_target": title_target,
                    "state": "structurally_verified",
                    "rights_id": metadata["rights_id"],
                    "index_kind": INDEX_KIND,
                    "unit_kind": source_event["unit_kind"],
                    "parent_unit_id": parent_unit_id,
                    "source_labels": source_event["labels"],
                    "source_components": [
                        component_for_range(
                            source_path, source_event["first_line"], source_event["last_line"]
                        )
                    ],
                    "target_components": [
                        component_for_range(
                            target_path, target_event["first_line"], target_event["last_line"]
                        )
                    ],
                    "qa": "qa/terminology_qa/NATIVE_INDONESIAN_TERMINOLOGY_AUDIT_20260831.md",
                    "translated_at": TRANSLATED_AT,
                    "notes": (
                        "Deterministic logical-unit index aligned by the complete ordered TeX structural "
                        "event stream; the stable neutral token is independent of translated title and page number."
                    ),
                }
                if source_event["unit_kind"] == "exercise":
                    row["exercise_metadata"] = {
                        "response_expected": True,
                        "answer_format": "other",
                        "solution_status": "unknown",
                        **({"source_number": label} if label else {}),
                    }
                rows.append(row)
                if source_event["event_type"] == "environment":
                    active.append((source_event["end_offset"], identity["unit_id"], source_event["unit_kind"]))

    return rows


def coverage_rows() -> list[dict]:
    rows: list[dict] = []
    for resource_id, metadata in RESOURCE_METADATA.items():
        for filename in metadata["files"]:
            source_path = f"{metadata['source_root']}/{filename}"
            target_path = f"{metadata['target_root']}/{filename}"
            rows.append(
                {
                    "schema": SCHEMA,
                    "unit_id": f"{metadata['namespace']}.canonical-file.{slug(filename)}",
                    "resource_id": resource_id,
                    "edition_id": metadata["edition_id"],
                    "locale": "id-ID",
                    "title_source": f"Canonical TeX file: {filename}",
                    "title_target": f"Berkas TeX kanonik: {filename}",
                    "state": "structurally_verified",
                    "rights_id": metadata["rights_id"],
                    "coverage_kind": COVERAGE_KIND,
                    "source_components": [coverage_component(source_path)],
                    "target_components": [coverage_component(target_path)],
                    "qa": "qa/terminology_qa/NATIVE_INDONESIAN_TERMINOLOGY_AUDIT_20260831.md",
                    "translated_at": TRANSLATED_AT,
                    "notes": (
                        "Deterministic complete-file coverage binding for the canonical reader tree. "
                        "It complements, without replacing, the retained fine-grained logical units; "
                        "intermediate sprint packets, slides, WIP files, and generated build products are excluded."
                    ),
                }
            )
    for support in DERIVATIVE_SUPPORT:
        metadata = RESOURCE_METADATA[support["resource_id"]]
        rows.append(
            {
                "schema": SCHEMA,
                "unit_id": support["unit_id"],
                "resource_id": support["resource_id"],
                "edition_id": metadata["edition_id"],
                "locale": "id-ID",
                "title_source": support["title_source"],
                "title_target": support["title_target"],
                "state": "structurally_verified",
                "rights_id": metadata["rights_id"],
                "coverage_kind": COVERAGE_KIND,
                "derivative_support": True,
                "source_components": [coverage_component(support["source_path"])],
                "target_components": [coverage_component(support["target_path"])],
                "qa": "qa/terminology_qa/NATIVE_INDONESIAN_TERMINOLOGY_AUDIT_20260831.md",
                "translated_at": TRANSLATED_AT,
                "notes": (
                    "Edition-local id-ID support file with no one-to-one upstream file. The upstream "
                    "reader driver is bound only as the provenance anchor; no content-equivalence claim is made."
                ),
            }
        )
    return sorted(rows, key=lambda row: (row["resource_id"], row["unit_id"]))


def refresh_direct_hashes(row: dict) -> tuple[int, int]:
    refreshed = 0
    unresolved = 0
    for side in ("source_components", "target_components"):
        for component in row[side]:
            path = lane_path(component["path"])
            bounds = raw_bounds(component["selector"])
            if not path.is_file() or bounds is None:
                unresolved += 1
                continue
            current = digest(selected_bytes(path, component["selector"]))
            if component.get("sha256") != current:
                component["sha256"] = current
                refreshed += 1
    return refreshed, unresolved


def load_rows() -> list[dict]:
    data = MANIFEST.read_bytes()
    if not data.endswith(b"\n") or b"\r" in data:
        raise RuntimeError("live manifest must be LF-only canonical JSONL with final newline")
    rows = [json.loads(line) for line in data.decode("utf-8").splitlines()]
    return [
        row
        for row in rows
        if row.get("coverage_kind") != COVERAGE_KIND and row.get("index_kind") != INDEX_KIND
    ]


def validate_rows(rows: list[dict]) -> None:
    required = {
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
    unit_ids: set[str] = set()
    for index, row in enumerate(rows, 1):
        missing = required - set(row)
        if missing:
            raise RuntimeError(f"manifest row {index} missing fields: {sorted(missing)}")
        if row["schema"] != SCHEMA or row["locale"] != "id-ID":
            raise RuntimeError(f"manifest row {index} has incompatible schema/locale")
        if any(token in row["state"].casefold() for token in ("pending", "checkpoint", "draft", "partial")):
            raise RuntimeError(f"nonfinal manifest state remains: {row['unit_id']}={row['state']}")
        if row["unit_id"] in unit_ids:
            raise RuntimeError(f"duplicate unit_id: {row['unit_id']}")
        unit_ids.add(row["unit_id"])
        metadata = RESOURCE_METADATA.get(row["resource_id"])
        if metadata is None:
            raise RuntimeError(f"unknown resource_id: {row['resource_id']}")
        if row["rights_id"] != metadata["rights_id"]:
            raise RuntimeError(f"cross-resource rights mismatch: {row['unit_id']}")
        if not row["source_components"] or not row["target_components"]:
            raise RuntimeError(f"empty component list: {row['unit_id']}")
    coverage = [row for row in rows if row.get("coverage_kind") == COVERAGE_KIND]
    if len(coverage) != 32:
        raise RuntimeError(f"expected 32 canonical TeX coverage units, found {len(coverage)}")
    target_paths = {
        component["path"]
        for row in coverage
        for component in row["target_components"]
    }
    if len(target_paths) != 32:
        raise RuntimeError("canonical TeX target coverage is not one-to-one")
    logical = [row for row in rows if row.get("index_kind") == INDEX_KIND]
    logical_ids = {row["unit_id"] for row in logical}
    for row in logical:
        parent = row.get("parent_unit_id")
        if parent is not None and parent not in logical_ids:
            raise RuntimeError(f"unresolved logical parent: {row['unit_id']} -> {parent}")
    exercises = [row for row in logical if row.get("unit_kind") == "exercise"]
    solutions = [row for row in logical if row.get("unit_kind") == "solution"]
    if len(exercises) != 2169:
        raise RuntimeError(f"expected 2,169 exercise units, found {len(exercises)}")
    if len(solutions) != 251:
        raise RuntimeError(f"expected 251 R007 solution units, found {len(solutions)}")


def write_manifest(out: Path) -> dict:
    rows = load_rows()
    normalized_nonfinal_states = 0
    for row in rows:
        if row.get("state") in NONFINAL_STATES:
            row["state"] = "structurally_verified"
            normalized_nonfinal_states += 1
    refreshed = 0
    unresolved = 0
    for row in rows:
        changed, skipped = refresh_direct_hashes(row)
        refreshed += changed
        unresolved += skipped
    coverage = coverage_rows()
    logical = logical_rows()
    generated = coverage + logical
    rows.extend(generated)
    validate_rows(rows)
    data = b"".join(canonical_json(row).encode("utf-8") + b"\n" for row in rows)
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(prefix=f".{out.name}.", dir=out.parent, delete=False) as stream:
        temporary = Path(stream.name)
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, out)
    return {
        "manifest": str(out),
        "rows": len(rows),
        "coverage_rows": len(coverage),
        "logical_rows": len(logical),
        "logical_rows_by_resource": {
            role: sum(row["resource_id"] == role for row in logical) for role in RESOURCE_METADATA
        },
        "exercise_rows": sum(row["unit_kind"] == "exercise" for row in logical),
        "hint_rows": sum(row["unit_kind"] == "hint" for row in logical),
        "solution_rows": sum(row["unit_kind"] == "solution" for row in logical),
        "rights_by_resource": {
            role: metadata["rights_id"] for role, metadata in RESOURCE_METADATA.items()
        },
        "refreshed_direct_component_hashes": refreshed,
        "normalized_nonfinal_states": normalized_nonfinal_states,
        "unresolved_legacy_components": unresolved,
        "bytes": len(data),
        "sha256": digest(data),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=str(MANIFEST))
    arguments = parser.parse_args()
    print(canonical_json(write_manifest(Path(arguments.out).resolve())))
