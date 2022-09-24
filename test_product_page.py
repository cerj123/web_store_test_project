from .pages.product_page import ProductPage
import time
import pytest


#product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#promo_links = [f"{product_link}/?promo=offer{offer_number}" for offer_number in range(10)]

@pytest.mark.parametrize('offer_number', [0, 1, 3, 4, 5, 6, pytest.param("7", marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, offer_number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    #browser.delete_all_cookies()
    page = ProductPage(browser, link)
    page.open()
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding_product_to_basket(product_name)
    page.check_value_of_basket(product_price)
