from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import BasketPageLocators

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    # Создание экземпляра класса страницы
    page = MainPage(browser, link)
    # Открытие страницы
    page.open()
    # Переход на логин
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_elems_on_register_page(browser):
    another_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, another_link)
    page.open()
    page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_cart()
    page.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET)
    page.is_element_present(*BasketPageLocators.EMPTY_BASKET)


