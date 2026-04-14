# class Shape:
#     def __init__(self, color, borderWidth):
#         self.color = color
#         self.borderWidth = borderWidth
#
#
#
#     def setColor(self, c):
#         self.color = c
#
#     def getColor(self):
#         return self.color
#
#     def setBorderWidth(self, borderWidth):
#         self.borderWidth = borderWidth
#
#     def getBorderWidth(self):
#         return self.borderWidth
#
#
# s = Shape("Red", 5)
#
# print(f"Color:", s.getColor())
# print(f"BorderWidth:", s.getBorderWidth())
#
# # by Set Get Method
# s.setColor("Blue")
# s.setBorderWidth(10)
# print("Color:", s.getColor())  # Blue
# print("BorderWidth:", s.getBorderWidth())


##################################################################################################################

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

s = Student("Amit", 20)
s.show()










