"""
Tests for the My Products feature (list, add navigation, delete).
"""
import pytest
from playwright.sync_api import Page, expect

from pages.my_products_page import MyProductsPage
from pages.add_product_page import AddProductPage
from config import BASE_URL


@pytest.fixture(autouse=True)
def navigate(page, login):
    """Log in and start each test on /my-products."""
    login(page)
    page.goto(f"{BASE_URL}/my-products")
    yield


class TestMyProductsHappyPath:
    """Positive tests – happy path."""

    @pytest.mark.smoke
    def test_my_products_page_renders_correctly(self, page: Page):
        """My Products page should show user's products and Add Product button."""
        my_products = MyProductsPage(page)
        my_products.assert_on_my_products_page()
        # Pre-loaded products should be visible
        my_products.assert_product_visible("Cricket kit")
        my_products.assert_product_visible("iPhone 13 pro max")

    def test_add_product_button_navigates_to_add_page(self, page: Page):
        """Clicking 'Add Product' should navigate to /add-product."""
        my_products = MyProductsPage(page)
        my_products.click_add_product()
        assert "/add-product" in page.url

    def test_clicking_product_title_navigates_to_edit(self, page: Page):
        """Clicking a product title should navigate to /edit-product/:id."""
        my_products = MyProductsPage(page)
        my_products.click_product_title("Cricket kit")
        assert "/edit-product/" in page.url

    @pytest.mark.smoke
    def test_delete_product_with_confirmation(self, page: Page):
        """Clicking delete and confirming 'Yes, delete' should remove the product."""
        my_products = MyProductsPage(page)
        initial_count = my_products.count_products()
        my_products.delete_product_at(0)
        page.wait_for_timeout(500)
        new_count = my_products.count_products()
        # The app renders each product card twice (duplicate display),
        # so deleting 1 unique product reduces the trash-button count by 2.
        assert new_count == initial_count - 2, (
            f"Expected product count to decrease by 2 (each product shown twice). "
            f"Before: {initial_count}, After: {new_count}"
        )

    def test_cancel_delete_keeps_product(self, page: Page):
        """Clicking delete then 'Cancel' should NOT delete the product."""
        my_products = MyProductsPage(page)
        initial_count = my_products.count_products()
        my_products.cancel_delete(0)
        page.wait_for_timeout(300)
        new_count = my_products.count_products()
        assert new_count == initial_count, (
            f"Expected same count after cancelling delete. "
            f"Before: {initial_count}, After: {new_count}"
        )

    def test_nav_browse_products_link(self, page: Page):
        """Browse Products nav link should navigate to /browse-products."""
        my_products = MyProductsPage(page)
        my_products.navigate_to_browse()
        assert "/browse-products" in page.url

    def test_nav_account_settings_link(self, page: Page):
        """Account Settings nav link should navigate to /account-settings."""
        my_products = MyProductsPage(page)
        my_products.navigate_to_account_settings()
        assert "/account-settings" in page.url

    def test_logout_redirects_to_login(self, page: Page):
        """Logout should redirect to /signin."""
        my_products = MyProductsPage(page)
        my_products.logout()
        assert "/signin" in page.url or page.url == f"{BASE_URL}/"
