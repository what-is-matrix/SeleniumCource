from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    REGISTER_FORM = (By.ID, "register_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    BASKET_ALERTS_INFO = (By.CSS_SELECTOR, "#messages .alert-info strong")
    BASKET_ALERTS_SUCCESS = (By.CSS_SELECTOR, "#messages .alert-success strong")
