from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_add_product_to_basket_button()

    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET
        )
        add_to_basket_btn.click()

    def should_be_correct_success_messages(self):
        self.should_be_message_about_product_added_to_basket()
        self.should_be_product_name_in_message_about_basket()
        self.should_be_message_about_product_price()
        self.cost_of_the_basket_must_match_price_of_the_goods()

    def should_be_product_url(self):
        assert "catalogue" in self.browser.current_url, \
            "Product url is not presented"

    def should_be_add_product_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET
        ), "Add product to basket button is not presented"

    def should_be_message_about_product_added_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_SUCCESS
        ), "Message about product added to basket is not presented"

    def get_product_name(self, name):
        WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located(name))
        try:
            return str(self.browser.find_element(*name).text)
        except NoSuchElementException:
            return None

    def should_be_product_name_in_message_about_basket(self):
        time.sleep(1)  # It's for Firefox, if you remove it, tests will fail
        product_name = self.get_product_name(
            ProductPageLocators.PRODUCT_NAME
        )
        basket_product_name = self.get_product_name(
            ProductPageLocators.BASKET_PRODUCT_NAME
        )
        assert product_name == basket_product_name, \
            "incorrect name of product in message about product added"

    def should_be_message_about_product_price(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_PRICE
        ), "Message about product price in your basket is not presented"

    def cost_of_the_basket_must_match_price_of_the_goods(self):
        assert self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text in self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE
        ).text, "Product price not equal product price in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.BASKET_SUCCESS
        ), "Success message is presented, but should not be"

    def should_success_message_disappear(self):
        assert self.is_disappeared(
            *ProductPageLocators.BASKET_SUCCESS
        ), "Success message is not disappeared"
