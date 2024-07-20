from selenium.webdriver.common.by import By
from selenium import common as c
from ui_testing.ParabankTesting.logic.base_page_app import BasePageApp


class SuccessfullyRegisterPage(BasePageApp):
    REGISTER_SUCCESS_TEXT = '//p[text() = "Your account was created successfully. You are now logged in."]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._register_success = self._driver.find_element(By.XPATH, self.REGISTER_SUCCESS_TEXT)
        except c.NoSuchElementException as e:
            print("NoSuchElementException", e)

    def success_text_displayed(self) -> bool:
        return self._register_success.is_displayed()

    def get_success_text(self) -> str:
        return self._register_success.text
