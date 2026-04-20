from abc import ABC, abstractmethod


class Shape(ABC):

    def execute(self):
        self.area()

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        rectangle_area = self.length * self.width
        print("Rectangle  area :", rectangle_area)
        return rectangle_area


#
# # Example usage
r = Rectangle(5, 10)
r.execute()
# # Polymorphism: Shape type reference holding Rectangle object
# shape: Shape = Rectangle(5, 10)
# shape.execute()

#################################################################################################################
from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


# Child class
class Dog(Animal):
    def make_sound(self):
        return "Bark"


# Another child class
class Cat(Animal):
    def make_sound(self):
        return "Meow"


# Using the classes
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Bark
print(cat.make_sound())  # Meow

