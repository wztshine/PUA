import logging
from utils.TestLogger import Logger


class BasePage(object):
    """初始化所有页面都会调用的基本页类"""
    def __init__(self, driver,loggerName=None):
        self.driver = driver
        # 创建logger对象，用来保存log
        if loggerName == None:
            self.logger = Logger(self.__class__.__name__,self.__class__.__name__)
        else:
            self.logger = logging.getLogger(loggerName+'.'+self.__class__.__name__)