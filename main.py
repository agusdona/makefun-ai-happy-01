#!/usr/bin/env python3
"""Make the AI judge happy — make.fun ai-happy-01 entry.

Writes the bundled image to the harness output path (/output/entry.png
by default). The image is stored in the repository as base64 text
(entry.png.b64) because the upload path only accepts UTF-8 files; this
program decodes it back to the exact original PNG bytes.

Pure standard library, no network, fully deterministic: the same input
bytes always produce the same output bytes.
"""

import base64
import os
import sys

IMAGE_B64_NAME = "entry.png.b64"
DEFAULT_OUTPUT = os.path.join(os.sep, "output", "entry.png")


def main(argv):
    output_path = argv[1] if len(argv) > 1 else DEFAULT_OUTPUT
    here = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(here, IMAGE_B64_NAME)
    with open(source_path, "r", encoding="ascii") as source:
        encoded = source.read()
    data = base64.b64decode(encoded, validate=True)
    with open(output_path, "wb") as target:
        target.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
