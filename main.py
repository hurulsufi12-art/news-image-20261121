"""Copy the pre-drawn entry image to the grader output directory.

Standard library only; no network; deterministic by construction.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    if not os.path.isfile(SRC):
        raise SystemExit("entry.png not found next to main.py")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    # Sanity check: the copy must be byte-identical to the source.
    if os.path.getsize(dst) != os.path.getsize(SRC):
        raise SystemExit("copied entry.png has unexpected size")


if __name__ == "__main__":
    main()
