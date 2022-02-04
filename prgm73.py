class Bank:
    def __init__(self,num=0,n='guest',atype='formal',bal=0):
        self.anumber=anum
        self.name=name
        self.acctype=atype
        self.balance=bal
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter Withdrawal amount "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n Withdrawal amout :", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Account number:",self.anumber)
        print("\n Name=",self.name)
        print("\n type=",self.acctype)
        print("\n Balance=",self.balance)
 

s = Bank(1,"Joel","savings",25000)
s.deposit()
s.withdraw()
s.display()
