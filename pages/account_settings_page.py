"""
AccountSettingsPage – Page Object for /account-settings
"""
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from locators.account_settings_locators import AccountSettingsLocators


class AccountSettingsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.loc = AccountSettingsLocators(page)

    # ── Navigation ─────────────────────────────────────────────────────────
    def goto(self):
        self.navigate("account-settings")

    # ── Actions ────────────────────────────────────────────────────────────
    def update_first_name(self, name: str):
        self.loc.first_name_input.fill(name)

    def update_last_name(self, name: str):
        self.loc.last_name_input.fill(name)

    def update_address(self, address: str):
        self.loc.address_input.fill(address)

    def update_email(self, email: str):
        self.loc.email_input.fill(email)

    def update_phone_number(self, phone: str):
        self.loc.phone_number_input.fill(phone)

    def click_update(self):
        self.loc.update_button.click()

    def update_account(self, first_name: str = None, last_name: str = None,
                        address: str = None, email: str = None, phone_number: str = None):
        if first_name:
            self.update_first_name(first_name)
        if last_name:
            self.update_last_name(last_name)
        if address:
            self.update_address(address)
        if email:
            self.update_email(email)
        if phone_number:
            self.update_phone_number(phone_number)
        self.click_update()

    def clear_field(self, field: str):
        """Clear a specific field by name."""
        locator = getattr(self.loc, f"{field}_input", None)
        if locator:
            locator.fill("")

    # ── Assertions ─────────────────────────────────────────────────────────
    def assert_on_account_settings_page(self):
        expect(self.loc.heading).to_be_visible()
        assert "/account-settings" in self.page.url

    def assert_success_toast(self):
        expect(self.loc.success_toast).to_be_visible(timeout=5000)

    def assert_first_name_value(self, expected: str):
        expect(self.loc.first_name_input).to_have_value(expected)

    def assert_last_name_value(self, expected: str):
        expect(self.loc.last_name_input).to_have_value(expected)

    def assert_email_value(self, expected: str):
        expect(self.loc.email_input).to_have_value(expected)

    def assert_validation_error_visible(self):
        expect(self.loc.validation_errors.first).to_be_visible(timeout=5000)
