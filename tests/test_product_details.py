"""
Tests for the Product Details page – views, buy, rent.
"""
import pytest
from playwright.sync_api import Page, expect

from pages.product_details_page import ProductDetailsPage
from pages.browse_products_page import BrowseProductsPage
from config import BASE_URL

# Available product IDs (from additionalProducts.json, not owned by testuser)
FUNSHINE_BEAR_ID = 1241      # Available, no rent history
BLENDER_ID = 2432            # Available, has rent history
LAWN_MOWER_ID = 678         # Available, multiple rent entries

# Sold products
LAST_OF_US_ID = 2134        # SOLD
IKEA_COUCH_ID = 5345        # SOLD


@pytest.fixture(autouse=True)
def ensure_logged_in(page, login):
    """Log in before each test; individual tests navigate to their target URL."""
    login(page)
    yield


class TestProductDetailsHappyPath:
    """Positive tests – happy path."""

    @pytest.mark.smoke
    def test_product_details_page_renders_correctly(self, page: Page):
        """Product details page should show all key information."""
        details = ProductDetailsPage(page)
        details.goto(FUNSHINE_BEAR_ID)
        details.assert_on_product_details_page()
        expect(page.get_by_text("Funshine bear")).to_be_visible()
        expect(details.loc.views_text).to_be_visible()
        expect(details.loc.categories_text if hasattr(details.loc, 'categories_text') else page.get_by_text("Toys")).to_be_visible()
        expect(details.loc.rent_history_label).to_be_visible()

    @pytest.mark.smoke
    def test_view_count_increments_on_visit(self, page: Page):
        """
        Visiting a product details page should increment the view count by 1.
        """
        details = ProductDetailsPage(page)
        # First visit – get initial count
        details.goto(FUNSHINE_BEAR_ID)
        initial_count = details.get_view_count()
        # Go back to browse
        page.goto(f"{BASE_URL}/browse-products")
        # Second visit – count should have incremented
        details.goto(FUNSHINE_BEAR_ID)
        new_count = details.get_view_count()
        assert new_count > initial_count, (
            f"Expected view count > {initial_count} after second visit, got {new_count}"
        )

    @pytest.mark.smoke
    def test_available_product_shows_buy_and_rent_buttons(self, page: Page):
        """An available product (not sold, not user's own) should show both buttons."""
        details = ProductDetailsPage(page)
        details.goto(FUNSHINE_BEAR_ID)
        details.assert_status_available()
        details.assert_buy_button_visible()
        details.assert_rent_button_visible()

    def test_sold_product_does_not_show_buy_button(self, page: Page):
        """
        A product with is_purchased=True (SOLD) should NOT show a Buy button.
        BUG DETECTION: The app shows status 'SOLD' but the buy/rent buttons
        may still be visible (depends on the ProductDetails component logic).
        """
        details = ProductDetailsPage(page)
        details.goto(LAST_OF_US_ID)
        details.assert_status_sold()
        # Assert buy button is NOT visible for a SOLD item
        details.assert_buy_button_not_visible()

    @pytest.mark.smoke
    def test_buy_flow_modal_cancel_then_confirm(self, page: Page):
        """Buy modal appears, cancel dismisses it, then confirm completes the purchase."""
        details = ProductDetailsPage(page)
        details.goto(FUNSHINE_BEAR_ID)

        # Step 1: open modal and cancel button should still be visible
        details.click_buy()
        details.assert_buy_confirmation_modal_visible()
        details.cancel_buy()
        expect(details.loc.buy_confirmation_text).to_be_hidden(timeout=3000)
        details.assert_buy_button_visible()

        # Step 2: open modal again and confirm product should become SOLD
        details.click_buy()
        details.confirm_buy()
        page.wait_for_timeout(500)
        details.goto(FUNSHINE_BEAR_ID)
        details.assert_status_sold()

    @pytest.mark.smoke
    def test_rent_flow_modal_cancel_then_confirm(self, page: Page):
        """Rent modal appears with correct buttons, cancel dismisses it, then confirm books the rent."""
        details = ProductDetailsPage(page)
        details.goto(FUNSHINE_BEAR_ID)

        # Step 1: open modal and verify buttons, then cancel
        details.click_rent()
        details.assert_rent_confirmation_modal_visible()
        expect(details.loc.book_rent_button).to_be_visible()
        expect(details.loc.rent_cancel_button).to_be_visible()
        details.cancel_rent()
        expect(details.loc.rent_start_date_input).to_be_hidden(timeout=3000)

        # Step 2: open modal again and confirm with valid dates
        details.click_rent()
        details.confirm_rent("2026-03-01", "2026-03-10")
        page.wait_for_timeout(500)

        # After booking, rent history should show the booked year
        details.goto(FUNSHINE_BEAR_ID)
        expect(page.get_by_text("2026").first).to_be_visible(timeout=5000)
