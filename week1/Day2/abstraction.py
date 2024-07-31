from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class dog(animal):
    def sound(self):
        print("Bow Bow") 
    


class cat(animal):
    def sound(self):
        print ("Meow")
    
dog=dog()
cat=cat()  

dog.sound()
cat.sound()