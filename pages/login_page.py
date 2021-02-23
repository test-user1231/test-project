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

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        email_field.send_keys(email)

        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD)
        password_field.send_keys(password)

        password_field_repeat = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT_FIELD)
        password_field_repeat.send_keys(password)
        btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        btn.click()

