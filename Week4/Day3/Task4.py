import functools
import logging

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO)

# Custom decorator to log method calls
def log_method_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling method: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Metaclass to ensure methods are decorated
class MethodLoggingMeta(type):
    def __new__(cls, name, bases, dct):
        methods_to_decorate = dct.get('__methods_to_log__', [])
        
        for method_name in methods_to_decorate:
            if method_name in dct and callable(dct[method_name]):
                dct[method_name] = log_method_call(dct[method_name])
                
        return super().__new__(cls, name, bases, dct)

# Example class using the metaclass
class MyClass(metaclass=MethodLoggingMeta):
    __methods_to_log__ = ['foo', 'bar']
    
    def foo(self):
        print("Executing foo")

    def bar(self):
        print("Executing bar")

    def baz(self):
        print("Executing baz")

# Testing the class
obj = MyClass()
obj.foo()  # Should log method call
obj.bar()  # Should log method call
obj.baz()  # Should not log method call
