"""
Locators for the Navigation Bar (shown after login).
"""
from playwright.sync_api import Page


class NavBarLocators:
    def __init__(self, page: Page):
        self.page = page

    @property
    def my_products_link(self):
        return self.page.get_by_text("My Products", exact=True)

    @property
    def browse_products_link(self):
        return self.page.get_by_text("Browse Products", exact=True)

    @property
    def transactions_link(self):
        return self.page.get_by_text("Bought/Sold/Borrowed/Lent List", exact=True)

    @property
    def account_settings_link(self):
        return self.page.get_by_text("Account Settings", exact=True)

    @property
    def logout_link(self):
        return self.page.get_by_text("Logout", exact=True)
