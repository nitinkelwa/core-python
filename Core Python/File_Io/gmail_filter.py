import re
#import os


def readline():

    input_file = open("C:\\Users\\DOS\\OneDrive\\Desktop\\correct.txt","r")

    gmail_file = open("C:\\Users\\DOS\\OneDrive\\Desktop\\gmail.txt", "w")
    yahoo_file = open("C:\\ Users \\DOS\\OneDrive\\Desktop\\yahoo.txt", "w")
    outlook_file = open("C:\\ Users \\DOS\\OneDrive\\Desktop\\ outlook.txt", "w")

    for line in input_file:
        if re.search("@gmail.com", line):
            gmail_file.write(line)

        if re.search("@yahoo.com", line):
            yahoo_file.write(line)

        if re.search("@outlook.com", line):
            outlook_file.write(line)

        print(line)
    input_file.close()
    gmail_file.close()
    yahoo_file.close()
    outlook_file.close()


readline()
