# class Shape:
#     def area(self):
#          print("Shape Area......")
#          return print("Shape class area method")
#
#
# class Rectangle(Shape):
#     def area(self):
#         print("Rectangle Area......")
#         return print("Rectangle class area method")
#
#
#
#
# r = Rectangle()
# r.area()
#
#
# s = Shape()
# s.area()
#
# shape: Shape = Rectangle()
# shape.area()


###########################################################################################################

class Employee:
    def work(self):
        print("Employee is working")


class Manager(Employee):
    def work(self):
        print("Manager is managing team")


e = Employee()
e.work()

m = Manager()
m.work()

Employee: Employee = Manager()
Employee.work()
