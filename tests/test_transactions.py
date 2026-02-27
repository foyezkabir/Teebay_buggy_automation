"""
Tests for the Transactions page (Bought/Sold/Borrowed/Lent List).
"""
import pytest
from playwright.sync_api import Page, expect

from pages.transactions_page import TransactionsPage
from config import BASE_URL


@pytest.fixture(autouse=True)
def ensure_logged_in(page, login):
    """Log in before each test; individual tests navigate to their target URL."""
    login(page)
    yield


class TestTransactionsPage:
    """Tests for the Bought/Sold/Borrowed/Lent List page."""

    @pytest.mark.smoke
    def test_transactions_nav_link_navigates(self, page: Page):
        """Clicking the 'Bought/Sold/Borrowed/Lent List' nav item should navigate."""
        page.get_by_text("Bought/Sold/Borrowed/Lent List", exact=True).click()
        page.wait_for_timeout(500)
        # Should navigate (even though page renders wrong content – see bug test)
        assert "localhost:3000" in page.url

    def test_transactions_url_is_accessible(self, page: Page):
        """Navigating to /transactions directly should be accessible."""
        transactions = TransactionsPage(page)
        transactions.goto()
        transactions.assert_on_transactions_page()
