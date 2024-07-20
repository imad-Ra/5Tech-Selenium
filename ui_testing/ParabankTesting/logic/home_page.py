from selenium.webdriver.common.by import By
from ui_testing.ParabankTesting.logic.base_page_app import BasePageApp
from selenium import common as c


class HomePage(BasePageApp):
    FORGOT_LOGIN_INFO = '//a[text() = "Forgot login info?"]'
    REGISTER_BUTTON = '//a[text() = "Register"]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._forgot_login_info_link = self._driver.find_element(By.XPATH, self.FORGOT_LOGIN_INFO)
            self._register_button = self._driver.find_element(By.XPATH, self.REGISTER_BUTTON)
        except c.NoSuchElementException as e:
            print("NoSuchElementException", e)

    def click_forgot_login_info(self):
        self._forgot_login_info_link.click()

    def click_register_button(self):
        self._register_button.click()