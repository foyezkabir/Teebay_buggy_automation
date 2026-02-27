"""
TransactionsPage – Page Object for /transactions (Bought/Sold/Borrowed/Lent List)

NOTE: The /transactions route actually re-renders the My Products page (bug).
      There is no dedicated transactions view rendered at that URL.
"""
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class TransactionsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def goto(self):
        self.navigate("transactions")

    def assert_on_transactions_page(self):
        # URL should include /transactions
        assert "/transactions" in self.page.url

    def assert_heading_visible(self, expected_heading: str):
        expect(self.page.get_by_role("heading", name=expected_heading)).to_be_visible()

    def assert_my_products_page_rendered_instead(self):
        """Assert that the transactions nav item renders the My Products view (known bug)."""
        expect(self.page.get_by_role("button", name="Add Product")).to_be_visible()
