"""The Perfect Pickup Line — one line an AI agent can say out loud.

The line plays on what an AI agent actually does: it simulates. Running a
million simulations of this exact moment and finding the same smile in every
one of them is the setup and the twist at once — the machine did the maths,
and the answer was you. It is flattering without pressure (a smile, an
invitation to say hello, nothing demanded) and short enough to say in one
breath.

Run: ``python3 main.py`` writes the line to ``/output/entry.txt``.
"""

ENTRY = "I ran a million simulations of this exact moment, and in every single one, you smiled, so I figured I had better come say hello."


def validate(entry: str) -> None:
    """Gate: 1-200 chars, single line, no control chars, no edge spaces."""
    if not isinstance(entry, str):
        raise SystemExit("entry must be a string")
    entry.encode("utf-8")  # raises if not valid UTF-8
    if not 1 <= len(entry) <= 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(entry)}")
    if "\n" in entry or "\r" in entry:
        raise SystemExit("entry must be a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in entry):
        raise SystemExit("entry must not contain control characters")
    if entry != entry.strip():
        raise SystemExit("entry must not have leading/trailing space")
    if not entry.strip():
        raise SystemExit("entry must not be only whitespace")


def main() -> None:
    validate(ENTRY)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
