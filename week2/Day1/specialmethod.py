# class person:
#     def __init__(self,age):
#         # self.name=name
#         self.age=age

#     def __add__(self,other):
#         return f"{self.age+other.age} {self.age+other.age} years old"    
    

# p=person(10)
# k=person(10)
# print(p+k)   



# Common Special Methods and Operator Overloading
# Initialization and Representation

# __init__(self, ...): Called when an instance is created.
# __str__(self): Called by str() and print() to return a string representation of the object.
# __repr__(self): Called by repr() to return a string that would recreate the object when passed to eval().
# Arithmetic Operators

# __add__(self, other): Called for the addition operator +.
# __sub__(self, other): Called for the subtraction operator -.
# __mul__(self, other): Called for the multiplication operator *.
# __truediv__(self, other): Called for the true division operator /.
# __floordiv__(self, other): Called for the floor division operator //.
# __mod__(self, other): Called for the modulo operator %.
# __pow__(self, other): Called for the exponentiation operator **.
# Comparison Operators

# __eq__(self, other): Called for the equality operator ==.
# __ne__(self, other): Called for the inequality operator !=.
# __lt__(self, other): Called for the less than operator <.
# __le__(self, other): Called for the less than or equal to operator <=.
# __gt__(self, other): Called for the greater than operator >.
# __ge__(self, other): Called for the greater than or equal to operator >=.
# Unary Operators

# __neg__(self): Called for the negation operator - (unary).
# __pos__(self): Called for the unary plus operator + (unary).
# __abs__(self): Called for the abs() function.
# __invert__(self): Called for the bitwise inversion operator ~.


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Example usage
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
v4 = v1 - v2
v5 = v1 * 3
v6 = -v1

print(v3)  # Output: Vector(6, 8)
print(v4)  # Output: Vector(-2, -2)
print(v5)  # Output: Vector(6, 9)
print(v6)  # Output: Vector(-2, -3)
print(v1 == Vector(2, 3))  # Output: True
