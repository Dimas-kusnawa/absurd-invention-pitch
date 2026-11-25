"""One-sentence absurd invention pitch for make.fun.

Writes the pitch to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic: same output on every run.
"""

import os

# The pitch, and why it should win:
# - Annoyance: losing one sock in every wash (tiny, universal).
# - Invention: socks that pair themselves in the dryer.
# - Silly mechanism: they leave a note saying "we eloped".
# - The laugh comes from the invention itself, not a bolted-on joke,
#   and the fix is silly yet weirdly plausible: the socks solve the
#   problem by running away together, on purpose.
PITCH = (
    "A pair of socks that finds its own match in the dryer "
    "and leaves a note saying 'we eloped', "
    "so you stop losing one every wash."
)


def main() -> None:
    # Gate from RULES.txt: 1 to 220 UTF-8 chars, one sentence, no newline.
    assert 1 <= len(PITCH) <= 220, f"pitch is {len(PITCH)} chars"
    assert "\n" not in PITCH, "pitch must be a single line"
    assert PITCH.count(".") == 1, "pitch must be one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)
    print(f"wrote {path}: {PITCH} ({len(PITCH)} chars)")


if __name__ == "__main__":
    main()
