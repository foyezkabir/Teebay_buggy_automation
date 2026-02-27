"""
Tests for the Account Settings feature.
"""
import pytest
from playwright.sync_api import Page, expect

from pages.account_settings_page import AccountSettingsPage
from config import BASE_URL


@pytest.fixture(autouse=True)
def navigate(page, login):
    """Log in and start each test on /account-settings."""
    login(page)
    page.goto(f"{BASE_URL}/account-settings")
    yield


class TestAccountSettingsHappyPath:
    """Positive tests, happy path."""

    @pytest.mark.smoke
    def test_account_settings_page_renders_with_prefilled_data(self, page: Page):
        """Account Settings page should render with pre-filled user data."""
        settings = AccountSettingsPage(page)
        settings.assert_on_account_settings_page()
        settings.assert_first_name_value("Test")
        settings.assert_last_name_value("User")
        settings.assert_email_value("testuser@teebay.com")
        expect(settings.loc.update_button).to_be_visible()

    @pytest.mark.smoke
    def test_update_all_fields_successfully(self, page: Page):
        """Updating all fields at once and clicking Update should show success toast and persist values."""
        settings = AccountSettingsPage(page)
        settings.update_account(
            first_name="Updated",
            last_name="UpdatedUser",
            address="999 New Address, City, 12345",
            email="updated@example.com",
            phone_number="9876543210",
        )
        settings.assert_success_toast()
        settings.assert_first_name_value("Updated")
        settings.assert_last_name_value("UpdatedUser")
        settings.assert_email_value("updated@example.com")

    def test_all_labels_are_visible(self, page: Page):
        """All field labels should be visible."""
        settings = AccountSettingsPage(page)
        expect(settings.loc.first_name_label).to_be_visible()
        expect(settings.loc.last_name_label).to_be_visible()
        expect(settings.loc.address_label).to_be_visible()
        expect(settings.loc.email_label).to_be_visible()
        expect(settings.loc.phone_number_label).to_be_visible()
