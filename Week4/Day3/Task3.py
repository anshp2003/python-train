from datetime import datetime

class Time(type):
    def __new__(cls,name,base,dct):
        dct['created_at']=datetime.now()
        return super().__new__(cls,name,base,dct)
    
class Myclass(metaclass=Time):
    pass    

class anotherMyclass(metaclass=Time):
    pass

print(Myclass.created_at)
print(anotherMyclass.created_at)