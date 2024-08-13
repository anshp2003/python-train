# class Meta(type):
#     def __new__(cls,name,base,dct):
#         print(f'creating class {name}')
#         return super().__new__(cls,name,base,dct)
    
# class myclass(metaclass=Meta):
#     pass


# instance=myclass()
# print(instance)


# class MethodValidator(type):
#     def __new__(cls, name, bases, dct):
#         if 'process' not in dct:
#             raise TypeError(f'{name} class is missing required method "process"')
#         return super().__new__(cls, name, bases, dct)

# class ValidClass(metaclass=MethodValidator):
#     def process(self):
#         print("Processing...")

# class InvalidClass(metaclass=MethodValidator):
#     pass

# # Test the classes
# a = ValidClass()
# a.process()

# try:
#     invalid_instance = InvalidClass()
# except TypeError as e:
#     print(e)

# class Registry(type):
#     def __init__(cls, name, bases, dct):
#         if not hasattr(cls, 'registry'):
#             cls.registry = []
#         else:
#             cls.registry.append(cls)
#         super().__init__(name, bases, dct)

# class Base(metaclass=Registry):
#     pass

# class SubClass1(Base):
#     pass

# class SubClass2(Base):
#     pass

# # Test the registry
# print(Base.registry)  # Output: [<class '__main__.SubClass1'>, <class '__main__.SubClass2'>]



class UppercaseAttributes(type):
    def __new__(cls, name, bases, dct):
        for attribute_name in dct:
            if not attribute_name.isupper() and not attribute_name.startswith('__'):
                raise TypeError(f"Attribute '{attribute_name}' in class '{name}' is not uppercase")
        return super().__new__(cls, name, bases, dct)

class ValidClass(metaclass=UppercaseAttributes):
    ATTRIBUTE_ONE = "Value1"
    ATTRIBUTE_TWO = "Value2"

class InvalidClass(metaclass=UppercaseAttributes):
    attribute_one = "Value1"
    ATTRIBUTE_TWO = "Value2"

# Test the valid class
valid_instance = ValidClass()
print(valid_instance.ATTRIBUTE_ONE)

# Test the invalid class
try:
    invalid_instance = InvalidClass()
except TypeError as e:
    print(e)
