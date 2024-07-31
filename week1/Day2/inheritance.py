# single inheritance

class person:
    def __init__(self,a,b):
        self.name=a
        self.age=b

    def display(self):
        print(self.name)
        print(self.age)   

class dep(person):
    def __init__(self,a,b,s,d):
        self.depname=d
        self.salary=s       
        person.__init__(self,a,b)
    def display1(self):

        print(self.depname)    
        print(self.salary)    

dep=dep("ansh",21,"it",200000)
dep.display()  
dep.display1()      




# Multiple inheritance


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee:
    def __init__(self, employee_id, department):
        self.employee_id = employee_id
        self.department = department

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")

class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, department, team_size):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, department)
        self.team_size = team_size

    def display_manager_info(self):
        # self.display_person_info()
        # self.display_employee_info()
        print(f"Team Size: {self.team_size}")

# Example usage:
manager = Manager("Alice", 35, "E123", "HR", 10)
manager.display_person_info()
manager.display_manager_info()
manager.display_employee_info()




