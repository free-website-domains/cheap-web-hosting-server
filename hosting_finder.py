#!/usr/bin/env python3
"""Convenience entrypoint for the Cheap Hosting Finder CLI."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from hosting_finder.cli import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
