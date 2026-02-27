"""
Tests for the Login feature.
"""
import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from config import BASE_URL, TEST_EMAIL, TEST_PASSWORD


@pytest.fixture(autouse=True)
def go_to_login(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    yield


class TestLoginHappyPath:
    """Positive tests – happy path."""

    @pytest.mark.smoke
    def test_login_page_renders_correctly(self, page: Page):
        """Assert all elements are visible on the login page."""
        login_page = LoginPage(page)
        login_page.assert_on_login_page()
        expect(login_page.loc.email_label).to_be_visible()
        expect(login_page.loc.password_label).to_be_visible()
        expect(login_page.loc.sign_in_button).to_be_visible()
        expect(login_page.loc.sign_up_link).to_be_visible()
        expect(login_page.loc.no_account_text).to_be_visible()

    @pytest.mark.smoke
    def test_successful_login_redirects_to_my_products(self, page: Page):
        """A valid credential login should redirect to /my-products."""
        login_page = LoginPage(page)
        login_page.login_and_wait(TEST_EMAIL, TEST_PASSWORD)
        assert "/my-products" in page.url

    def test_login_sign_up_link_navigates_to_register(self, page: Page):
        """Clicking 'Sign Up' should navigate to the /register page."""
        login_page = LoginPage(page)
        login_page.click_sign_up_link()
        page.wait_for_url("**/register")
        assert "/register" in page.url
