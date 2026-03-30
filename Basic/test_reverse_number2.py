number = 1456
r = 0
rev = 0
n = number

while n > 0:
    r = n % 10
    rev = (rev * 10) + r
    n = n // 10

print('reverse number', rev)
