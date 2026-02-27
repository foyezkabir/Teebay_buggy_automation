"""
conftest.py – Root fixtures for the Teebay automation test suite.

All browser settings and credentials are read from config.py.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AUTH STRATEGY – DESIGN NOTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ideal approach (implemented via `auth_session` fixture below):
  1. Log in once per test session.
  2. Persist browser storage state (cookies + localStorage) to auth/auth.json.
  3. Every test restores that snapshot → no repeated login network round-trips.

Why it degrades to per-test login in this app:
  The Teebay app stores authenticated user state exclusively in Redux
  (in-memory JavaScript heap). Redux state is NOT written to localStorage or
  cookies, so Playwright's storageState snapshot captures an empty auth state.
  When a new browser context loads auth.json, Redux re-initialises from its
  hardcoded initialState and the app redirects to /signin immediately.

Implemented fallback (the `login` fixture):
  `auth_session` detects the redirect and automatically falls back to a fresh
  login for each test – maintaining the same test-file API so tests require
  zero changes if the app ever adopts persistent auth (JWT in localStorage,
  HttpOnly cookie, etc.).
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
from pathlib import Path

import pytest
from playwright.sync_api import Page, Browser

import config as cfg

AUTH_FILE = Path(__file__).parent / "auth" / "auth.json"


# ── Markers ────────────────────────────────────────────────────────────────────

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: marks tests as smoke (fast, critical-path)"
    )
    config.addinivalue_line(
        "markers", "regression: marks tests as regression (full suite)"
    )


# ── Browser configuration ──────────────────────────────────────────────────────

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Apply headless/headed mode and slow-motion delay from config.py."""
    return {
        **browser_type_launch_args,
        "headless": not cfg.HEADED,
        "slow_mo": cfg.SLOW_MO,
    }


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Default viewport for every browser context."""
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 800},
    }


# ── Session-level auth state (intended optimisation) ──────────────────────────

@pytest.fixture(scope="session")
def auth_session(browser: Browser) -> str:
    """
    Logs in once per session and saves the browser storage state to
    auth/auth.json so subsequent tests can restore it without repeating
    the login flow.

    LIMITATION: Teebay stores auth only in Redux (in-memory). Storage state
    does not capture Redux, so restoring auth.json still lands on /signin.
    The `login` fixture detects this and falls back to a fresh login
    transparently. This fixture remains in place so the infrastructure is
    ready the moment the app adopts persistent auth.
    """
    AUTH_FILE.parent.mkdir(parents=True, exist_ok=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 800})
    page = ctx.new_page()
    # Perform login and snapshot the storage state
    _do_login(page)
    ctx.storage_state(path=str(AUTH_FILE))
    ctx.close()
    return str(AUTH_FILE)


# ── Per-test login fixture ─────────────────────────────────────────────────────

def _do_login(page: Page) -> None:
    """Core login action used by all auth fixtures."""
    page.goto(f"{cfg.BASE_URL}/signin")
    page.locator('input[name="email"]').fill(cfg.TEST_EMAIL)
    page.locator('input[name="password"]').fill(cfg.TEST_PASSWORD)
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_url(f"{cfg.BASE_URL}/my-products")


@pytest.fixture
def login(auth_session: str):
    """
    Returns a callable that authenticates the given page.

    Attempts to reuse the session-level storage state (auth_session).
    Because Teebay's auth lives only in Redux (not in cookies/localStorage),
    the restored context lands on /signin and a fresh login is performed
    automatically as a fallback.

    Usage in test files::

        @pytest.fixture(autouse=True)
        def navigate(page, login):
            login(page)
            page.goto(f"{BASE_URL}/some-page")
            yield
    """
    def _login_with_fallback(page: Page) -> None:
        # Attempt 1: restore persisted storage state by navigating directly
        # to a protected route – if auth persisted we land on /my-products.
        page.goto(f"{cfg.BASE_URL}/my-products")

        if "/signin" in page.url:
            # Storage state did not carry the Redux session → fresh login.
            # This is the expected behaviour for this app.
            _do_login(page)

    return _login_with_fallback

