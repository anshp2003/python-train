# class person:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def diplay(self):  
#         print(self.a,self.b)


# obj=person("ansh",21)
# obj.diplay()

# class math:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         self.c=a+b
#     def diplay(self):  
        
#         print(self.c)

# obj=math(2,10)
# obj.diplay()

# create a class person display name,age,salary of a person

class person:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def display(self):
        print(f"Name:{self.a},Age:{self.b},Salary:{self.c}") 

obj=person("Ansh",21,50000)
obj.display()           
        


















