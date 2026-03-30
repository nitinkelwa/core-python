# 1. write a program a to find a maximum of two number.

# a = 50
# b = 60
# if a >b:
#   print( "maximum numbre is ",a)

# else:
#   print ( 'maximum number is ',b)


# 2. find the smaller of two numbers using the conditional operator.

# a = 80
# b = 90
# print(" smaller number is ",a if a < b else b)


# 3. write a program to generate 5 random integer numbers between 1 to 100.


# import random

# for i in range(5):
#   num = random.randint(1, 100)
#  print(num)

# 4. write program to reverse digits of a given number.

# number = 483
# r = 0
# rev = 0
# n = number

# while n > 0:
#   r = n % 10
#  rev = (rev * 10) + r
# n=n//10

# print ('reverse number is ',rev)


# 5. write a program to find sum of all integer greater than 100 and less than 200 that are divisibele by 7.


sum = 0

#for i in range(101, 200):
 #   if i % 7 == 0:
  #      sum += i
   #     print(" Division By  7 NO ", i)

#print("Sum =", sum)

#write a program to generate a triangle .


rows = 4


for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()









