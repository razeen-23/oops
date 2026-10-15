class bankaccount:
    def __init__(self,balance=0):
        self.balance=balance
        

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("amount deposited succesfully.")
        else:
            print("invalid deposited money.")

    def withdraw(self,amount):
        if amount <=0:
            print("invalid withdrawal money")
        elif amount > self.balance:
            print("insufficent balance")
        else:
            self.balance -= amount
            print("amount withrdawn succesfully.")

    def check_balance(self):
        print("current balance:",self.balance)


account = bankaccount()

while True:
    print("/n --- banking system ---")
    print("1.deposit")
    print("2.withdraw")
    print("3.check_balance")
    print("4.exit")

    choice = input("enter your choice:")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("invalid choice")






    # if choice == "1":
    #     print("deposit selected")

    # elif choice == "2":
    #     print("withdraw selected")
    
    # elif choice == "3":
    #     print("check balance selected")

    # elif choice == "4":
    #     print("thank you!")
    #     break

    # else:
    #     print("invalid choice")




    


              




    

