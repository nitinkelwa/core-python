class Account:

    def balance(self):
        self.number = ""
        self.balance = 0.0
        self.account_type = ""

    # setter getter for number

    def setnumber(self, number):
        self.number = number

    def getnumber(self):
        return self.number

    # setter getter for balance

    def setbalance(self, balance):
        self.balance = balance

    def getbalance(self):
        return self.balance

    # setter getter for account type

    def setaccount_type(self, type):
        self.account_type = type

    def getaccount_type(self):
        return self.account_type




    ################################################################################################################
#
#
class ATM:
    def __init__(self):
        self.__balance = 1000   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance:", self.__balance)

atm = ATM()

atm.deposit(500)
atm.show_balance()   # Balance: 1500

