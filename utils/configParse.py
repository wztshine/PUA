import os

class config(object):
    current_path = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(current_path,'config.txt')

    @classmethod
    def getArg(cls,argName):
        # 从config.txt中通过参数名，获取参数值
        with open(cls.config_path,'r',encoding='utf-8') as f:
            for line in f:
                if len(line.strip()) == 0:
                    pass
                else:
                    name,content = line.split('#')[0].split('=')
                    if argName == name.strip():
                        if content.strip() == "":
                            return None
                        else:
                            return content.strip()
            raise Exception("Can't find the Argument: %s" % argName)

    @classmethod
    def setArg(cls,argName,content):
        # 对config.txt 设置 参数名和参数值
        arg_list = []
        comment = ''
        with open(cls.config_path,'r',encoding='utf-8') as f:
            for line in f:
                name = line.split('#')[0].split('=')[0].strip()
                if argName != name.strip():
                    arg_list.append(line)
                else:
                    comment = '  #' + line.split('#')[-1]+'\n'
        arg_list.append(argName+' = '+ content + comment)
        arg_list = [li for li in arg_list if li != '\n']
        open(cls.config_path,'w',encoding='utf-8').write(''.join(arg_list))


if __name__ =="__main__":
    config.setArg('log_path', '')
