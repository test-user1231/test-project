import pytest
import time
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators, BasketPageLocators


# @pytest.mark.parametrize('link', ["?promo=offer0",
#                                   "?promo=offer1",
#                                   "?promo=offer2",
#                                   "?promo=offer3",
#                                   "?promo=offer4",
#                                   "?promo=offer5",
#                                   "?promo=offer6",
#                                   pytest.param("?promo=offer7", marks=pytest.mark.xfail),
#                                   "?promo=offer8",
#                                   "?promo=offer9"])
# def test_guest_can_add_product_to_basket_with_params(browser, link):
#     original_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{0}".format(link)
#     page = ProductPage(browser, original_link)
#     page.open()
#     book_name, price = page.add_to_cart()
#     page.solve_quiz_and_get_code()
#     page.check_book_name(book_name)
#     page.check_price(price)

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart()
    page.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET)
    page.is_element_present(*BasketPageLocators.EMPTY_BASKET)


class TestUserAddToBasketFromProductPage:
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "zaxscdvfbgnhmj,k"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.add_to_cart()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
