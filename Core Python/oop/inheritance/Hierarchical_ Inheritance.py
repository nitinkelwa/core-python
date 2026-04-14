# class Shape:
#     def __init__(self, color='', borderWidth=0):
#         self.color = color
#         self.borderWidth = borderWidth
#
#     def setColor(self, c):
#         self.color = c
#
#     def getColor(self):
#         return self.color
#
#     def setBorderWidth(self, bw):
#         self.borderWidth = bw
#
#     def getBorderWidth(self):
#         return self.borderWidth
#
#
# class Rectangle(Shape):
#     def __init__(self, length=0, width=0, color='', borderWidth=0):
#         self.length = length
#         self.width = width
#         super().__init__(color, borderWidth)
#
#     def setLength(self, l):
#         self.length = l
#
#     def getLength(self):
#         return self.length
#
#     def setWidth(self, w):
#         self.width = w
#
#     def getWidth(self):
#         return self.width
#
#
#
# class Circle(Shape):
#     def __init__(self, radius=0, color='', borderWidth=0):
#         self.radius = radius
#         super().__init__(color, borderWidth)
#
#     def setRadius(self, r):
#         self.radius = r
#
#     def getRadius(self):
#         return self.radius
#
# # Creating a Rectangle object
# r = Rectangle(10, 20, 'red', 100)
# print("Rectangle:")
# print("Length:", r.getLength())
# print("Width:", r.getWidth())
# print("Color:", r.getColor())
# print("Border Width:", r.getBorderWidth())
#
#
# # Creating a Circle object
# c = Circle(15, 'blue', 50)
# print("\nCircle:")
# print("Radius:", c.getRadius())
# print("Color:", c.getColor())
# print("Border Width:", c.getBorderWidth())
#
#
#
# ######################################################################################################################


# Parent class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

# Child class 1
class Manager(Employee):
    def work(self):
        print(f"{self.name} manages the team")

# Child class 2
class Developer(Employee):
    def work(self):
        print(f"{self.name} writes code")

# Child class 3
class Designer(Employee):
    def work(self):
        print(f"{self.name} designs UI")

# Creating objects
m = Manager("Nitin", 80000)
d = Developer("Pravin", 60000)
ds = Designer("Neha", 55000)

# Calling methods
m.show_details()
m.work()

d.show_details()
d.work()

ds.show_details()
ds.work()

















