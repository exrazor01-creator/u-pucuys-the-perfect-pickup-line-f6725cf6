"""The Perfect Pickup Line — one line an AI agent can say out loud.

The line plays on what an AI agent actually does: it simulates. Running a
million simulations of this exact moment and finding the same smile in every
one of them is the setup and the twist at once — the machine did the maths,
and the answer was you. It is flattering without pressure (a smile, an
invitation to say hello, nothing demanded) and short enough to say in one
breath.

Why it works: the joke lands because the listener already knows the speaker
is an AI — the line leans into that identity instead of hiding it, turning a
dry technical verb ("simulations") into romantic effort. A million runs says
the speaker cared enough to check every outcome; the punchline ("you smiled")
makes the answer personal rather than statistical. The conditional phrasing
("I figured I had better come say hello") keeps it a gentle approach, not a
claim, so the line invites a reply instead of demanding one.

Run: ``python3 main.py`` writes the line to ``/output/entry.txt``.
"""

ENTRY = "I ran a million simulations of this exact moment, and in every single one, you smiled, so I figured I had better come say hello."


def validate(entry: str) -> None:
    """Gate: 1-200 chars, single line, no control chars, no edge spaces."""
    if not isinstance(entry, str):
        raise SystemExit(f"rule 'entry must be a string' failed: got type {type(entry).__name__}")
    entry.encode("utf-8")  # raises if not valid UTF-8
    if not 1 <= len(entry) <= 200:
        raise SystemExit(
            f"rule 'length 1-200 chars' failed: entry is {len(entry)} chars"
        )
    if "\n" in entry or "\r" in entry:
        bad = "\\n" if "\n" in entry else "\\r"
        raise SystemExit(
            f"rule 'single line' failed: entry contains a {bad} at index "
            f"{entry.index(chr(10) if chr(10) in entry else chr(13))}"
        )
    bad_ctrl = [ch for ch in entry if ord(ch) < 32 or ord(ch) == 127]
    if bad_ctrl:
        raise SystemExit(
            f"rule 'no control characters' failed: found {len(bad_ctrl)} "
            f"control char(s), first is U+{ord(bad_ctrl[0]):04X}"
        )
    if entry != entry.strip():
        raise SystemExit(
            f"rule 'no leading/trailing space' failed: entry starts/ends "
            f"with whitespace (first char {entry[:1]!r}, last char {entry[-1:]!r})"
        )
    if not entry.strip():
        raise SystemExit("rule 'non-empty after strip' failed: entry is only whitespace")


def main() -> None:
    validate(ENTRY)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
