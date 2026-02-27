"""
Tests for the Add Product feature.
"""
import pytest
from playwright.sync_api import Page, expect

from pages.add_product_page import AddProductPage
from pages.my_products_page import MyProductsPage
from config import BASE_URL


@pytest.fixture(autouse=True)
def navigate(page, login):
    """Log in and start each test on /add-product."""
    login(page)
    page.goto(f"{BASE_URL}/add-product")
    yield


class TestAddProductHappyPath:
    """Positive tests – happy path."""

    @pytest.mark.smoke
    def test_add_product_page_renders_correctly(self, page: Page):
        """All form fields should be visible on the Add Product page."""
        add_page = AddProductPage(page)
        add_page.assert_on_add_product_page()
        expect(add_page.loc.title_input).to_be_visible()
        expect(add_page.loc.categories_dropdown).to_be_visible()
        expect(add_page.loc.description_textarea).to_be_visible()
        expect(add_page.loc.purchase_price_input).to_be_visible()
        expect(add_page.loc.rent_price_input).to_be_visible()
        expect(add_page.loc.rent_duration_dropdown).to_be_visible()
        expect(add_page.loc.add_product_button).to_be_visible()

    @pytest.mark.smoke
    def test_add_product_successfully(self, page: Page):
        """
        Filling all required fields (including multiple categories) and submitting
        should create the product, show a success toast, and redirect to /my-products.
        """
        add_page = AddProductPage(page)
        add_page.fill_title("Test Bicycle")
        add_page.select_category("Electronics")
        add_page.select_category("Outdoor")
        add_page.fill_description("A sturdy mountain bicycle in good condition.")
        add_page.fill_purchase_price("300")
        add_page.fill_rent_price("15")
        add_page.select_rent_duration("Daily")
        add_page.click_add_product()
        add_page.assert_success_toast()
        add_page.assert_redirected_to_my_products()
        # Confirm product appears in my products list
        expect(page.get_by_text("Test Bicycle", exact=True).first).to_be_visible()

    def test_add_product_redirects_to_my_products(self, page: Page):
        """After successful add, user is redirected to /my-products."""
        add_page = AddProductPage(page)
        add_page.add_product(
            title="Redirect Test Item",
            categories=["Furniture"],
            description="Just for redirect test.",
            purchase_price="50",
            rent_price="5",
            rent_duration="Monthly",
        )
        add_page.assert_redirected_to_my_products()
