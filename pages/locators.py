from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
    
class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_TO_BUSKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_TO_BUSKET_ALERT = (By.CSS_SELECTOR, "div.alert:nth-of-type(1) .alertinner")
    BASKET_VALUE = (By.CSS_SELECTOR, ".alert-info .alertinner")
