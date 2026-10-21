class bankaccount:
    def __init__(self,balance=0):
        self.__balance = balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print("deposited successfully")
        else:
            print("invalid amount")

    def get_balance(self):
        return self.__balance

    def _deduct_balance(self,amount):
        self.__balance-=amount

class savingsaccount(bankaccount):
    def withdraw(self,amount):
        if 0 < amount<=self.get_balance():
            self._deduct_balance(amount)
            print("amount withdrawn success",amount)
        else:
            print("insufficient balance:")

class currentaccount(bankaccount):
    def __init__(self, balance=0):
        super().__init__(balance)
        self.overdraft_limit=5000

    def withdraw(self,amount):
            if 0 < amount<=self.get_balance() + self.overdraft_limit:
                self._deduct_balance(amount)
                print("current amount withdrawn successfully",amount)
            else:
                print("overdraft limit is exceeded:")

savings = savingsaccount(10000)
current = currentaccount(2000)

print("Savings Account:")
savings.deposit(1000)
savings.withdraw(3000)
print("Balance:", savings.get_balance())

print("\nCurrent Account:")
current.deposit(500)
current.withdraw(4000)
print("Balance:", current.get_balance())                


