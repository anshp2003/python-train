# a=int(input("enter your number"))
# print(f"Multiplication table of {a}")
# try:
#     for i in range(1,11):
#         print(f"{a}X{i}={a*i}")
# except Exception as e:
#     print(e)
# print("some imp lines of code ")

# try:
#     x = int(input("Enter a number: "))
#     y = 10 / x
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except ValueError:
#     print("Invalid input! Please enter a number.")

# print(y)


try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
else:
    print(f"The division was successful {y}")
