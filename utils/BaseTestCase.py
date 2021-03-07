import unittest
from utils.TestLogger import Logger

class TestCase(unittest.TestCase):
    """重写了unittest.TestCase的__init__()，添加了一个Logger对象"""
    def __init__(self,methodName='runTest'):
        super().__init__(methodName)
        self.logger_name = self.__class__.__name__ # self.__class__.__name__是当前类的类名
        self.logger = Logger(self.logger_name,self.logger_name) # logger的名字是类名，存放的log文件名是 类名.log

# class TT(TestCase):
#     def test_add(self):
#         print(self.logger)
#         self.logger.info('add is runing')
#         self.logger.warning('this is warning.')

# if __name__ == '__main__':
#     unittest.main(verbosity=2)