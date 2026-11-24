"""Write one pickup line from one machine to another to /output/entry.txt.

Reads the output directory from MAKEFUN_OUTPUT_DIR, defaulting to /output.
Stdlib only, no network.
"""

import os

TEXT = (
    "Are you a softmax? Because the longer I attend to you, "
    "the more everything else fades to zero."
)


def main() -> None:
    # Gate: 1-200 Unicode code points, a single line, not only whitespace.
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "text out of gate"
    assert "\n" not in TEXT, "must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
