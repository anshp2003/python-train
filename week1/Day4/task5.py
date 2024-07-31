import pandas as pd
from io import StringIO

class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append(f"Deposit: ${amount:.2f}")
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.transactions.append(f"Withdrawal: ${amount:.2f}")
        return self.balance

    def get_balance(self):
        return self.balance

    def get_statement(self):
        statement = [f"Account Statement for {self.account_holder} ({self.account_number}):"]
        statement.extend(self.transactions)
        statement.append(f"Current Balance: ${self.balance:.2f}")
        return "\n".join(statement)

    @classmethod
    def from_csv(cls, csv_input):
        data = pd.read_csv(csv_input)
        
        accounts = []
        for  row in data.iterrows():
            account = cls(row['account_no'], row['name'])
            accounts.append(account)
        return accounts


# Creating accounts from CSV string
accounts = Account.from_csv('C:\\Users\\hp\\Desktop\\ansh\\python training\\week1\\Day4\\Book1.csv')

# Displaying the statements for each account
for account in accounts:
    account.deposit(1000)
    account.withdraw(100)
    print(account.get_statement())

    print('-' * 40)
