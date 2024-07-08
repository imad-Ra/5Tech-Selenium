from selenium.webdriver.common.by import By

from youtube_project.infra.base_page import BasePage
from selenium import common as c


class HomePage(BasePage):
    VIDEO_THUMBNAIL = '//a[@id="thumbnail"]'
    SHORTS_BUTTON = '//ytd-guide-section-renderer//a[@title="Shorts"]'
    VIDEO_SELECTOR = ('//ytd-rich-grid-row[@class="style-scope ytd-rich-grid-renderer"]//ytd-rich-grid-media['
                      '@class="style-scope ytd-rich-item-renderer"]')[1]

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._video_thumbnail = self._driver.find_element(By.XPATH, self.VIDEO_THUMBNAIL)
            self._shorts_button = self._driver.find_element(By.XPATH, self.SHORTS_BUTTON)
            self._video_selector = self._driver.find_element(By.XPATH, self.VIDEO_SELECTOR)

        except c.NoSuchElementException as e:
            print("NoSuchElementException", e)

    def click_shorts_button(self):
        self._shorts_button.click()

    def click_video_selector(self):
        self._video_selector.click()

    def click_video_thumbnail(self):
        self._video_thumbnail.click()