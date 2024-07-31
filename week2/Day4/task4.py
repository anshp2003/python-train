class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __mul__(self,scaler):
        return vector(self.x*scaler , self.y*scaler)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
v1=vector(5,6)    
# v2=vector(5,6)
# scaler=2
v1=v1*8
print(v1)   

# class Vector:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

#     def __sub__(self, other):
#         return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

#     def __mul__(self, scalar):
#         return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

#     def __repr__(self):
#         return f"Vector({self.x}, {self.y, self.z})"

# # Example usage:
# v1 = Vector(1, 2, 3)
# scalar = 3
# result = v1 * scalar

# print(result)  # Output: Vector(3, 6, 9)
