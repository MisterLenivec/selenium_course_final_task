from .base_page import BasePage
from .locators import BasketPageLocators


languages = {
    "ar": "سلة التسوق فارغة",
    "ca": "La seva cistella està buida.",
    "cs": "Váš košík je prázdný.",
    "da": "Din indkøbskurv er tom.",
    "de": "Ihr Warenkorb ist leer.",
    "en": "Your basket is empty.",
    "el": "Το καλάθι σας είναι άδειο.",
    "es": "Tu carrito esta vacío.",
    "fi": "Korisi on tyhjä",
    "fr": "Votre panier est vide.",
    "it": "Il tuo carrello è vuoto.",
    "ko": "장바구니가 비었습니다.",
    "nl": "Je winkelmand is leeg",
    "pl": "Twój koszyk jest pusty.",
    "pt": "O carrinho está vazio.",
    "pt-br": "Sua cesta está vazia.",
    "ro": "Cosul tau este gol.",
    "ru": "Ваша корзина пуста",
    "sk": "Váš košík je prázdny",
    "uk": "Ваш кошик пустий.",
    "zh-cn": "Your basket is empty.",
    "en-US": "Your basket is empty.",
}


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_PRODUCTS_FROM
        ), "Products in basket is presented, but should not be"

    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_EMPTY_TEXT
        ), "Message about empty basket is not presented"

    def should_be_correct_text_message_about_empty_basket(self):
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        assert languages[language] in self.browser.find_element(
            *BasketPageLocators.BASKET_EMPTY_TEXT
        ).text, "incorrect message about empty basket"
