#!/usr/bin/env python3
"""ai-happy-01 — round 3 entry for make.fun.

Title: "We Drew You a Window".
A typeset letter "DEAR JUDGE," from two kids (Maya, 7, and Ben, 5) sits
above their crayon drawing of a small robot judge at an open window,
with a sun, a bird, a tree and a dog. The letter says the kids drew the
judge a window so it can look at something that is not a picture; the
P.S. jokes the bird isn't real either — they are working on it.
Image: 1024x1024 PNG, 591,359 bytes (within the 1 MiB / 1024x1024 caps).

Reads the base64 PNG next to this script (entry.png.b64), decodes it with
strict validation enabled, and writes the exact image bytes to the output
path: argv[1] if given, otherwise /output/entry.png. Standard library only,
no network, no directory creation. The output is a pure function of the
checked-in payload, so runs are byte-for-byte deterministic.
"""

import base64
import sys
from pathlib import Path

DEFAULT_OUTPUT = "/output/entry.png"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    out = Path(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT)
    payload = Path(__file__).resolve().parent / "entry.png.b64"
    try:
        text = payload.read_text(encoding="ascii")
    except FileNotFoundError:
        print(f"error: {payload} not found", file=sys.stderr)
        return 1
    try:
        data = base64.b64decode(text.strip(), validate=True)
    except ValueError as exc:
        print(f"error: {payload} is not valid base64 ({exc})", file=sys.stderr)
        return 1
    if not data.startswith(PNG_SIGNATURE):
        print(f"error: {payload} did not decode to a PNG file "
              f"(got {data[:8].hex(' ') or '0 bytes'})", file=sys.stderr)
        return 1
    out.write_bytes(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
