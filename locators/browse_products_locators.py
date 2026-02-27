"""
Locators for the Browse Products page.

URL: /browse-products
"""
from playwright.sync_api import Page


class BrowseProductsLocators:
    def __init__(self, page: Page):
        self.page = page

    # ── Heading ────────────────────────────────────────────────────────────
    @property
    def heading(self):
        return self.page.get_by_role("heading", name="SEARCH")

    # ── Search filters ─────────────────────────────────────────────────────
    @property
    def title_search_input(self):
        return self.page.locator('input[name="title"]').or_(
            self.page.get_by_role("textbox").first
        )

    @property
    def categories_filter_dropdown(self):
        """Single-select dropdown for category filter."""
        return self.page.get_by_role("listbox").first

    def category_filter_option(self, category_name: str):
        return self.page.get_by_role("option", name=category_name)

    @property
    def buy_filter_checkbox(self):
        return self.page.get_by_role("checkbox").nth(0)

    @property
    def rent_filter_checkbox(self):
        return self.page.get_by_role("checkbox").nth(1)

    @property
    def filter_button(self):
        return self.page.get_by_role("button", name="Filter")

    @property
    def clear_button(self):
        return self.page.get_by_role("button", name="Clear")

    @property
    def load_more_button(self):
        return self.page.get_by_role("button", name="Load More")

    # ── Product list ──────────────────────────────────────────────────────
    def product_title(self, title: str):
        """Locate a product card by its title text."""
        return self.page.get_by_text(title, exact=True).first

    @property
    def product_list(self):
        """All product title texts on the page."""
        return self.page.get_by_text("Categories:").all_text_contents

    # ── Filter labels ──────────────────────────────────────────────────────
    @property
    def buy_filter_label(self):
        return self.page.get_by_text("Buy Filters", exact=True)

    @property
    def rent_filter_label(self):
        return self.page.get_by_text("Rent Filters", exact=True)
