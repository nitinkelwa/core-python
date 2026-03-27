number = 154
n = number
r = 0
sum = 0
while n > 0:
    r = n % 10
    sum = sum + r * r * r
    n = n // 10

if sum == number:
    print('it is an armstrong number',sum)

else:
    print('it is not an armstrong number',sum)