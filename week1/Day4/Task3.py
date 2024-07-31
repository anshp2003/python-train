"""
2) Modify the Vehicle class by adding a class method to keep track of the total number of vehicles created and a static method that provides general advice on vehicle maintenance.
"""


class vehicle:
    total_vehicle=0

    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        vehicle.total_vehicle +=1
    def add_vehicle(self):
        return f"vehicle name: {self.brand} and model: {self.model}"
    
    @classmethod
    def total(cls):
        return f"Total vehicle is created: {cls.total_vehicle}"
    
    @staticmethod
    def maintenance_advice():
        return("General Vehicle Maintenance Advice:\n"
            "1. Regularly check and change the oil.\n"
            "2. Keep the tires properly inflated and rotated.\n"
            "3. Check the brakes and brake fluid regularly.\n"
            "4. Replace the air filter periodically.\n"
            "5. Keep the vehicle clean inside and out.\n"
            "6. Regularly check the battery and replace if necessary.\n"
            "7. Follow the manufacturer's maintenance schedule.")
    
obj=vehicle("Toyota Supera",1985)
obj1=vehicle("Ford Mustang",1969)
print(f"{obj.add_vehicle()}\n{obj1.add_vehicle()}")
print(vehicle.total())
print(vehicle.maintenance_advice())