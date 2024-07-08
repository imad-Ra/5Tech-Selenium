import unittest

from youtube_project.infra.browser_wrapper import BrowserWrapper
from youtube_project.infra.config_provider import ConfigProvider
from youtube_project.logic.home_page import HomePage


class TestShortsButton(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.browser.close_browser()
    def test_shorts_button(self):
        # check if short page opened correctly
        self.home_page.click_shorts_button()
        self.driver.implicitly_wait(10)
        self.assertEqual(self.driver.current_url, self.config["url"] + "/shorts")



if __name__ == "__main__":
    unittest.main()
