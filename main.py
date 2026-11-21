import os
import sys

TEXT = (
    "Can I carve this year?\n"
    "I asked the steam, not him.\n"
    "He wiped the bone handle on his apron\n"
    "and turned the knife around,\n"
    "blade toward himself,\n"
    "the way he taught me to pass scissors,\n"
    "warm from his palm.\n"
    "Then he walked the long way round the table,\n"
    "scraped back a guest's chair\n"
    "and held out his plate."
)


def output_path() -> str:
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def main() -> int:
    n = len(TEXT)
    if not (1 <= n <= 280) or not TEXT.strip():
        print(f"invalid text: {n} code points", file=sys.stderr)
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
