class Account:
    def __init__(self,initial_balance):
        self._balance=initial_balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,amount):
        self._balance=amount        
        self.log_transcation(self._balance)

    def log_transcation(self,amount):
        print(f"Transaction: setting balance  to {amount}") 

obj=Account(1500)
print(obj.balance)
obj.balance=2000
print(obj.balance)
obj.balance=3000        
print(obj.balance)
