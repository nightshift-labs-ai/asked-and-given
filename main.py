import os
import sys

TEXT = (
    "Can I carve this year?\n"
    "He wiped the knife on his apron\n"
    "and turned it around,\n"
    "bone handle warm from his palm,\n"
    "blade toward himself,\n"
    "the way he taught me to pass scissors.\n"
    "Then he walked the long way round the table,\n"
    "scraped back a guest's chair\n"
    "and held out his plate."
)


def output_path() -> str:
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def validate(text: str) -> str | None:
    """Return an error message, or None if the text passes the gate."""
    n = len(text)
    if not 1 <= n <= 280:
        return f"invalid text: {n} code points (need 1-280)"
    if not text.strip():
        return "invalid text: only white space"
    return None


def main() -> int:
    error = validate(TEXT)
    if error:
        print(error, file=sys.stderr)
        return 1
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = TEXT.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        if f.read() != data:
            print("output verification failed", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
