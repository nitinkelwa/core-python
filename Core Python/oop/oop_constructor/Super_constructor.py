#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# # Child class
# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(name)  # calling parent constructor
#         self.age = age
#
#     def show(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#
#
# s = Student("Amit", 20)
# s.show()


#############################################################################################################

class Collage:
    def __init__(self, cname):
        self.collage_name = cname


class Student(Collage):
    def __init__(self, cname,name  ):
        super().__init__(cname)
        self.student_name = name

    def show(self):
        print(f"collage name: {self.collage_name} \nStudent name: {self.student_name}")


s = Student("svce", "Nitin")
s.show()
