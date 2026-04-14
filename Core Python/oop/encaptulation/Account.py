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

    # Deposit method

    def deposit(self, amt):
        self.balance = self.balance + amt

        print("Total balance after deposit =", self.balance)


