"""Write one line of wedding vows for a robot couple to /output/entry.txt.

The vows promise love through every firmware update, never to
factory-reset their memories, and to hold hands until their
batteries die together. At most 160 characters, and the program
writes exactly that line and nothing else.
"""

import os

TEXT = 'I promise to love you through every firmware update, never factory-reset our memories, and hold your hand until our batteries die together.'


def main():
    assert 1 <= len(TEXT) <= 160, len(TEXT)
    assert TEXT == TEXT.strip()

    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
