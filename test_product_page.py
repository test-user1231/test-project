import pytest
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators, BasketPageLocators


@pytest.mark.parametrize('link', ["?promo=offer0",
                                  "?promo=offer1",
                                  "?promo=offer2",
                                  "?promo=offer3",
                                  "?promo=offer4",
                                  "?promo=offer5",
                                  "?promo=offer6",
                                  pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                  "?promo=offer8",
                                  "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    original_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{0}".format(link)
    page = ProductPage(browser, original_link)
    page.open()
    book_name, price = page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.check_book_name(book_name)
    page.check_price(price)


@pytest.mark.negative
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)


@pytest.mark.negative
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)


@pytest.mark.negative
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)


@pytest.mark.smoke
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.smoke
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart()
    page.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET)
    page.is_element_present(*BasketPageLocators.EMPTY_BASKET)

