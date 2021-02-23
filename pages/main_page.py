from .base_page import BasePage


# Наследуемся от базовой страницы в которой есть общие методы для использования на страницах этого класса
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

