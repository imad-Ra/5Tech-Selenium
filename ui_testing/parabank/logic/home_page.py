from selenium.webdriver.common.by import By
from ui_testing.parabank.infra.base_page import BasePage


class HomePage(BasePage):
    REGISTER_BUTTON = '//a[@href="register.htm"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._register_button = self._driver.find_element(By.XPATH, self.REGISTER_BUTTON)

    def click_on_register_button(self):
        self._register_button.click()


