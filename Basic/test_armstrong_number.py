number = 153
n = number
r = 0
sum = 0
while n > 0:
    r = n % 10  # r = 3 , r = 5 , r = 1
    sum = sum + r * r * r  # sum = 0+27 = 27 , 27+125 = 152 , 152+ 1 = 153

    n = n // 10

if sum == number:
    print('it is an armstrong number', sum)

else:
    print('it is not an armstrong number', sum)
