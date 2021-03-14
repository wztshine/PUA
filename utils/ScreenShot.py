import inspect
from functools import wraps
import traceback
import sys
import os

from utils.configParse import config


pj_path = config.getArg('project_path')
log_path = config.getArg('log_path')
log_path = os.path.join(pj_path,log_path)

def decorator_for_func(orig_func,driver):
    @wraps(orig_func)
    def decorator(*args, **kwargs):
        try:
            return orig_func(*args, **kwargs)
        except:
            img_path = os.path.join(log_path,orig_func.__name__+'.jpg')
            print('Error found on',orig_func.__name__)
            # 获取错误信息
            a,b,c = sys.exc_info()
            for i in traceback.extract_tb(c):
                print(i)
            driver.get_screenshot_as_file(img_path)
            raise Exception(orig_func.__name__,'failed!')
    return decorator

def decorator_for_class(cls):
    for name, method in inspect.getmembers(cls):
        if (not inspect.ismethod(method) and not inspect.isfunction(method)) or inspect.isbuiltin(method):
            continue
        elif name.lower().startswith('test'):
            setattr(cls, name, decorator_for_func(method,cls.__getattribute__(cls,'driver')))
    return cls