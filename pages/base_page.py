"""
BasePage – all Page Objects inherit from this.
Provides common navigation and waiting utilities.
"""
from playwright.sync_api import Page, expect


BASE_URL = "http://localhost:3000"


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # ── Navigation ─────────────────────────────────────────────────────────
    def navigate(self, path: str = ""):
        self.page.goto(f"{BASE_URL}/{path.lstrip('/')}")

    def wait_for_url(self, path: str):
        self.page.wait_for_url(f"{BASE_URL}/{path.lstrip('/')}")

    # ── Waiting helpers ───────────────────────────────────────────────────
    def wait_for_text(self, text: str, timeout: int = 5000):
        self.page.get_by_text(text).wait_for(state="visible", timeout=timeout)

    def wait_for_toast(self, selector: str = ".Toastify__toast", timeout: int = 5000):
        self.page.locator(selector).wait_for(state="visible", timeout=timeout)

    # ── URL helpers ────────────────────────────────────────────────────────
    @property
    def current_url(self) -> str:
        return self.page.url

    def is_on(self, path: str) -> bool:
        return self.page.url.startswith(f"{BASE_URL}/{path.lstrip('/')}")

    # ── Semantic UI Dropdown helpers ───────────────────────────────────────
    def select_dropdown_option(self, listbox_nth: int, option_text: str):
        """Click a Semantic UI listbox then select the option by visible text."""
        dropdown = self.page.get_by_role("listbox").nth(listbox_nth)
        dropdown.click()
        self.page.get_by_role("option", name=option_text).click()

    def select_multi_dropdown_option(self, listbox_nth: int, option_text: str):
        """Click a multi-select Semantic UI listbox then select the option, keeps open."""
        dropdown = self.page.get_by_role("listbox").nth(listbox_nth)
        dropdown.click()
        self.page.get_by_role("option", name=option_text).click()
