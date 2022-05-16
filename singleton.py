# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
class Singleton(type):
    _instances = {}
    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        else:
            cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]

class Test(metaclass=Singleton):
    pass


# https://www.jianshu.com/p/eeda9fdf2e03
def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class LogHelper(object):
    x = # something
