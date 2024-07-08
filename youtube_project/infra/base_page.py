from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage():

    def __init__(self,driver: WebDriver):
        self._driver = driver

    def refresh_page(self):
        self._driver.refresh()
        
