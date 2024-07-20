from selenium.webdriver.common.by import By
from ui_testing.ParabankTesting.logic.base_page_app import BasePage
from selenium import common as c


class RegisterPage(BasePage):
    FIRST_NAME_INPUT = '//input[@id="customer.firstName"]'
    LAST_NAME_INPUT = '//input[@id="customer.lastName"]'
    ADDRESS_INPUT = '//input[@id="customer.address.street"]'
    CITY_INPUT = '//input[@id="customer.address.city"]'
    STATE_INPUT = '//input[@id="customer.address.state"]'
    ZIP_CODE_INPUT = '//input[@id="customer.address.zipCode"]'
    PHONE_INPUT = '//input[@id="customer.phoneNumber"]'
    SSN_INPUT = '//input[@id="customer.ssn"]'
    USERNAME_INPUT = '//input[@id="customer.username"]'
    PASSWORD_INPUT = '//input[@id="customer.password"]'
    CONFIRM_INPUT = '//input[@id="repeatedPassword"]'
    REGISTER_BUTTON = '//input[@value="Register"]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._first_name_input = self._driver.find_element(By.XPATH, self.FIRST_NAME_INPUT)
            self._last_name_input = self._driver.find_element(By.XPATH, self.LAST_NAME_INPUT)
            self._address_input = self._driver.find_element(By.XPATH, self.ADDRESS_INPUT)
            self._city_input = self._driver.find_element(By.XPATH, self.CITY_INPUT)
            self._state_input = self._driver.find_element(By.XPATH, self.STATE_INPUT)
            self._zip_code_input = self._driver.find_element(By.XPATH, self.ZIP_CODE_INPUT)
            self._phone_input = self._driver.find_element(By.XPATH, self.PHONE_INPUT)
            self._ssn_input = self._driver.find_element(By.XPATH, self.SSN_INPUT)
            self._username_input = self._driver.find_element(By.XPATH, self.USERNAME_INPUT)
            self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
            self._confirm_input = self._driver.find_element(By.XPATH, self.CONFIRM_INPUT)
            self._register_button = self._driver.find_element(By.XPATH, self.REGISTER_BUTTON)
        except c.NoSuchElementException as e:
            print("NoSuchElementException", e)

    def fill_first_name_input(self, first_name):
        self._first_name_input.send_keys(first_name)

    def fill_last_name_input(self, last_name):
        self._last_name_input.send_keys(last_name)

    def fill_address_input(self, address):
        self._address_input.send_keys(address)

    def fill_city_input(self, city):
        self._city_input.send_keys(city)

    def fill_state_input(self, state):
        self._state_input.send_keys(state)

    def fill_zip_code_input(self, zip_code):
        self._zip_code_input.send_keys(zip_code)

    def fill_phone_input(self, phone):
        self._phone_input.send_keys(phone)

    def fill_ssn_input(self, ssn):
        self._ssn_input.send_keys(ssn)

    def fill_username_input(self, username):
        self._username_input.send_keys(username)

    def fill_password_input(self, password):
        self._password_input.send_keys(password)

    def fill_confirm_input(self, confirm):
        self._confirm_input.send_keys(confirm)

    def click_on_register_button(self):
        self._register_button.click()

    def fill_all_inputs_flow(self, first_name, last_name, address, city, state,
                             zip_code, phone, ssn, username, password, confirm):
        self.fill_first_name_input(first_name)
        self.fill_last_name_input(last_name)
        self.fill_address_input(address)
        self.fill_city_input(city)
        self.fill_state_input(state)
        self.fill_zip_code_input(zip_code)
        self.fill_phone_input(phone)
        self.fill_ssn_input(ssn)
        self.fill_username_input(username)
        self.fill_password_input(password)
        self.fill_confirm_input(confirm)