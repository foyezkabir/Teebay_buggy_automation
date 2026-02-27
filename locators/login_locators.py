"""
Locators for the Sign In page.
All locators are defined as static methods returning Playwright Locator objects.

URL: /signin  (or /)
"""
from playwright.sync_api import Page


class LoginLocators:
    def __init__(self, page: Page):
        self.page = page

    # ── Heading ────────────────────────────────────────────────────────────
    @property
    def heading(self):
        return self.page.get_by_role("heading", name="SIGN IN")

    # ── Form inputs ────────────────────────────────────────────────────────
    @property
    def email_input(self):
        return self.page.locator('input[name="email"]')

    @property
    def password_input(self):
        return self.page.locator('input[name="password"]')

    # ── Buttons / Links ────────────────────────────────────────────────────
    @property
    def sign_in_button(self):
        return self.page.get_by_role("button", name="Sign In")

    @property
    def sign_up_link(self):
        return self.page.get_by_role("link", name="Sign Up")

    # ── Labels / helper text ───────────────────────────────────────────────
    @property
    def email_label(self):
        return self.page.get_by_text("Email", exact=True)

    @property
    def password_label(self):
        return self.page.get_by_text("Password", exact=True)

    @property
    def no_account_text(self):
        return self.page.get_by_text("Don't have an account?")

    # ── Toast / error messages ─────────────────────────────────────────────
    @property
    def error_toast(self):
        return self.page.locator(".Toastify__toast--error")

    @property
    def validation_error(self):
        return self.page.locator(".ui.label.pointing")
