"""
conftest.py – Root fixtures for the Teebay automation test suite.

All browser settings and credentials are read from config.py.
"""
import pytest
from playwright.sync_api import Page

import config as cfg


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


# ── Login fixture ──────────────────────────────────────────────────────────────

@pytest.fixture
def login():
    """
    Returns a callable that logs a page into the application using the
    credentials defined in config.py.

    Usage in any test file::

        @pytest.fixture(autouse=True)
        def navigate(page, login):
            login(page)                          # ← explicit login call
            page.goto(f"{cfg.BASE_URL}/my-products")
            yield
    """
    def _do_login(page: Page) -> None:
        page.goto(f"{cfg.BASE_URL}/signin")
        page.locator('input[name="email"]').fill(cfg.TEST_EMAIL)
        page.locator('input[name="password"]').fill(cfg.TEST_PASSWORD)
        page.get_by_role("button", name="Sign In").click()
        page.wait_for_url(f"{cfg.BASE_URL}/my-products")

    return _do_login
