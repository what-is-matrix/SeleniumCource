from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, "#basket_formset .basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD1 = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form button[type="submit"]')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    REGISTER_FORM = (By.ID, "register_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    BASKET_ALERTS_INFO = (By.CSS_SELECTOR, "#messages .alert-info strong")
    BASKET_ALERTS_SUCCESS = (By.CSS_SELECTOR, "#messages .alert-success strong")
