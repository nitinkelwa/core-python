num = 121

original = num
reverse = 0

while num > 0:
    r = num % 10
    reverse = reverse * 10 + r
    num = num // 10

if original == reverse:
    print(original, "is Palindrome")
else:
    print(original, "is Not Palindrome")