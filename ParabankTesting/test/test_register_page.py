import time
import unittest

from ParabankTesting.infra.browser_wrapper import BrowserWrapper
from ParabankTesting.infra.config_provider import ConfigProvider
from ParabankTesting.logic.home_page import HomePage
from ParabankTesting.logic.register_page import RegisterPage
from ParabankTesting.infra.utils import Utils
from ParabankTesting.logic.successfully_register_page import SuccessfullyRegisterPage
from ParabankTesting.logic.utils import Field, generate_random_value


class TestRegisterPage(unittest.TestCase):

    # Before all - Called automatically
    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.browser.close_browser()

    def test_login_successful(self):
        # Arrange
        self.home_page.click_register_button()
        infra_utils = Utils()

        register_page = RegisterPage(self.driver)

        # Act
        register_page.fill_first_name_input(generate_random_value(Field.FIRST_NAME))
        register_page.fill_last_name_input(generate_random_value(Field.LAST_NAME))
        register_page.fill_address_input(generate_random_value(Field.ADDRESS))
        register_page.fill_city_input(generate_random_value(Field.CITY))
        register_page.fill_state_input(generate_random_value(Field.STATE))
        register_page.fill_zip_code_input(generate_random_value(Field.ZIP_CODE))
        register_page.fill_phone_input(infra_utils.generate_random_string(10))
        register_page.fill_ssn_input(generate_random_value(Field.SSN))
        register_page.fill_username_input((infra_utils.generate_random_string(8)))
        generated_password = Utils.generate_random_string(10)
        register_page.fill_password_input(generated_password)
        register_page.fill_confirm_input(generated_password)
        time.sleep(1)

        register_page.click_on_register_button()
        time.sleep(2)

        # Assert
        success = SuccessfullyRegisterPage(self.driver)
        self.assertTrue(success.success_text_displayed())