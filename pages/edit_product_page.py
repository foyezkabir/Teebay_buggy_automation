"""
EditProductPage – Page Object for /edit-product/:productId
"""
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from locators.edit_product_locators import EditProductLocators


class EditProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.loc = EditProductLocators(page)

    # ── Navigation ─────────────────────────────────────────────────────────
    def goto(self, product_id: int):
        self.navigate(f"edit-product/{product_id}")

    # ── Actions ────────────────────────────────────────────────────────────
    def _clear_and_type(self, locator, value: str):
        """Select all existing text then type new value via keyboard so that
        react-hook-form's internal onChange handler is triggered (fill() sets
        the DOM value but does not fire keyboard events that RHF relies on)."""
        locator.click()
        locator.press("Control+a")
        locator.press_sequentially(value, delay=30)

    def update_title(self, new_title: str):
        self._clear_and_type(self.loc.title_input, new_title)

    def update_description(self, new_description: str):
        self._clear_and_type(self.loc.description_textarea, new_description)

    def update_purchase_price(self, price: str):
        self._clear_and_type(self.loc.purchase_price_input, price)

    def update_rent_price(self, price: str):
        self._clear_and_type(self.loc.rent_price_input, price)

    def select_category(self, category: str):
        self.loc.categories_dropdown.click()
        self.page.get_by_role("option", name=category).click()
        self.page.keyboard.press("Escape")

    def update_rent_duration(self, duration: str):
        self.loc.rent_duration_dropdown.click()
        self.page.get_by_role("option", name=duration).click()

    def click_save(self):
        self.loc.save_button.click()

    def update_product(self, title: str = None, description: str = None,
                       purchase_price: str = None, rent_price: str = None,
                       rent_duration: str = None):
        """Update any subset of product fields and save."""
        if title:
            self.update_title(title)
        if description:
            self.update_description(description)
        if purchase_price:
            self.update_purchase_price(purchase_price)
        if rent_price:
            self.update_rent_price(rent_price)
        if rent_duration:
            self.update_rent_duration(rent_duration)
        self.click_save()

    # ── Assertions ─────────────────────────────────────────────────────────
    def assert_on_edit_page(self):
        expect(self.loc.heading).to_be_visible()
        assert "/edit-product/" in self.page.url

    def assert_title_value(self, expected: str):
        expect(self.loc.title_input).to_have_value(expected)

    def assert_purchase_price_value(self, expected: str):
        expect(self.loc.purchase_price_input).to_have_value(expected)

    def assert_rent_price_value(self, expected: str):
        expect(self.loc.rent_price_input).to_have_value(expected)

    def assert_validation_errors(self):
        expect(self.loc.validation_errors.first).to_be_visible(timeout=5000)
