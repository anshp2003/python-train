# class Employee:
#     def __init__(self, first, last):
#         self.firstname = first
#         self.lastname = last

#     @property
#     def email(self):
#         return f"{self.firstname}.{self.lastname}@gmail.com"
    
#     @property
#     def fullname(self):
#         return f"{self.firstname} {self.lastname}"

#     @fullname.setter
#     def fullname(self, name):
#         first, last = name.split()
#         self.firstname = first
#         self.lastname = last

# # Creating an instance of Employee
# e1=Employee("Ansh", "Patel")
# print(e1.fullname)  # Should print: Ansh Patel
# print(e1.email)  # Should print: ansh.patel@gmail.com

# # Updating fullname using the setter
# e1.fullname = "Jay Patel"
# print(e1.firstname)  # Should print: Jay
# print(e1.lastname)  # Should print: Patel

# class MyClass:
#     def __init__(self):
#         self._value = 0  # Protected attribute

#     @property
#     def value(self):
#         return self._value  # Getter method

#     @value.setter
#     def value(self, value):
#         if value < 0:
#             raise ValueError("Value must be non-negative")  # Validation logic
#         self._value = value  # Setter method

# obj = MyClass()
# obj.value = 10  # This works fine
# print(obj.value)  # Output: 10

# obj.value = 5  # This raises a ValueError
# print(obj.value)  # Output: 10


class employee:

    def __init__(self,first,last):

        self.firstname=first
        self.lastname=last
    @property
    def email(self): 
        return f"{self.firstname}{self.lastname}@gmail.com"
    
    @property
    def fullname (self):
        return f"{self.firstname}{self.lastname}"
        
        

    @fullname.setter
    def fullname(self,name):
        first,last=name.split()
        self.firstname=first
        self.lastname=last
    # @email.setter

    # def email(self,email):
    #     name_part= email.split('@')[0] 
    #     self.firstname,self.lastname= name_part.split('.')   
e1=employee("ansh","patel")
print(e1.email)
e1.fullname="raj patel"
print(e1.email)
    
