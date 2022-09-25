from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url
        
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_LIST), \
            "Products list is presented, but should not be"

    def should_be_message_about_empty_basket(self):
        empty_basket_message = "Your basket is empty."
        basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert basket_message.find(empty_basket_message) != -1, \
            f"expected '{empty_basket_message}' to be substring of '{basket_message}'"
