"""
Locators for the Account Settings page.

URL: /account-settings
"""
from playwright.sync_api import Page


class AccountSettingsLocators:
    def __init__(self, page: Page):
        self.page = page

    # ── Heading ────────────────────────────────────────────────────────────
    @property
    def heading(self):
        return self.page.get_by_role("heading", name="ACCOUNT SETTINGS")

    # ── Form inputs ────────────────────────────────────────────────────────
    @property
    def first_name_input(self):
        return self.page.locator('input[name="first_name"]')

    @property
    def last_name_input(self):
        return self.page.locator('input[name="last_name"]')

    @property
    def address_input(self):
        return self.page.locator('input[name="address"]')

    @property
    def email_input(self):
        return self.page.locator('input[name="email"]')

    @property
    def phone_number_input(self):
        return self.page.locator('input[name="phone_number"]')

    # ── Labels ────────────────────────────────────────────────────────────
    @property
    def first_name_label(self):
        return self.page.get_by_text("First Name", exact=True)

    @property
    def last_name_label(self):
        return self.page.get_by_text("Last Name", exact=True)

    @property
    def address_label(self):
        return self.page.get_by_text("Address", exact=True)

    @property
    def email_label(self):
        return self.page.get_by_text("Email", exact=True)

    @property
    def phone_number_label(self):
        return self.page.get_by_text("Phone Number", exact=True)

    # ── Buttons ────────────────────────────────────────────────────────────
    @property
    def update_button(self):
        return self.page.get_by_role("button", name="Update")

    # ── Toasts ────────────────────────────────────────────────────────────
    @property
    def success_toast(self):
        return self.page.locator(".Toastify__toast--success")

    @property
    def error_toast(self):
        return self.page.locator(".Toastify__toast--error")

    @property
    def validation_errors(self):
        return self.page.locator(".ui.label.pointing")
