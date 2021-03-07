import os
import time
import unittest
from utils.configParse import config
from utils.HTMLTestRunner import HTMLTestRunner


if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    test_cases_path = config.getArg('test_cases_path')
    result_dir = os.path.join(config.getArg('result_path'), now)
    os.makedirs(result_dir, exist_ok=True)
    report = '{0}/Report.html'.format(result_dir)
    config.setArg('log_path', result_dir)

    discover = unittest.defaultTestLoader.discover(start_dir=test_cases_path, pattern="*.py")
    with open(report, 'wb')as f:
        runner = HTMLTestRunner(stream=f, title="测试报告", description="本测试报告...")
        runner.run(discover)