# Singleton accidently, but not process-safe (thread-safe)

class FakeProperty:

    def __init__(self, attr: str, dtype:Type) -> None:
        self.attr = attr
        self.dtype = dtype

    def __get__(self, obj, objtype):
        return obj._cache[self.attr]

    def __set__(self, obj, value):
        if not isinstance(value, self.dtype):
            raise TypeError("Attribute: %s requires tpye: %s, but type:%s is gotten.",self.attr, self.dtype, type(value))
        obj._cache[self.attr] = value
    
    def __delete__(self, obj):
        obj._cache[self.attr] = 0

def dynamic_property(*args: Any, **kwargs: Any):
    def decorate(cls):
        for attr, dtype in kwargs.items():
            setattr(cls, attr, FakeProperty(attr, dtype))
        return cls
    return decorate

  
@dynamic_property(
    slot1 = int,
    slot2 = str
)
class Test():
    pass
