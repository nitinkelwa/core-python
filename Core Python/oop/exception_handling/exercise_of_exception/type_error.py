a = 10
b = "5"

try:
    result = a + b
except TypeError as e:
    print("Type mismatch :", e)
