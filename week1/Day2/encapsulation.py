class person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    
    def set_name(self,name):
        self.__name=name
    def set_age(self,age):
         self.__age=age
    
obj=person("ansh",20)
print(obj.get_name(),obj.get_age())
obj.set_name("kalu")
obj.set_age(25)
print(obj.get_age(),obj.get_name())








        