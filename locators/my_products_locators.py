"""
Locators for the My Products page.

URL: /my-products
"""
from playwright.sync_api import Page


class MyProductsLocators:
    def __init__(self, page: Page):
        self.page = page

    # ── Navigation / buttons ──────────────────────────────────────────────
    @property
    def add_product_button(self):
        return self.page.get_by_role("button", name="Add Product")

    # ── Product cards ─────────────────────────────────────────────────────
    @property
    def product_cards(self):
        """All product card containers."""
        return self.page.locator(".product-card, [class*='ProductCard'], [class*='Card']")

    def product_title(self, title: str):
        """Locator for a product with a specific title."""
        return self.page.get_by_text(title, exact=True).first()

    def delete_button_nth(self, index: int = 0):
        """Delete (trash-icon) button at position index across all cards."""
        return self.page.get_by_role("button").filter(has_text="").nth(index)

    @property
    def first_delete_button(self):
        """First delete button in the list (unnamed button only in My Products area)."""
        # Delete buttons are unnamed icon-only buttons. There's one per product card.
        return self.page.locator("button").filter(has_text="").nth(0)

    @property
    def delete_confirmation_text(self):
        return self.page.get_by_text("Are you sure you want to delete this product?")

    @property
    def delete_confirm_button(self):
        return self.page.get_by_role("button", name="Yes, delete")

    @property
    def delete_cancel_button(self):
        return self.page.get_by_role("button", name="Cancel")

    # ── Product info helpers ──────────────────────────────────────────────
    def price_text(self, price: str):
        return self.page.get_by_text(price)

    def category_text(self, category: str):
        return self.page.get_by_text(category)
