text = input(" hello nitin : ")

count = 0
for ch in text:
    if ch.isalpha():
        count += 1

print("Total alphabets is =", count)
