from utils.BasePage import BasePage
from locator.Settings_locators import Main_Page_locator


class Main_Page(BasePage):

    def click_search_button(self):
        """触发搜索功能"""
        self.logger.info('main page search button.')
        element = self.driver.find_element(*Main_Page_locator.search_button)
        element.click()

    def input_text(self):
        # element = self.driver.find_element(*Main_Page_locator.input_area)
        self.logger.info('main page input text find element')
        # element.send_keys(Main_Page_locator.search_text)
