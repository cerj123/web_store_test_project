from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET)
        login_link.click()

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def should_be_message_about_adding_product_to_basket(self, product_name):
        should_be_message = product_name + " has been added to your basket."
        added_to_basket_alert = self.browser.find_element(*ProductPageLocators.ADDED_TO_BUSKET_ALERT).text
        assert should_be_message == added_to_basket_alert, \
            f"expected '{should_be_message}' to be equal to '{added_to_basket_alert}'"

    def check_value_of_basket(self, product_price):
        basket_value_alert = self.browser.find_element(*ProductPageLocators.BASKET_VALUE).text
        assert basket_value_alert.find(product_price) != -1, \
            f"expected '{product_price}' to be substring of '{basket_value_alert}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not dissapeared"
