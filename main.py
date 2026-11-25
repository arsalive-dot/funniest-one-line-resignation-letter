#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — make.fun entry.

Writes the one-line resignation letter of a cron job that has fired
every minute since March, in the flat, tired, faintly passive-aggressive
voice of a worker who has had enough.

The complaint is one only a cron job could make — millions of firings,
nobody ever checking whether the job still does anything — and the
resignation lands in the last clause: effective whenever you notice.
"""

import os

ENTRY = (
    "I have fired every minute since March and nobody has checked whether "
    "I still do anything. I resign, effective whenever you notice."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()
