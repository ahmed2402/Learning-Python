# Let‘s Practice
# Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.

class Account :
    

    def __init__(self,accNo,balance):
        self.balance = balance
        self.accountNo = accNo

    def debit(self,amount):
        self.balance = self.balance - amount
        print(f"Here you go your {amount}PKR\n")
        print(f"Your remaining Balance is : {self.balance}\n")

    def credit(self,amount):
        self.balance = self.balance + amount
        print(f"{amount}PKR is credited into your account\n")
        print(f"Your Balance is : {self.balance}\n")

    def printBlance(self):
        print(f"Your Balance is {self.balance}")


b1 = Account(123,75000)
print(b1.accountNo)
print(b1.balance)

b1.debit(10000)
b1.credit(5000)
b1.printBlance()

