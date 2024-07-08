class BasePage:
    def __init__(self, driver):
        self._driver = driver

    def refresh_page(self):
        self._driver.refresh.reload()
