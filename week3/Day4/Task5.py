class Divide(Exception):
    pass

def divide1(a, b):
    try:
        if b == 0:
            raise Divide("You entered zero; it cannot divide any number.")
        c = a / b
        print(f"The result of divide is {c}")
    except Divide as e:
        print(e)

# Usage example
divide1(10, 0)   # Should print: You entered zero; it cannot divide any number.
divide1(10, 2)   # Should print: The result of divide is 5.0



# 'another method'
# # Define custom exceptions
# class DivisionByZeroError(Exception):
#     """Exception raised for division by zero."""
#     def __init__(self, message="Cannot divide by zero."):
#         self.message = message
#         super().__init__(self.message)

# class TypeError(Exception):
#     """Exception raised for type errors in division."""
#     def __init__(self, message="Both inputs must be numbers."):
#         self.message = message
#         super().__init__(self.message)

# # Function to divide two numbers
# def divide(a, b):
#     try:
#         if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
#             raise TypeError()
#         if b == 0:
#             raise DivisionByZeroError()
#         return a / b
#     except DivisionByZeroError as e:
#         print(f"Error: {e.message}")
#     except TypeError as e:
#         print(f"Error: {e.message}")

# # Usage examples
# print(divide(10, 2))   # Should print: 5.0
# print(divide(10, 0))   # Should print: Error: Cannot divide by zero.
# print(divide(10, 'a')) # Should print: Error: Both inputs must be numbers.
