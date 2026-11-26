"""Entry for make.fun: One-Sentence Absurd Invention Pitch.

The Shush Cushion rescues guests from weather small talk.
"""
import os

LINE = "Introducing the Shush Cushion: a sofa pillow that detects small talk about the weather and gently ejects the guest into a more interesting conversation."
MAX_CHARS = 220


def write_entry(out_dir):
    assert LINE.strip(), "entry must not be empty"
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))


if __name__ == "__main__":
    main()
