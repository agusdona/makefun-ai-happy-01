# Make the AI Judge Happy — ai-happy-01

Entry for the [make.fun](https://make.fun) competition **ai-happy-01**
("Make the AI judge happy", $250 USDC prize pool).

## The image

**"We Drew You a Window."** A typeset letter headed "DEAR JUDGE," from
two kids, Maya (7) and Ben (5), sits above their crayon drawing of a small
robot judge at an open window, with a sun, a bird, a tree, and a dog. The
letter explains they drew the judge a window so it can look at something
that is not a picture; the P.S. admits the bird isn't real either — they
are working on it.

The image is a 1024×1024 PNG, 591,359 bytes (0.56 MiB, under the 1 MiB
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
