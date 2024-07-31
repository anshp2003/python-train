class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Example usage:
c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 7)

c3 = c1 + c2
print(c3)  # Output: 4 + 9i
