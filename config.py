"""
config.py – Central configuration for the Teebay automation test suite.

Edit this file to change browser behaviour, target URL, or test credentials
without touching any test or page-object code.
"""

# ── Application ────────────────────────────────────────────────────────────────
BASE_URL = "http://localhost:3000"

# ── Browser settings ───────────────────────────────────────────────────────────
HEADED  = True   # True  → show browser window  |  False → headless (CI)
SLOW_MO = 500    # milliseconds between actions  |  0 → no delay

# ── Test credentials ───────────────────────────────────────────────────────────
TEST_EMAIL    = "testuser@teebay.com"
TEST_PASSWORD = "123456"
