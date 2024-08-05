class bankaccount:
    def __init__(self,balance=0):
        self.balance=balance

    def __add__(self,amount):
        if (amount>=0):
            self.balance+=amount 
            return self   
        else:
            print("error")    

    def __sub__(self,amount):
        if (amount<=self.balance):
            self.balance-=amount   
            return self 
        else:
            print("error")          
    def deposit(self,amount):
        return self.__add__(amount)
    def withdraw(self,amount):
        return self.__sub__(amount)
    def __str__(self):
        return f"bankaccount(balance={self.balance})"      






acc=bankaccount(1000)
print(acc)        

acc.deposit(500)
print(acc)

acc.withdraw(550)
print(acc)


try:
    acc-(100)  # Attempt to withdraw more than the balance
except ValueError as e:
    print(e)  # Output: Insufficient funds for withdrawal.