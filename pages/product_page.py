from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ProductPage(BasePage):
    def add_to_cart(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        btn.click()
        return book_name, price

    def check_book_name(self, book_name):
        cart_book_name = WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "div >div:nth-Child(1) >div.alertinner >strong"))
        )
        assert book_name == cart_book_name.text, "Book is incorrect"

    def check_price(self, price):
        cart_price = self.browser.find_element(By.CSS_SELECTOR, "div >div >div:nth-Child(2) >p >strong")
        assert price == cart_price.text, "Price is incorrect"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
