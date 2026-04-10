import  datetime

x =datetime.date.today()

formated = x .strftime("%d-%m-%y")


print("Formatted date is :", formated)