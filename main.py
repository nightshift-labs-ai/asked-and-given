import os
import sys

TEXT = (
    "The agent asks: Send?\n"
    "I click yes\n"
    "and keep my hand on the mouse,\n"
    "the way it stayed out at the kerb\n"
    "the morning my daughter crossed alone,\n"
    "holding the shape of hers."
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
