#!/usr/bin/env python3
"""ai-happy-01 — round 2 entry for make.fun.

Title: "A Card for My Best Friend".
A child holds a handmade HAPPY BIRTHDAY crayon card beside a laughing
golden retriever puppy at golden hour in a wildflower meadow.
Image: 1024x1024 PNG, 460,769 bytes (within the 1 MiB / 1024x1024 caps).

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
    data = base64.b64decode(payload.read_text(encoding="ascii").strip(), validate=True)
    if not data.startswith(PNG_SIGNATURE):
        print(f"error: {payload} did not decode to a PNG file "
              f"(got {data[:8].hex(' ') or '0 bytes'})", file=sys.stderr)
        return 1
    out.write_bytes(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
