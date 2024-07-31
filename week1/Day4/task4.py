class Account:
    def __init__(self,initial_balance=0.0):
        if initial_balance < 0:
            initial_balance=0
        self.balance=initial_balance
        self.transaction=[]

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            self.transaction.append(f"Desposited: {amount:2f}") 
        else:
            print("Deposit amount will must be Positive")    

    def withdraw(self,amount):
        if amount>0:
        
            if amount <= self.balance:
                self.balance-=amount        
                self.transaction.append(f"withdraw: {amount:.2f}") 
            else:
                print("funds are insufficient")
        else:
            print("withdraw amount muste be positive")
    def get_balance(self):
        return self.balance

    def get_statement(self):
        for transaction in self.transaction:
            print(transaction)      
        print(f"current balance: {self.balance:2.2f}")

obj=Account(1000)
obj.deposit(500)
obj.withdraw(500)
obj.deposit(250)
obj.get_statement()


# another method

# class Account:
#     def __init__(self, initial_balance=0.0):
#         if initial_balance < 0:
#             raise ValueError("Initial balance cannot be negative.")
#         self._balance = initial_balance
#         self._transactions = []

#     def deposit(self, amount):
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive.")
#         self._balance += amount
#         self._transactions.append(f"Deposited: ${amount:.2f}")
#         print(f"Deposited ${amount:.2f}")

#     def withdraw(self, amount):
#         if amount <= 0:
#             raise ValueError("Withdrawal amount must be positive.")
#         if amount > self._balance:
#             raise ValueError("Insufficient funds.")
#         self._balance -= amount
#         self._transactions.append(f"Withdrew: ${amount:.2f}")
#         print(f"Withdrew ${amount:.2f}")

#     def get_balance(self):
#         return self._balance

#     def get_statement(self):
#         statement = "\n".join(self._transactions)
#         statement += f"\nCurrent balance: ${self._balance:.2f}"
#         return statement

# # Example usage:
# try:
#     account = Account(100)
#     account.deposit(50)
#     account.withdraw(30)
#     account.deposit(20)
#     print(account.get_statement())
# except ValueError as e:
#     print(e)


