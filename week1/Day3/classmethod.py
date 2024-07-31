class car:

    wheels=4

    def __init__(self,model,year):

        self.model=model
        self.year=year
        # self.wheels=5
    @classmethod
    def number_of_wheels(cls):
        return cls.wheels    

ca=car("toyota" ,"1964")
car1=car("civic","1955")
print(car.number_of_wheels())    
print(car.number_of_wheels()) 


class BankAccount:
    # Class attribute to keep track of the number of accounts
    number_of_accounts = 0

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        BankAccount.number_of_accounts += 1

    # Instance method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    # Instance method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    # Class method to get the number of accounts
    @classmethod
    def get_number_of_accounts(cls):
        return cls.number_of_accounts

# Creating instances of BankAccount
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 1500)

# Accessing class method
print(BankAccount.get_number_of_accounts())  # Output: 2
# Performing some operations
account1.deposit(500)
account2.withdraw(300)

# Checking balances
print(account1.balance)  # Output: 1500
print(account2.balance)  # Output: 1200


class Product:
    # Class attribute to keep track of the total number of products sold
    total_products_sold = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Class method to update the total number of products sold
    @classmethod
    def product_sold(cls, quantity):
        cls.total_products_sold += quantity

    # Class method to get the total number of products sold
    @classmethod
    def get_total_products_sold(cls):
        return cls.total_products_sold

# Creating instances of Product
product1 = Product("Laptop", 1000)
product2 = Product("Phone", 500)

# Updating total products sold
Product.product_sold(10)
Product.product_sold(20)

# Accessing class method
print(Product.get_total_products_sold())  # Output: 30

