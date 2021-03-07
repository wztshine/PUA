import unittest
from pages.Settings_Pages import Main_Page
from appium import webdriver
from utils.BaseTestCase import TestCase


class Test_Settings(TestCase):
    @classmethod
    def setUpClass(self):
        desired_caps = {'platformName': 'Android', # 平台名称
                        'platformVersion': '10',  # 系统版本号
                        'deviceName': '39504f3231593398',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'appPackage': 'com.android.settings',  # apk的包名
                        'appActivity': 'com.android.settings.Settings',  # activity 名称
                        'automationName': 'UiAutomator1',
                        'noReset':True,
                        'fullReset':False,
                        'unicodeKeyboard':True,
                        'resetKeyboard':True
                        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium

    def test_main_page_search(self, t=500):
        """测试搜索按钮"""
        self.logger.info('------------test main page started-------')
        main_page = Main_Page(self.driver,self.logger_name)
        main_page.click_search_button()
        # main_page.input_text()

    def test_xyz(self):
        self.logger.info('---------------Test xyz-------------')

if __name__ == '__main__':
    unittest.main(verbosity=2)   # verbosity 报告的详细程度，默认1