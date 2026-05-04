import re

import os


def readLine():
    input_file = open("C:\\Users\\DOS\\OneDrive\\Desktop\\mix gmail.txt", 'r')

    outlook_file = open("C:\\Users\\DOS\\OneDrive\\Desktop\\outlook.com.txt", "w")
    yahoo_file = open("C:\\Users\\DOS\\OneDrive\\Desktop\\yahoo.com.txt", "w")
    gmail_file = open("C:\\Users\\DOS\\OneDrive\\Desktop\\gmail.com.txt", "w")

    for line in input_file:
        if (re.search("gmail.com", line)):
            gmail_file.write(line)
        if (re.search("outlook.com", line)):
           outlook_file.write(line)
        if (re.search("yahoo.com", line)):
           yahoo_file.write(line)

        print(line)
    input_file.close()
    outlook_file.close()
    yahoo_file.close()
    gmail_file.close()

    readLine()
