# -*- coding: utf-8 -*-
"""Build the whole site, in order, in ONE process.

Why one process: build_white.py regenerates every page at import time. Running the
stage scripts separately means the last one to import it clobbers pages an earlier
stage had already specialised — which is exactly how find.html silently reverted to
its placeholder once build_pubcrawl.py was added. Inside a single process the import
is cached, so build_white runs once and each stage's output survives.

Usage:  CALDERA_SITE=../_work/site python3 build_all.py
"""
import golive          # noqa: F401  -- pages + 404, robots.txt, sitemap.xml, _redirects
import build_find      # noqa: F401  -- replaces find.html with the outlet directory
import build_pubcrawl  # noqa: F401  -- adds pubcrawl.html
import seo             # noqa: F401  -- titles, descriptions, JSON-LD, llms.txt  (must be LAST)

print("build_all: done")
