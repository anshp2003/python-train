# class Ageerror(Exception):
#     pass


# try:
#     age=int(input("enter the age: "))

#     if(age<18):
#         raise Ageerror
#     pass
# except Ageerror:
#     print("the age is not valid to vote")

# else:
#     print("person is eligible to vote")



class NegativeNumberError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    return number

try:
    num = int(input("Enter a positive number: "))
    check_positive(num)
except NegativeNumberError as e:
    print(e)
except ValueError:
    print("Please enter a valid integer.")
else:
    print("number is positive")    
finally:
    print("some imp of code")



class InsufficientFundsError(Exception):
    """Exception raised for errors in the withdrawal amount."""
    def __init__(self, balance, amount):
        self.message = f"Insufficient funds: balance is {balance}, attempted to withdraw {amount}"
        super().__init__(self.message)

class NegativeDepositError(Exception):
    """Exception raised for errors in the deposit amount."""
    def __init__(self, amount):
        self.message = f"Cannot deposit a negative amount: {amount}"
        super().__init__(self.message)

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise NegativeDepositError(amount)
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount

# Usage
account = BankAccount(100)

try:
    account.deposit(-50)
except NegativeDepositError as e:
    print(e)

try:
    account.withdraw(200)
except InsufficientFundsError as e:
    print(e)


class UnsupportedFileFormatError(Exception):
    """Exception raised for unsupported file formats."""
    def __init__(self, filename):
        self.message = f"Unsupported file format: {filename}"
        super().__init__(self.message)

def process_file(filename):
    if not filename.endswith('.txt'):
        raise UnsupportedFileFormatError(filename)
    with open(filename, 'r') as file:
        # Process file content
        content = file.read()
        return content

# Usage
try:
    content = process_file('data.csv')
except UnsupportedFileFormatError as e:
    print(e)

try:
    content = process_file('document.pdf')
except UnsupportedFileFormatError as e:
    print(e)

