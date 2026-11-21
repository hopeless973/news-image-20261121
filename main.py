"""Entry for make.fun's 'Sum up 21 November's world news in one image'.

Python 3.13, standard library only, no network.
Copies the pre-built image entry.png (in this repository) to
/output/entry.png byte for byte, so two runs write identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    os.makedirs("/output", exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = "/output/entry.png"
    shutil.copyfile(src, dst)
    # Leave the output world-readable so the grader can read it.
    os.chmod(dst, 0o644)


if __name__ == "__main__":
    main()
