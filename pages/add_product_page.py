"""
AddProductPage – Page Object for /add-product
"""
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from locators.add_product_locators import AddProductLocators


class AddProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.loc = AddProductLocators(page)

    # ── Navigation ─────────────────────────────────────────────────────────
    def goto(self):
        self.navigate("add-product")

    # ── Actions ────────────────────────────────────────────────────────────
    def fill_title(self, title: str):
        self.loc.title_input.fill(title)

    def select_category(self, category: str):
        """Open the multi-select dropdown and click a category option."""
        self.loc.categories_dropdown.click()
        self.page.get_by_role("option", name=category).click()
        # Click outside to close dropdown
        self.page.keyboard.press("Escape")

    def fill_description(self, description: str):
        self.loc.description_textarea.fill(description)

    def fill_purchase_price(self, price: str):
        self.loc.purchase_price_input.fill(price)

    def fill_rent_price(self, price: str):
        self.loc.rent_price_input.fill(price)

    def select_rent_duration(self, duration: str):
        """Open the single-select dropdown and pick a duration (Daily, Hourly, etc.)."""
        self.loc.rent_duration_dropdown.click()
        self.page.get_by_role("option", name=duration).click()

    def click_add_product(self):
        self.loc.add_product_button.click()

    def add_product(
        self,
        title: str,
        categories: list,
        description: str,
        purchase_price: str,
        rent_price: str,
        rent_duration: str,
    ):
        """Fill in the entire Add Product form and submit."""
        self.fill_title(title)
        for cat in categories:
            self.select_category(cat)
        self.fill_description(description)
        self.fill_purchase_price(purchase_price)
        self.fill_rent_price(rent_price)
        self.select_rent_duration(rent_duration)
        self.click_add_product()

    # ── Assertions ─────────────────────────────────────────────────────────
    def assert_on_add_product_page(self):
        expect(self.loc.heading).to_be_visible()
        assert "/add-product" in self.page.url

    def assert_success_toast(self):
        expect(self.loc.success_toast).to_be_visible(timeout=5000)

    def assert_error_toast(self):
        expect(self.loc.error_toast).to_be_visible(timeout=5000)

    def assert_validation_errors(self):
        expect(self.loc.validation_errors.first).to_be_visible(timeout=5000)

    def assert_redirected_to_my_products(self):
        self.page.wait_for_url("**/my-products", timeout=5000)
        assert "/my-products" in self.page.url
