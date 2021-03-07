class Singleton(object):  
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            Singleton._instance = super().__new__(cls)
        return Singleton._instance

