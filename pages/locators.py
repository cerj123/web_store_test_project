from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")
'''    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
'''    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
    
class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_TO_BUSKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_TO_BUSKET_ALERT = (By.CSS_SELECTOR, "div.alert:nth-of-type(1) .alertinner")
    BASKET_VALUE = (By.CSS_SELECTOR, ".alert-info .alertinner")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-of-type(1) .alertinner")

class BasketPageLocators():
    PRODUCTS_LIST = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
