# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
class Singleton(type):
    _instances = {}
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwds)
        else:
            cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]

class Test(metaclass=Singleton):
    pass
