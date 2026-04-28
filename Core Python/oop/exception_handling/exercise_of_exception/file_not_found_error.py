
try:
    f = open("file.txt")
except FileNotFoundError:
    print("File not found")