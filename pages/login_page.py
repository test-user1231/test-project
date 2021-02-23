from .base_page import BasePage
from .locators import LoginPageLocators


# Наследуемся от базовой страницы в которой есть общие методы для использования на страницах этого класса
class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # Проверка что в урл есть подстрока
    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert 'login' in str(login_url), "Link is incorrect"

    # Проверка что есть форма логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is empty"

    # Проверка что есть форма регистрации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form not found"

