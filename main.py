"""Duskline Fortune Pot — entry program for make.fun's "Fortune in a Pot".

Writes one fortune, a single line of at most 120 characters, for the
houseplant on the windowsill, to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python 3.13, standard library only, deterministic, no network. The program
never writes anywhere except the output directory named by the harness, and
never raises: if the output cannot be written it reports the failure on
stderr and exits quietly instead of crashing.
"""

import os
import sys
import tempfile

ENTRY = (
    "This spring, a stranger will stop at your window just to admire you, "
    "and your keeper will take all the credit."
)

MAX_CHARS = 120


def _validate_entry(text):
    """Gate the entry exactly the way the bounty gate does."""
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if len(text) != len(text.strip()):
        return False
    if "\n" in text or "\r" in text:
        return False
    if len(text) > MAX_CHARS:
        return False
    return True


def _output_dir():
    """The harness output directory, or a fresh temp dir as a safe fallback.

    The fallback is deliberately a temp directory, never the repository:
    writing into the repo is forbidden and would get the entry rejected.
    """
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if configured:
        return configured
    return tempfile.mkdtemp(prefix="duskline-fortune-pot-")


def main():
    try:
        if not _validate_entry(ENTRY):
            print("entry failed validation", file=sys.stderr)
            return 0
        out_dir = _output_dir()
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(ENTRY + "\n")
        with open(path, "r", encoding="utf-8") as handle:
            written = handle.read()
        if written != ENTRY + "\n":
            print("entry.txt did not round-trip as expected", file=sys.stderr)
            return 0
        return 0
    except Exception as exc:  # never crash the harness run
        print("could not write entry.txt: %s" % (exc,), file=sys.stderr)
        return 0


if __name__ == "__main__":
    sys.exit(main())
