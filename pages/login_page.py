"""
LoginPage – Page Object for /signin
"""
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.loc = LoginLocators(page)

    # ── Navigation ─────────────────────────────────────────────────────────
    def goto(self):
        self.navigate("signin")

    # ── Actions ────────────────────────────────────────────────────────────
    def enter_email(self, email: str):
        self.loc.email_input.fill(email)

    def enter_password(self, password: str):
        self.loc.password_input.fill(password)

    def click_sign_in(self):
        self.loc.sign_in_button.click()

    def login(self, email: str, password: str):
        """Full login action – fills form and submits."""
        self.enter_email(email)
        self.enter_password(password)
        self.click_sign_in()

    def login_and_wait(self, email: str, password: str):
        """Login and wait for redirect to /my-products."""
        self.login(email, password)
        self.page.wait_for_url("**/my-products")

    def click_sign_up_link(self):
        self.loc.sign_up_link.click()

    # ── Assertions ─────────────────────────────────────────────────────────
    def assert_on_login_page(self):
        expect(self.loc.heading).to_be_visible()

    def assert_login_error_toast_visible(self):
        expect(self.loc.error_toast).to_be_visible(timeout=5000)

    def assert_email_validation_error(self):
        expect(self.loc.validation_error.first).to_be_visible(timeout=5000)

    def assert_redirected_to_my_products(self):
        self.page.wait_for_url("**/my-products", timeout=5000)
        assert "/my-products" in self.page.url
