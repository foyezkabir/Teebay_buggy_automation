"""
MyProductsPage – Page Object for /my-products
"""
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from locators.my_products_locators import MyProductsLocators
from locators.navbar_locators import NavBarLocators


class MyProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.loc = MyProductsLocators(page)
        self.nav = NavBarLocators(page)

    # ── Navigation ─────────────────────────────────────────────────────────
    def goto(self):
        self.navigate("my-products")

    # ── Actions ────────────────────────────────────────────────────────────
    def click_add_product(self):
        self.loc.add_product_button.click()
        self.page.wait_for_url("**/add-product")

    def click_product_title(self, title: str):
        """Navigate to edit product by clicking on the title."""
        self.page.get_by_text(title, exact=True).first.click()
        self.page.wait_for_url("**/edit-product/**")

    def delete_product_at(self, index: int = 0):
        """Delete the product card at the given 0-based index."""
        # Trash-icon buttons are icon-only Semantic UI buttons
        self.page.locator('button:has(i.trash)').nth(index).click()
        expect(self.loc.delete_confirmation_text).to_be_visible(timeout=5000)
        self.loc.delete_confirm_button.click()

    def cancel_delete(self, index: int = 0):
        self.page.locator('button:has(i.trash)').nth(index).click()
        expect(self.loc.delete_confirmation_text).to_be_visible(timeout=5000)
        self.loc.delete_cancel_button.click()

    def navigate_to_browse(self):
        self.nav.browse_products_link.click()
        self.page.wait_for_url("**/browse-products")

    def navigate_to_account_settings(self):
        self.nav.account_settings_link.click()
        self.page.wait_for_url("**/account-settings")

    def navigate_to_transactions(self):
        self.nav.transactions_link.click()

    def logout(self):
        self.nav.logout_link.click()
        # Logout opens a confirmation modal
        self.page.get_by_role("button", name="Yes I am sure!").click()
        self.page.wait_for_url("**/signin", timeout=10000)

    # ── Assertions ─────────────────────────────────────────────────────────
    def assert_product_visible(self, title: str):
        expect(self.page.get_by_text(title, exact=True).first).to_be_visible(timeout=5000)

    def assert_product_not_visible(self, title: str):
        expect(self.page.get_by_text(title, exact=True).first).to_be_hidden(timeout=5000)

    def assert_add_product_button_visible(self):
        expect(self.loc.add_product_button).to_be_visible()

    def assert_on_my_products_page(self):
        expect(self.loc.add_product_button).to_be_visible()
        assert "/my-products" in self.page.url

    def count_products(self) -> int:
        """Return the number of delete buttons (one per product card)."""
        return self.page.locator('button:has(i.trash)').count()
