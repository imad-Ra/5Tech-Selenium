from selenium.webdriver.common.by import By

from parabank.infra.base_page import BasePage


class SuccessRegisterPage(BasePage):
    SUCCESS_REGISTER_TEXT = '//h1[@class="title"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._success_register_text = self._driver.find_element(By.XPATH, self.SUCCESS_REGISTER_TEXT)

    def success_register_text_shown(self):
        self._success_register_text.is_display()
