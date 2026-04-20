# class Payment:
#     def pay(self, amount):
#         print(f"Paying ₹{amount}")
#
# class UPI(Payment):
#     def pay(self, amount):
#         print("Paying ₹",amount,"via UPI")
#
# class Card(Payment):
#     def pay(self, amount):
#         print("Paying ₹",amount, "via Card")
#
# methods = [UPI(), Card()]
#
# for m in methods:
#     m.pay(500)

################################################################################################


class Dog:
    def sound(self):
        print("Dog barks")

class Cat(Dog):
    def sound(self):
        print("Cat meows")

animals = [Dog(), Cat()]

for a in animals:
    a.sound()