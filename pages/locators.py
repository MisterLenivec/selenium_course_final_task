from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".pull-right a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD_ONE = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_TWO = (By.ID, "id_registration-password2")
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alertinner > strong")
    BASKET_SUCCESS = (By.CSS_SELECTOR, "div.alertinner")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info > .alertinner > p > strong")


class BasketPageLocators:
    BASKET_PRODUCTS_FROM = (By.ID, "basket_formset")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")
