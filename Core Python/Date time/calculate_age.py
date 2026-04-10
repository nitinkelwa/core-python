import datetime

dob = datetime.date(2002, 6, 8)
today = datetime.date.today()

age = today.year - dob.year


# Day name of DOB
day_name = dob.strftime("%A")

print("Your age is:", age)
print("You were born on:", day_name)