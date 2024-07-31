class MathOperations:
    # Static method
    @staticmethod
    def add(x, y):
        return x + y

    # Static method
    @staticmethod
    def multiply(x, y):
        return x * y

# Accessing static methods
# math=MathOperations
# print(math.add(5,5))
print(MathOperations.add(5, 3))      # Output: 8
print(MathOperations.multiply(5, 3)) # Output: 15



class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

# Accessing static methods without creating an instance
temp_in_celsius = 25
temp_in_fahrenheit = 77

converted_to_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(temp_in_celsius)
converted_to_celsius = TemperatureConverter.fahrenheit_to_celsius(temp_in_fahrenheit)

print(f"{temp_in_celsius}°C is {converted_to_fahrenheit}°F")  # Output: 25°C is 77.0°F
print(f"{temp_in_fahrenheit}°F is {converted_to_celsius}°C")  # Output: 77°F is 25.0°C
