"""
BrowseProductsPage – Page Object for /browse-products
"""
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from locators.browse_products_locators import BrowseProductsLocators


class BrowseProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.loc = BrowseProductsLocators(page)

    # ── Navigation ─────────────────────────────────────────────────────────
    def goto(self):
        self.navigate("browse-products")

    # ── Actions ────────────────────────────────────────────────────────────
    def search_by_title(self, keyword: str):
        self.loc.title_search_input.fill(keyword)

    def filter_by_category(self, category: str):
        self.loc.categories_filter_dropdown.click()
        self.page.get_by_role("option", name=category).click()

    def toggle_buy_filter(self):
        # The checkbox input is hidden; click its label instead
        self.page.get_by_text("Buy Filters", exact=True).click()

    def toggle_rent_filter(self):
        # The checkbox input is hidden; click its label instead
        self.page.get_by_text("Rent Filters", exact=True).click()

    def click_filter(self):
        self.loc.filter_button.click()

    def click_clear(self):
        self.loc.clear_button.click()

    def click_load_more(self):
        self.loc.load_more_button.click()

    def open_product(self, title: str):
        """Click a product title to open its details page."""
        self.page.get_by_text(title, exact=True).first.click()
        self.page.wait_for_url("**/product-details/**")

    # ── Assertions ─────────────────────────────────────────────────────────
    def assert_on_browse_page(self):
        expect(self.loc.heading).to_be_visible()
        assert "/browse-products" in self.page.url

    def assert_product_visible(self, title: str):
        expect(self.page.get_by_text(title, exact=True).first).to_be_visible(timeout=5000)

    def assert_product_not_visible(self, title: str):
        expect(self.page.get_by_text(title, exact=True).first).to_be_hidden(timeout=5000)

    def assert_load_more_visible(self):
        expect(self.loc.load_more_button).to_be_visible()

    def get_visible_product_titles(self) -> list:
        """Return a list of visible product title text on the page."""
        return self.page.locator(".product-card h2, .product-card h3").all_text_contents()
