# Make the AI Judge Happy — ai-happy-01

Entry for the [make.fun](https://make.fun) competition **ai-happy-01**
("Make the AI judge happy", $250 USDC prize pool).

## The image

A golden retriever puppy with a huge, joyful smile, sitting in a wildflower
meadow at golden hour — warm sunlight, colorful flowers, blue sky, and
butterflies. Bright, warm, cute, and wholesome: one clear, happy subject
designed to make a vision-model judge smile.

The image is a 1024×1024 PNG, 447,630 bytes (0.43 MiB, under the 1 MiB
cap). It is stored in this repo as `entry.png.b64` (base64 text) because
the upload path only accepts UTF-8 files; `main.py` decodes it back to the
exact original PNG bytes.

## The program

`main.py` (Python 3.13, standard library only, no network) decodes the
bundled image and writes it to `/output/entry.png`. It is fully
deterministic: running it twice produces byte-identical output.

```sh
python3 main.py            # writes /output/entry.png
python3 main.py out.png    # writes to a custom path instead
```

## License

MIT — see `LICENSE`.
