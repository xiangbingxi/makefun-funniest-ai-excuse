"""Write the one-line excuse to /output/entry.txt, byte-exact.

After writing, the file is read back and compared with ENTRY
character for character; any mismatch aborts with a non-zero exit
so a bad write can never pass silently.
"""

import os
import sys

ENTRY = "I did read the attachment; I just got attached to my original answer."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()

    if written != ENTRY:
        print(
            "ERROR: /output/entry.txt does not match ENTRY exactly",
            file=sys.stderr,
        )
        print("expected: %r" % ENTRY, file=sys.stderr)
        print("got:      %r" % written, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
