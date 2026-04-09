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

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))
print("")
print("")
print("")

if (a >= b and a >= c):
    print("1st number is largest :", a)

elif (b >= c):
    print("2nd number is largest  :", b)

else:
    print("3rd number is largest  :", c)
