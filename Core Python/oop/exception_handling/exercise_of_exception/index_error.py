a = [1, 2, 3]

try:
    a = [1, 2, 3]
    print(a[5])
except IndexError:
    print("Index out of range")
