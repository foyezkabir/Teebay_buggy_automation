"""
Locators for the Add Product page.

URL: /add-product

Note: The Add Product form does NOT show labels for purchase_price and rent_price.
Labels are only shown on the Edit Product page (isEdit=true). So we rely on
name attributes to locate those inputs on this page.
"""
from playwright.sync_api import Page


class AddProductLocators:
    def __init__(self, page: Page):
        self.page = page

    # ── Heading ────────────────────────────────────────────────────────────
    @property
    def heading(self):
        return self.page.get_by_role("heading", name="ADD PRODUCT")

    # ── Form inputs ────────────────────────────────────────────────────────
    @property
    def title_input(self):
        return self.page.locator('input[name="title"]')

    @property
    def categories_dropdown(self):
        """Semantic-UI multi-select listbox for categories."""
        return self.page.get_by_role("listbox").nth(0)

    def category_option(self, category_name: str):
        """A visible option inside the opened categories dropdown."""
        return self.page.get_by_role("option", name=category_name)

    @property
    def description_textarea(self):
        return self.page.locator('textarea[name="description"]')

    @property
    def purchase_price_input(self):
        return self.page.locator('input[name="purchase_price"]')

    @property
    def rent_price_input(self):
        return self.page.locator('input[name="rent_price"]')

    @property
    def rent_duration_dropdown(self):
        """Semantic-UI single-select listbox for rent duration type."""
        return self.page.get_by_role("listbox").nth(1)

    def rent_duration_option(self, duration: str):
        """An option in the opened rent duration dropdown (Daily, Hourly, etc.)."""
        return self.page.get_by_role("option", name=duration)

    # ── Buttons ────────────────────────────────────────────────────────────
    @property
    def add_product_button(self):
        return self.page.get_by_role("button", name="Add Product")

    # ── Toasts ────────────────────────────────────────────────────────────
    @property
    def success_toast(self):
        return self.page.locator(".Toastify__toast--success")

    @property
    def error_toast(self):
        return self.page.locator(".Toastify__toast--error")

    @property
    def validation_errors(self):
        return self.page.locator(".ui.label.pointing")
