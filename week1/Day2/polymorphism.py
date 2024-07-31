# polymorphism are two types 

# 1. method oerloading
# 2. method overriding

class MathOperations:
    def add(self, *args):
        return sum(args)
    
# Create an instance of MathOperations
math_op = MathOperations()

# Call the add method with two arguments
print(math_op.add(1, 2))  # Output: 3

# Call the add method with three arguments
print(math_op.add(1, 2, 3))  # Output: 6

# Call the add method with four arguments
print(math_op.add(1, 2, 3, 4))  # Output: 10
class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c
    
# Create an instance of MathOperations
math_op = MathOperations()

# Call the add method with two arguments
print(math_op.add(1, 2))  # Output: 3

# Call the add method with three arguments
print(math_op.add(1, 2, 3))  # Output: 6


# method overriding

class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call the sound method on each instance
print(dog.sound())  # Output: Woof!
print(cat.sound())  # Output: Meow!


class Animal:
    def sound(self):
        print("Some generic animal sound")

class Mammal(Animal):
    def sound(self):
        print("Some generic mammal sound")

class Dog(Mammal):
    def sound(self):
        super().sound()    
        super().sound()    
        
        print("Bark")

# Create an instance of Dog
dog = Dog()

# Call the overridden method
dog.sound()  # Output: Bark
