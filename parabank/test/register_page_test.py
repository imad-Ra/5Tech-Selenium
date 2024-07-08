import unittest
from parabank.infra.browser_wrapper import BrowserWrapper
from parabank.infra.config_provider import ConfigProvider
from parabank.logic.home_page import HomePage
from parabank.logic.register_page import RegisterPage
from parabank.logic.success_register_page import SuccessRegisterPage


class RegisterPageTest(unittest.TestCase):

    def setUp(self):
        try:
            self.browser = BrowserWrapper()
            self.config = ConfigProvider.load_config_json()
            if self.config is None:
                raise ValueError("Failed to load configuration")
            self.driver = self.browser.get_driver(self.config["url"])
            if not self.driver:
                raise ValueError("Failed to initialize WebDriver")
            self.home_page = HomePage(self.driver)
            self.register_page = RegisterPage(self.driver)
        except Exception as e:
            self.fail(f"Setup failed: {e}")

    def test_register_page_successfully(self):
        self.register_page.first_name_input(self.config["first_name"])
        self.register_page.last_name_input(self.config["last_name"])
        self.register_page.address_input(self.config["address_input"])
        self.register_page.city_input(self.config["city_input"])
        self.register_page.state_input(self.config["state_input"])
        self.register_page.zip_code_input(self.config["zip_code_input"])
        self.register_page.phone_input(self.config["phone_input"])
        self.register_page.ssn_input(self.config["ssn_input"])
        self.register_page.user_name_input(self.config["user_name"])
        self.register_page.password_input(self.config["password"])
        self.register_page.password_confirm_input(self.config["password_confirm"])

        self.register_page.click_registration_confirm_button()
        self.assertTrue(SuccessRegisterPage.success_register_text_shown())

    def tearDown(self):
        self.browser.close_browser()


if __name__ == "__main__":
    unittest.main()
