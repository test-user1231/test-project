from selenium.webdriver.common.by import By


# Файл с локаторами, один класс - одна страница
class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BTN = (By.CSS_SELECTOR, "div >span >a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


# наследую от базового чтобы мог использовать локаторы из него
class LoginPageLocators(BasePageLocators):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_REPEAT_FIELD = (By.CSS_SELECTOR, "E,id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR, "form#register_form >button")


class ProductPageLocators(BasePageLocators):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "div >.add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, "div.product_main >h1")
    PRICE = (By.CSS_SELECTOR, "div.product_main >p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div >div:nth-Child(1) >div.alertinner")


class BasketPageLocators(BasePageLocators):
    EMPTY_BASKET = (By.CSS_SELECTOR, "div.content >div >p")
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "div >h2.col-sm-6")
