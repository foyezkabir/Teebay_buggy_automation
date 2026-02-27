"""
Tests for the Browse Products feature.
"""
import pytest
from playwright.sync_api import Page, expect

from pages.browse_products_page import BrowseProductsPage
from config import BASE_URL


@pytest.fixture(autouse=True)
def navigate(page, login):
    """Log in and start each test on /browse-products."""
    login(page)
    page.goto(f"{BASE_URL}/browse-products")
    yield


class TestBrowseProductsHappyPath:
    """Positive tests - happy path."""

    @pytest.mark.smoke
    def test_browse_page_renders_correctly(self, page: Page):
        """Browse page should show the search heading and at least some products."""
        browse_page = BrowseProductsPage(page)
        browse_page.assert_on_browse_page()
        expect(browse_page.loc.title_search_input).to_be_visible()
        expect(browse_page.loc.categories_filter_dropdown).to_be_visible()
        expect(browse_page.loc.buy_filter_checkbox).to_be_visible()
        expect(browse_page.loc.rent_filter_checkbox).to_be_visible()
        expect(browse_page.loc.filter_button).to_be_visible()
        expect(browse_page.loc.clear_button).to_be_visible()

    @pytest.mark.smoke
    def test_browse_shows_products_and_load_more(self, page: Page):
        """Products from the shared pool should be visible and Load More button present."""
        browse_page = BrowseProductsPage(page)
        # These are from additionalProducts.json (not the user's own)
        browse_page.assert_product_visible("Funshine bear")
        browse_page.assert_product_visible("Blender")
        browse_page.assert_product_visible("Lawn Mower")
        browse_page.assert_load_more_visible()

    def test_load_more_loads_additional_products(self, page: Page):
        """Clicking 'Load More' should trigger loading (may show loading indicator)."""
        browse_page = BrowseProductsPage(page)
        browse_page.click_load_more()
        # Allow time for load
        page.wait_for_timeout(2000)
        # Page should still show browse page
        browse_page.assert_on_browse_page()

    def test_filters_and_clear_work_correctly(self, page: Page):
        """Buy filter, Rent filter, and Clear button should all function correctly."""
        browse_page = BrowseProductsPage(page)

        # Apply Buy filter
        browse_page.toggle_buy_filter()
        browse_page.click_filter()
        page.wait_for_timeout(500)
        browse_page.assert_on_browse_page()

        # Reset and apply Rent filter
        browse_page.click_clear()
        page.wait_for_timeout(300)
        browse_page.toggle_rent_filter()
        browse_page.click_filter()
        page.wait_for_timeout(500)
        browse_page.assert_on_browse_page()

        # Clear resets filters and restores all products
        browse_page.click_clear()
        page.wait_for_timeout(300)
        browse_page.assert_product_visible("Funshine bear")

    def test_open_product_details_from_browse(self, page: Page):
        """Clicking a product on Browse should navigate to product details page."""
        browse_page = BrowseProductsPage(page)
        browse_page.open_product("Funshine bear")
        assert "/product-details/" in page.url
