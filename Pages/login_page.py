from pip._internal.utils import logging

from Pages.base_page import BasePage
from Locators.login_page_locators import LoginPageLocators
from Locators.products_page_locators import ProductsPageLocators
from TestData.test_data import TestData


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.navigate_to(TestData.BASE_URL)

    def login(self, account):
        self.enter_text(LoginPageLocators.INPUT_USERNAME, account.username)
        self.enter_text(LoginPageLocators.INPUT_PASSWORD, account.password)
        self.click(LoginPageLocators.BUTTON_LOGIN)

    def get_error_text(self):
        return self.get_text(LoginPageLocators.TEXT_ERROR)

    def click_img_erro(self, index):
        self.click(ProductsPageLocators.CLICK_IMG_ERROR(index))

