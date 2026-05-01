class InsufficientFundException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Account:
    def __init__(self):
        self.balance = 0
        self.count = 0

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, Current Balance: {self.balance}")

    def withdrawal(self, amount):
        # minimum transaction
        if amount < 2000:
            raise InsufficientFundException("You cannot withdraw more than ₹2000 in a single transaction.")

        #maximum transaction
        if self.count >= 2:
            raise InsufficientFundException("Withdrawal limit exceeded. Maximum 2 withdrawals allowed.")


        if self.balance - amount >= 2000:
            self.balance -= amount
            self.count += 1
            print(f"Withdrew: {amount}, Remaining Balance: {self.balance}")
        else:
            raise InsufficientFundException("Insufficient balance. Minimum ₹2000 must remain in the account.")


# Example
acc = Account()
acc.set_balance(50000)
print(acc.get_balance())

try:
    acc.deposit(2000)  # balance = 7000
    acc.withdrawal(3000)  # balance = 4000
    acc.withdrawal(2500)
    acc.withdrawal(21000)



except InsufficientFundException as e:
    print("exception:", e)


##################################################################################################################
#
# class LimitExceededException(Exception):
#     def __init__(self, msg):
#         super().__init__(msg)
#
#
# class Wallet:
#     def __init__(self):
#         self.balance = 0
#         self.withdraw_count = 0
#
#     def set_balance(self, amount):
#         self.balance = amount
#
#     def get_balance(self):
#         return self.balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited: {amount}, Balance: {self.balance}")
#
#     def withdraw(self, amount):
#         #  1: minimum withdrawal
#         if amount < 500:
#            raise LimitExceededException("Minimum withdrawal is ₹500")
#
#         #  2: max 3 withdrawals
#         if self.withdraw_count >= 3:
#             raise LimitExceededException("Withdrawal limit reached (max 3)")
#
#         # 3: minimum balance must remain
#         if self.balance - amount < 1000:
#             raise LimitExceededException("Minimum ₹1000 must remain in wallet")
#
#         self.balance -= amount
#         self.withdraw_count += 1
#         print(f"Withdrawn: {amount}, Remaining Balance: {self.balance}")
#
# w = Wallet()
# w.set_balance(10000)
# print("Initial Balance:", w.get_balance())
#
# try:
#         w.deposit(2000)
#         w.withdraw(1000)
#         w.withdraw(2000)
#         w.withdraw(3000)
#         w.withdraw(1500)
#
# except LimitExceededException as e:
#
#         print("Exception:", e)


#######################################################################################################z#######


















