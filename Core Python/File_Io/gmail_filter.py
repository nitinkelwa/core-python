import re #  (regular expression) = kisi pattern ko found krne ke liye use krte he
import os #  (operating system) = kisi file ko system se delete krna update krna  ya  file ka path use krne ke liye os import krte he .


def readline():  # function.

    input_file =  open("C:\\Users\\DOS\\OneDrive\\Desktop\\correct.txt.txt","r") # kha se hume read krwana he.

    gmail_file = open("C:\\Users\\DOS\\OneDrive\\Desktop\\gmail.txt.txt", "w") # jha hume print write krna he .
    yahoo_file = open("C:\\Users\\DOS\\OneDrive\\Desktop\\yahoo.txt.txt", "w")
    outlook_file = open("C:\\Users\\DOS\\OneDrive\\Desktop\\outlook.txt.txt", "w")

    for line in input_file:                            # jo line read kr rha he wo line me store ho rhi he
        if( re.search("@gmail.com", line)):     # kisi bhi pattern ko research krega jese gmail.com to line me store hoga .
            gmail_file.write(line)                      # agar gmail.com vala pattern mila to use gmail_file me write krega .

        if (re.search("@yahoo.com", line)):      #  " " "
            yahoo_file.write(line)

        if (re.search("@outlook.com", line)):    # " " " "
            outlook_file.write(line)


    input_file.close()                                    # kisi file ko open kiya he to use close krna padega .
    gmail_file.close()
    yahoo_file.close()
    outlook_file.close()
print("gmail filter kr di gyi he 👍")                             # hume pta rhe ki program proper execute hua he bina error ke.

readline()
