# input from users.
# name =(input("what is your name :"))  # input is lagane se users se input milega
# print("ohh welcome.",name)            # what's you type in output that is our input
#
# age = input ("what's your age :")
# print("you are a young man because you are ",age,"year old. ")
#
# address=input("where are you from :")
# print("wow nice,you are come from clean city. ",address)
#
from operator import index
from tkinter.font import names
from traceback import print_tb


# question no.1

# a = int(input("Enter first number :"))
# print("first number is :", a)
# print(type(a))
#
# b = int(input("Enter second number :"))
# print("second number is", b)
#
# print("The sum of numbers are =", a + b)


#


# marks = int(input("Enter your marks:"))
#
# print("student result ")
#
# if (marks >= 90):
#     grade = "A"
#
# elif (marks >= 80 and marks <= 89):
#     grade = "B"
#
# elif (marks <= 79 and marks>=60):
#     grade = "C"
#
# else:
#     grade="D"
#
# print("The grade is =", grade)


#  odd or even

# num = int(input("Enter the number for cheking odd or even:"))
#
# if (num % 2 == 0):
#     print("The number  :", num, "even")
#
# else:
#     print("The number ", num, "odd")


#  greatest number of 3.
#
# a = int(input("Enter 1st number:"))
# b = int(input("Enter 2nd number:"))
# c = int(input("Enter 3rd number:"))
# print("")
# print("")
# print("")
#
# if (a >= b and a >= c):
#     print("1st number is largest :", a)
# elif (b >= c):
#     print("2nd number is largest  :", b)
#
# else:
#     print("3rd number is largest  :", c)


#
# class Student:
#     def __init__(self):
#         self.__m = 0  # private variable (different name)
#
#     # Setter
#     def set_marks(self, value):   # parameter ka naam alag
#         self.__m = value
#
#     # Getter
#     def get_marks(self):
#         return self.__m
#
# s = Student()
#
# s.set_marks(90)
# print(s.get_marks())
#

class Student:

    def __init__(self):
        self.name = ""
        self.subject = ""
        self.roll = ""

    def __set__(self, name, subject, roll):
        self.n = name
        self.s = subject
        self.r = roll

    def get__name(self):
        return self.n

    def get__subject(self):
        return self.s

    def get__roll(self):
        return self.r

    s = Student()

    s.set_name(nitin )
    print(s.get__name)
