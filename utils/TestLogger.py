import logging
import os
from utils.configParse import config

def get_log_path(log_name):
    """log 存放路径。如果用户没有配置 log_path，就放到 temp_log_path 下"""
    if config.getArg('log_path'):
        log_path = os.path.join(config.getArg('project_path'),config.getArg('log_path'),log_name+'.log')
        os.makedirs(os.path.join(config.getArg('project_path'),config.getArg('log_path')),exist_ok=True)
    else:
        log_path = os.path.join(config.getArg('project_path'),config.getArg('temp_log_path'),log_name+'.log')
        os.makedirs(os.path.join(config.getArg('project_path'), config.getArg('temp_log_path')),exist_ok=True)
    return log_path

class Logger(object):
    def __init__(self,name,log_name):
        """name: logger对象的名字
           log_name: log文件名字,存放在：项目/temp_log_path/xx.log """

        # log存放路径
        log_path = get_log_path(log_name)

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level = logging.INFO)
        handler = logging.FileHandler(log_path)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
        handler.setFormatter(formatter)
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(formatter)

        # 如果已经有 handlers，就清空handlers，否则运行多个测试用例时，会重复打印log。
        # 网上的说法是多个测试用例调用logger时，会重复添加handler，导致打印多次
        if self.logger.hasHandlers():
            self.logger.handlers.clear()

        self.logger.addHandler(handler)
        self.logger.addHandler(console)

    def info(self,msg):
        return self.logger.info(msg)

    def debug(self,msg):
        return self.logger.debug(msg)

    def warning(self,msg):
        return self.logger.warning(msg)

    def error(self,msg):
        return self.logger.error(msg)

    def critical(self,msg):
        return self.logger.critical(msg)

if __name__ == '__main__':
    logger = Logger('test','testlog')
    logger.info("creating an logger.")








