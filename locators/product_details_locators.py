"""
Locators for the Product Details page.

URL: /product-details/:productId

Key available test products:
- id 1241 (Funshine bear) – Available, can buy/rent
- id 2432 (Blender)       – Available, has rent history
- id 2134 (Last of Us)    – SOLD, no buy button
- id 5345 (Ikea couch)    – SOLD, no buy button
- id 1    (Cricket kit)   – User's own product (should NOT show buy/rent)
- id 2    (iPhone 13)     – User's own product (should NOT show buy/rent)
"""
from playwright.sync_api import Page


class ProductDetailsLocators:
    def __init__(self, page: Page):
        self.page = page

    # ── Heading ────────────────────────────────────────────────────────────
    @property
    def heading(self):
        return self.page.get_by_role("heading", name="PRODUCT DETAILS")

    # ── Product info ───────────────────────────────────────────────────────
    @property
    def product_name(self):
        return self.page.locator("h2, h3").first

    @property
    def views_text(self):
        return self.page.get_by_text("Views:", exact=False)

    @property
    def status_available(self):
        return self.page.get_by_text("Available", exact=True)

    @property
    def status_sold(self):
        return self.page.get_by_text("SOLD", exact=True)

    @property
    def rent_history_label(self):
        return self.page.get_by_text("Rent history:", exact=False)

    # ── Action buttons ─────────────────────────────────────────────────────
    @property
    def rent_button(self):
        return self.page.get_by_role("button", name="Rent", exact=True)

    @property
    def buy_button(self):
        return self.page.get_by_role("button", name="Buy")

    # ── Rent modal ─────────────────────────────────────────────────────────
    @property
    def rent_start_date_input(self):
        return self.page.get_by_placeholder("yyyy-mm-dd").nth(0)

    @property
    def rent_end_date_input(self):
        return self.page.get_by_placeholder("yyyy-mm-dd").nth(1)

    @property
    def book_rent_button(self):
        return self.page.get_by_role("button", name="Book rent")

    @property
    def rent_cancel_button(self):
        return self.page.get_by_role("button", name="Cancel")

    @property
    def rent_modal_end_date_label(self):
        """Label for end date in the rent modal – currently shows 'Last Name' (BUG)."""
        return self.page.get_by_text("Last Name", exact=True)

    @property
    def rent_modal_start_date_label(self):
        return self.page.get_by_text("Start date", exact=True)

    # ── Buy modal ──────────────────────────────────────────────────────────
    @property
    def buy_confirmation_text(self):
        return self.page.get_by_text("Are you sure you want to buy this product?")

    @property
    def buy_confirm_button(self):
        return self.page.get_by_role("button", name="Yes!")

    @property
    def buy_cancel_button(self):
        return self.page.get_by_role("button", name="Cancel")
