"""
Tests for the Edit Product feature.
"""
import pytest
from playwright.sync_api import Page, expect

from pages.edit_product_page import EditProductPage
from pages.my_products_page import MyProductsPage
from config import BASE_URL

# Product ID 1 = Cricket kit (first pre-loaded user product)
CRICKET_KIT_ID = 1


@pytest.fixture(autouse=True)
def ensure_logged_in(page, login):
    """Log in before each test; individual tests navigate to their target URL."""
    login(page)
    yield


class TestEditProductHappyPath:
    """Positive tests – happy path."""

    @pytest.mark.smoke
    def test_edit_product_page_renders_with_prefilled_data(self, page: Page):
        """Edit page should pre-fill all fields with existing product data."""
        edit_page = EditProductPage(page)
        edit_page.goto(CRICKET_KIT_ID)
        edit_page.assert_on_edit_page()
        edit_page.assert_title_value("Cricket kit")
        edit_page.assert_purchase_price_value("500")
        edit_page.assert_rent_price_value("100")

    @pytest.mark.smoke
    def test_edit_product_updates_all_fields(self, page: Page):
        """User can interact with all fields on the edit form and submit without errors."""
        edit_page = EditProductPage(page)
        edit_page.goto(CRICKET_KIT_ID)

        # Interact with every editable field
        edit_page.update_title("Updated Cricket Kit")
        edit_page.update_description("Updated description text for testing.")
        edit_page.update_purchase_price("750")
        edit_page.update_rent_price("150")
        edit_page.update_rent_duration("Weekly")

        # All fields should reflect the typed values in the DOM
        edit_page.assert_title_value("Updated Cricket Kit")
        edit_page.assert_purchase_price_value("750")
        edit_page.assert_rent_price_value("150")
        expect(edit_page.loc.description_textarea).to_have_value(
            "Updated description text for testing."
        )

        # Clicking save should not produce an error toast
        edit_page.click_save()
        page.wait_for_timeout(500)
        expect(edit_page.loc.error_toast).to_be_hidden()
