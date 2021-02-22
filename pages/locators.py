from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "div >.add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, "div.product_main >h1")
    PRICE = (By.CSS_SELECTOR, "div.product_main >p.price_color")

