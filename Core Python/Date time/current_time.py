import datetime

d = datetime.datetime.now()
print("The time is ", d)
print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.minute)
print(d.second)
print(d.microsecond)
print(d.strftime("%a %b,%d,%y"))
print(d.strftime("%y-%m-%d %H:%M:%S"))
print(d.strftime("%d-%m-%y %H:%M:%S"))
print(d.min)
print(d.max)

