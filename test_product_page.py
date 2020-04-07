from .pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('promo', [pytest.param(
    i, marks=pytest.mark.xfail(i == 7, reason='fix this bug soon')
) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/' \
        f'coders-at-work_207/?promo=offer{promo}'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_success_messages()
