from selenium.webdriver.common.by import By

class Main_Page_locator(object):
    """一个主页面定位器类，所有的页面定位器应该来自这里"""
    search_button = (By.CLASS_NAME, 'android.widget.Button')
    input_area = (By.XPATH,"//@class='android.widget.EditText'") # 搜索框
    search_text = 'language'
