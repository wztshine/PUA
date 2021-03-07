class config(object):
    @classmethod
    def getArg(cls,argName):
        # 从config.txt中通过参数名，获取参数值
        with open(r'../config.txt','r',encoding='utf-8') as f:
            for line in f:
                name,content = line.split('#')[0].split('=')
                if argName == name.strip():
                    if content.strip() == "":
                        return None
                    return content.strip()
            raise Exception("Can't find the Argument: %s" % argName)

    @classmethod
    def setArg(cls,argName,content):
        # 对config.txt 设置 参数名和参数值
        arg_list = []
        comment = ''
        with open(r'../config.txt','r',encoding='utf-8') as f:
            for line in f:
                name = line.split('#')[0].split('=')[0].strip()
                if argName != name.strip():
                    arg_list.append(line)
                else:
                    comment = '  #' + line.split('#')[-1]
        arg_list.append(argName+' = '+ content + comment)
        open(r'../config.txt','w',encoding='utf-8').write(''.join(arg_list))
