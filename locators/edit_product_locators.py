"""
Locators for the Edit Product page.

URL: /edit-product/:productId

On the Edit Product page all labels are visible (Purchase Price, Rent Price,
Frequency) unlike the Add Product page where those labels are hidden.
"""
from playwright.sync_api import Page


class EditProductLocators:
    def __init__(self, page: Page):
        self.page = page

    # ── Heading ────────────────────────────────────────────────────────────
    @property
    def heading(self):
        return self.page.get_by_role("heading", name="EDIT PRODUCT")

    # ── Form inputs ────────────────────────────────────────────────────────
    @property
    def title_input(self):
        return self.page.locator('input[name="title"]')

    @property
    def categories_dropdown(self):
        """Semantic-UI multi-select listbox for categories."""
        return self.page.get_by_role("listbox").nth(0)

    def category_option(self, category_name: str):
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
        """Semantic-UI single-select listbox for rent duration."""
        return self.page.get_by_role("listbox").nth(1)

    def rent_duration_option(self, duration: str):
        return self.page.get_by_role("option", name=duration)

    # ── Labels (only shown in edit mode) ──────────────────────────────────
    @property
    def purchase_price_label(self):
        return self.page.get_by_text("Purchase Price", exact=True)

    @property
    def rent_price_label(self):
        return self.page.get_by_text("Rent Price", exact=True)

    @property
    def frequency_label(self):
        return self.page.get_by_text("Frequency", exact=True)

    # ── Buttons ────────────────────────────────────────────────────────────
    @property
    def save_button(self):
        """The save/update button on the edit form (labeled 'Add Product' – this is a bug)."""
        return self.page.get_by_role("button", name="Add Product")

    # ── Toasts / Validation ───────────────────────────────────────────────
    @property
    def success_toast(self):
        return self.page.locator(".Toastify__toast--success")

    @property
    def error_toast(self):
        return self.page.locator(".Toastify__toast--error")

    @property
    def validation_errors(self):
        return self.page.locator(".ui.label.pointing")
