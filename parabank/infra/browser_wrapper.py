from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from parabank.infra.config_provider import ConfigProvider


class BrowserWrapper:
    def __init__(self):
        self._driver = None
        self.config = ConfigProvider.load_config_json()

    def get_driver(self, url):
        try:
            if self.config["browser"].lower() == "chrome":
                service = ChromeService(ChromeDriverManager().install())
                self._driver = webdriver.Chrome(service=service)
            elif self.config["browser"].lower() == "firefox":
                service = FirefoxService(GeckoDriverManager().install())
                self._driver = webdriver.Firefox(service=service)
            else:
                raise ValueError(f"Unsupported browser type: {self.config['browser']}")

            self._driver.get(url)
            return self._driver
        except Exception as e:
            print(f"ERROR: {e}")
            return None

    def close_browser(self):
        if self._driver:
            self._driver.quit()