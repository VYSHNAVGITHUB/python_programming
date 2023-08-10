class Bank:
    def create_ac(self,name,acno,):
        self.name=name
        self.acno=acno
        self.balance=0
    def deposit(self,amount):
        self.amount=amount
        self.balance=self.amount+self.balance
        print("your ac has been credited with amount",self.amount)
        print("availale balance is",self.balance)
    def withdraw(self,amnt):
        self.amnt=amnt
        if(self.amnt<=self.balance):
            self.balance=self.balance-self.amnt
            print("your ac has been debited with amount",self.amnt)
            print("available balance is",self.balance)
        else:
            print("insufficient blnc")

ac1=Bank()
ac1.create_ac("anu",50224522)
ac1.deposit(25000)
ac1.withdraw(20000)
ac1.withdraw(10000)


