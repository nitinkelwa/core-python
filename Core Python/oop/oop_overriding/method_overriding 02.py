
#
# # Base class
# class Shape:
#     def execute(self):
#         print('Shape Execute Method')
#         self.area()  # Call the overridden method
#
#     def area(self):
#         print('Shape Area Method')  # Default behavior
#
#
# # Child class overriding area()
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         rectangle_area = self.length * self.width
#         print('Rectangle Area:', rectangle_area)
#         return rectangle_area
#
#
# # Another child class overriding area()
# class Circle(Shape):
#     PI = 3.14  # Class-level constant
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         circle_area = self.PI * self.radius * self.radius
#         print('Circle Area:', circle_area)
#         return circle_area
#
#
# # Child class without overriding area()
# class Test(Shape):
#     pass
#
#
# # Create objects and call execute()
# r = Rectangle(10, 20)
# r.execute()  # Should call Rectangle's area()
#
# c = Circle(10)
# c.execute()  # Should call Circle's area()
#
# t = Test()
# t.execute()  # Will call Shape's area() since Test does not override it
#

#######################################################################################################


class Animal:
    def speak(self):
        print("Animal makes a sound")

    def info(self):
        print("This is a general animal")


# Child class 1
class Dog(Animal):
    def speak(self):
        print("Dog barks")


# Child class 2
class Cat(Animal):
    def speak(self):
        print("Cat meows")


# Child class 3
class Cow(Animal):
    pass



def animal_sound(obj):
    obj.speak()
    obj.info()
    print("------")


# Creating objects
d = Dog()
c = Cat()
w = Cow()

animal_sound(d)
animal_sound(c)
animal_sound(w)

