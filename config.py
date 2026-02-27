"""
config.py – Central configuration for the Teebay automation test suite.

All values can be overridden by environment variables, which lets GitHub
Actions (or any CI system) run headless without changing this file:

    HEADED=false SLOW_MO=0 pytest

Local defaults (headed browser, 500 ms delay) are preserved when env vars
are absent, so local development works without any extra flags.
"""
import os

# ── Application ────────────────────────────────────────────────────────────────
BASE_URL = os.environ.get("BASE_URL", "http://localhost:3000")

# ── Browser settings ───────────────────────────────────────────────────────────
# Env var  HEADED=false  → headless (CI default)
# Env var  HEADED=true   → headed  (local default)
HEADED  = os.environ.get("HEADED",  "true").strip().lower() == "true"
# Env var  SLOW_MO=0     → no delay (CI)  |  500 → 500 ms delay (local)
SLOW_MO = int(os.environ.get("SLOW_MO", "500"))

# ── Test credentials ───────────────────────────────────────────────────────────
# Override via GitHub Secrets: TEST_EMAIL / TEST_PASSWORD
TEST_EMAIL    = os.environ.get("TEST_EMAIL",    "testuser@teebay.com")
TEST_PASSWORD = os.environ.get("TEST_PASSWORD", "123456")
