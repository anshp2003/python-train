class vechile:
    def __init__(self):
        self.speed=0

    def set_speed(self,speed):

        self.speed=speed
        return f"speed set to {self.speed} km/h"

    def stop(self):
        self.speed=0 
        return "vechile Stopped"      

    def display_speed(self):
        return f"current speed of {self.speed} km/h"

class car(vechile):

    def __init__(self):
        super().__init__()        



class Truck(vechile):

    def __init__(self):
        super().__init__()  


truck=vechile()

print(truck.set_speed(50))
print(truck.display_speed())
print(truck.stop())
print(truck.display_speed())


car1=vechile()
print(car1.set_speed(100))
print(car1.display_speed())
print(car1.stop())
print(car1.display_speed())