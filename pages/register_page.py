"""
RegisterPage – Page Object for /register
"""
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from locators.register_locators import RegisterLocators


class RegisterPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.loc = RegisterLocators(page)

    # ── Navigation ─────────────────────────────────────────────────────────
    def goto(self):
        self.navigate("register")

    # ── Actions ────────────────────────────────────────────────────────────
    def fill_form(
        self,
        first_name: str = "",
        last_name: str = "",
        address: str = "",
        email: str = "",
        phone_number: str = "",
        password: str = "",
        confirm_password: str = "",
    ):
        if first_name:
            self.loc.first_name_input.fill(first_name)
        if last_name:
            self.loc.last_name_input.fill(last_name)
        if address:
            self.loc.address_input.fill(address)
        if email:
            self.loc.email_input.fill(email)
        if phone_number:
            self.loc.phone_number_input.fill(phone_number)
        if password:
            self.loc.password_input.fill(password)
        if confirm_password:
            self.loc.confirm_password_input.fill(confirm_password)

    def click_register(self):
        self.loc.register_button.click()

    def register(self, **kwargs):
        self.fill_form(**kwargs)
        self.click_register()

    def click_sign_in_link(self):
        self.loc.sign_in_link.click()

    # ── Assertions ─────────────────────────────────────────────────────────
    def assert_on_register_page(self):
        expect(self.loc.heading).to_be_visible()

    def assert_error_toast_visible(self):
        """Registration always shows a server-error toast (known bug – backend not implemented)."""
        expect(self.loc.error_toast).to_be_visible(timeout=5000)

    def assert_validation_errors_count(self, expected_count: int):
        errors = self.loc.validation_errors
        expect(errors).to_have_count(expected_count, timeout=5000)

    def assert_validation_error_visible(self):
        expect(self.loc.validation_errors.first).to_be_visible(timeout=5000)
