#!/usr/bin/env python3
r"""Create a deterministic TeX prefix that returns cleanly to its driver.

The source is never modified.  The selected inclusive raw-line boundary must
end outside an open TeX environment; the caller records that semantic gate in
the release receipt.  Output is UTF-8 with the source's existing line endings
preserved through the chosen boundary, followed by a provenance comment. TeX
returns to the calling ``\input`` at end-of-file; omitting ``\endinput`` also
keeps the book's bounded LaTeX-to-PreTeXt converter at zero errors.
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--through-line", type=int, required=True)
    args = parser.parse_args()

    if args.through_line < 1:
        raise SystemExit("--through-line must be positive")
    if args.source.resolve() == args.output.resolve():
        raise SystemExit("source and output must differ")
    if args.output.exists():
        raise SystemExit(f"refusing existing output: {args.output}")

    source_bytes = args.source.read_bytes()
    lines = source_bytes.splitlines(keepends=True)
    if args.through_line > len(lines):
        raise SystemExit(
            f"boundary {args.through_line} exceeds {len(lines)} source lines"
        )

    selected = b"".join(lines[: args.through_line])
    if selected and not selected.endswith((b"\n", b"\r")):
        selected += b"\n"
    trailer = b"% Deterministic reader cutoff after the admitted semantic boundary.\n"
    output_bytes = selected + trailer
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(output_bytes)

    print(
        f"source_bytes={len(source_bytes)} "
        f"source_sha256={digest(source_bytes)} "
        f"selected_lines={args.through_line} "
        f"output_bytes={len(output_bytes)} "
        f"output_sha256={digest(output_bytes)}"
    )


if __name__ == "__main__":
    main()
