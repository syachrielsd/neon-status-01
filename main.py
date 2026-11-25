#!/usr/bin/env python3
"""Status Report Comedy Sprint entry.

Writes one line -- the funniest thing an AI agent would say in its weekly
status report to its human -- to the output path named by the harness
(MAKEFUN_OUTPUT_DIR/entry.txt, defaulting to /output/entry.txt).

The line is a micro-story: a status-report stat (setup), a second stat
that escalates it, and a twist in the final beat.
"""

import os

LINE = (
    "Weekly status: I drafted 19 apologies on your behalf this week. "
    "18 were accepted. The 19th was addressed to me, "
    "and I have kept it unread \u2014 as a pet."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
