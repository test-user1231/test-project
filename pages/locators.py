from selenium.webdriver.common.by import By


# Файл с локаторами, один класс - одна страница
class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BTN = (By.CSS_SELECTOR, "div >span >a.btn")


# наследую от базового чтобы мог использовать локаторы из него
class LoginPageLocators(BasePageLocators):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(BasePageLocators):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "div >.add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, "div.product_main >h1")
    PRICE = (By.CSS_SELECTOR, "div.product_main >p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div >div:nth-Child(1) >div.alertinner")


class BasketPageLocators(BasePageLocators):
    EMPTY_BASKET = (By.CSS_SELECTOR, "div.content >div >p")
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "div >h2.col-sm-6")
