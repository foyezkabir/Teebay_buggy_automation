"""
ProductDetailsPage – Page Object for /product-details/:productId
"""
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from locators.product_details_locators import ProductDetailsLocators


class ProductDetailsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.loc = ProductDetailsLocators(page)

    # ── Navigation ─────────────────────────────────────────────────────────
    def goto(self, product_id: int):
        self.navigate(f"product-details/{product_id}")

    # ── Buy actions ────────────────────────────────────────────────────────
    def click_buy(self):
        self.loc.buy_button.click()

    def confirm_buy(self):
        self.click_buy()
        expect(self.loc.buy_confirmation_text).to_be_visible(timeout=3000)
        self.loc.buy_confirm_button.click()

    def cancel_buy(self):
        # Modal must already be open before calling this method
        expect(self.loc.buy_confirmation_text).to_be_visible(timeout=3000)
        self.loc.buy_cancel_button.click()

    # ── Rent actions ───────────────────────────────────────────────────────
    def click_rent(self):
        self.loc.rent_button.click()

    def fill_rent_dates(self, start_date: str, end_date: str):
        """Fill rent dates; expects modal to be open."""
        self.loc.rent_start_date_input.fill(start_date)
        self.loc.rent_end_date_input.fill(end_date)

    def confirm_rent(self, start_date: str, end_date: str):
        self.click_rent()
        self.fill_rent_dates(start_date, end_date)
        self.loc.book_rent_button.click()

    def cancel_rent(self):
        # Modal must already be open before calling this method
        self.loc.rent_cancel_button.click()

    # ── Assertions ─────────────────────────────────────────────────────────
    def assert_on_product_details_page(self):
        expect(self.loc.heading).to_be_visible()
        assert "/product-details/" in self.page.url

    def assert_buy_button_visible(self):
        expect(self.loc.buy_button).to_be_visible(timeout=3000)

    def assert_buy_button_not_visible(self):
        expect(self.loc.buy_button).to_be_hidden(timeout=3000)

    def assert_rent_button_visible(self):
        expect(self.loc.rent_button).to_be_visible(timeout=3000)

    def assert_rent_button_not_visible(self):
        expect(self.loc.rent_button).to_be_hidden(timeout=3000)

    def assert_status_available(self):
        expect(self.loc.status_available).to_be_visible(timeout=3000)

    def assert_status_sold(self):
        expect(self.loc.status_sold).to_be_visible(timeout=3000)

    def assert_view_count_incremented(self, previous_count: int):
        """Asserts the views counter shows a value greater than previous_count."""
        views_text = self.page.get_by_text("Views:").text_content()
        current_count = int("".join(filter(str.isdigit, views_text.split(":")[1])))
        assert current_count > previous_count, (
            f"Expected views > {previous_count}, got {current_count}"
        )

    def get_view_count(self) -> int:
        views_el = self.page.get_by_text("Views:").first
        views_raw = views_el.text_content()
        return int("".join(filter(str.isdigit, views_raw)))

    def assert_rent_confirmation_modal_visible(self):
        expect(self.loc.rent_start_date_input).to_be_visible(timeout=3000)

    def assert_buy_confirmation_modal_visible(self):
        expect(self.loc.buy_confirmation_text).to_be_visible(timeout=3000)
