"""
Locators for the Registration page.

URL: /register

Notable bugs (to be captured in test assertions or test notes):
- firstName field validation is missing from the Yup schema.
- confirmPassword field is not validated.
- Successful form submission always shows a server-error toast (backend bug).
"""
from playwright.sync_api import Page


class RegisterLocators:
    def __init__(self, page: Page):
        self.page = page

    # ── Heading ────────────────────────────────────────────────────────────
    @property
    def heading(self):
        return self.page.get_by_role("heading", name="REGISTRATION")

    # ── Form inputs ────────────────────────────────────────────────────────
    @property
    def first_name_input(self):
        return self.page.locator('input[name="firstName"]')

    @property
    def last_name_input(self):
        return self.page.locator('input[name="lastName"]')

    @property
    def address_input(self):
        return self.page.locator('input[name="address"]')

    @property
    def email_input(self):
        return self.page.locator('input[name="email"]')

    @property
    def phone_number_input(self):
        return self.page.locator('input[name="phoneNumber"]')

    @property
    def password_input(self):
        return self.page.locator('input[name="password"]')

    @property
    def confirm_password_input(self):
        return self.page.locator('input[name="confirmPassword"]')

    # ── Buttons / Links ────────────────────────────────────────────────────
    @property
    def register_button(self):
        return self.page.get_by_role("button", name="Register")

    @property
    def sign_in_link(self):
        return self.page.get_by_role("link", name="Sign In")

    # ── Labels ────────────────────────────────────────────────────────────
    @property
    def first_name_label(self):
        return self.page.get_by_text("First Name", exact=True)

    @property
    def last_name_label(self):
        return self.page.get_by_text("Last Name", exact=True)

    @property
    def already_have_account_text(self):
        return self.page.get_by_text("Already have an account?")

    # ── Toast / Validation ─────────────────────────────────────────────────
    @property
    def error_toast(self):
        return self.page.locator(".Toastify__toast--error")

    @property
    def validation_errors(self):
        return self.page.locator(".ui.label.pointing")
