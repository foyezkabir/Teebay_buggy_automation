"""
Tests for the Registration feature.
"""
import pytest
from playwright.sync_api import Page, expect

from pages.register_page import RegisterPage
from config import BASE_URL

NEW_USER = {
    "first_name": "Jane",
    "last_name": "Doe",
    "address": "456 New Street, Springfield, 12345",
    "email": "janedoe@example.com",
    "phone_number": "+11234567890",
    "password": "SecurePass123",
    "confirm_password": "SecurePass123",
}


@pytest.fixture(autouse=True)
def go_to_register(page: Page):
    reg_page = RegisterPage(page)
    reg_page.goto()
    yield


class TestRegistrationHappyPath:
    """Positive tests - happy path."""

    @pytest.mark.smoke
    def test_registration_page_renders_correctly(self, page: Page):
        """Assert all form elements are visible."""
        reg = RegisterPage(page)
        expect(reg.loc.heading).to_be_visible()
        expect(reg.loc.first_name_input).to_be_visible()
        expect(reg.loc.last_name_input).to_be_visible()
        expect(reg.loc.address_input).to_be_visible()
        expect(reg.loc.email_input).to_be_visible()
        expect(reg.loc.phone_number_input).to_be_visible()
        expect(reg.loc.password_input).to_be_visible()
        expect(reg.loc.confirm_password_input).to_be_visible()
        expect(reg.loc.register_button).to_be_visible()

    def test_registration_form_submits_with_valid_data(self, page: Page):
        """
        Submitting a fully filled + valid registration form should attempt
        to create the user. The backend always returns a server-error toast
        (known bug - backend not implemented), but the form should submit
        without frontend validation errors.
        """
        reg = RegisterPage(page)
        reg.fill_form(**NEW_USER)
        reg.click_register()

        # The happy-path expectation: no frontend validation errors visible
        expect(reg.loc.validation_errors).to_have_count(0, timeout=3000)
        
        # Backend returns error (known bug) – assert the toast appears
        reg.assert_error_toast_visible()

    def test_sign_in_link_navigates_to_login(self, page: Page):
        """Clicking 'Sign In' should navigate to /signin."""
        reg = RegisterPage(page)
        reg.click_sign_in_link()
        page.wait_for_url("**/signin")
        assert "/signin" in page.url
