# class Student:
#     def getStudent(self):
#         self.name = input("Name: ")
#         self.age = input("Age: ")
#         self.gender = input("Gender: ")
#
#
# class Test(Student):
#
#     def getMarks(self):
#         self.studentClass = input("Class: ")
#         print("Enter the marks of the respective subjects")
#         self.literature = int(input("Literature: "))
#         self.math = int(input("Math: "))
#         self.biology = int(input("Biology: "))
#         self.physics = int(input("Physics: "))
#
#
# class Marks(Test):
#     # Display student's information along with total marks
#     def display(self):
#         print("\n\nName:", self.name)
#         print("Age:", self.age)
#         print("Gender:", self.gender)
#         print("Class:", self.studentClass)
#         print("Literature:", self.literature)
#         print("Math:", self.math)
#         print("Biology:", self.biology)
#         print("Physics:", self.physics)
#         total_marks = self.literature + self.math + self.biology + self.physics
#         if total_marks > 100:
#             print("Passed")
#         else:
#             print("Failed")
#         print("Total Marks:", total_marks)
#
#
# # Create an object of Marks class
# m = Marks()
# #
# # # Collect student details
# m.getStudent()
# #
# # # Collect marks details
# m.getMarks()
# #
# # # Display all information
# m.display()


####################################################################################################################


class Person:

    print("fill this form............... ")

    def getdata(self):
        print("give me information about you")
        self.name = input("enter your first name:")
        self.last_name = input("enter your last name: ")
        self.mobile_no = int(input("write your mobile number here:"))
        self.address = input("where are you from:")
        print("")
        print("")


class Father(Person):

    def getinformation(self):
        print("father's details: ...............")

        self.father_name = input("enter your father name:")
        self.fathers_mobile_no = int(input("enter father mobile number: "))
        self.occupation = input("what is your father's occupation:")
        print("")
        print("")


class Mother(Father):

    def getdetails(self):
        print("mother's details: .......................")
        self.mother_name = input("enter your mother name: ")
        self.mothers_mobile_number = int(input("enter your mother mobile number:"))
        self.mother_occupation = input("what is your father's occupation:")
        print("")
        print("")


class Family(Mother):

    def display(self):
        print("name:", self.name)
        print("last name:", self.last_name)
        print("mobile number:", self.mobile_no)
        print("address:", self.address)
        print("your father name is :", self.father_name)
        print("your father mobile number:", self.fathers_mobile_no)
        print("your father work as a :  ", self.occupation)
        print("your mother name is:", self.mother_name)
        print("your mother's mobile number", self.mothers_mobile_number)
        print("your mother work as a", self.mother_occupation)




f = Family()

f.getdata()
f.getinformation()
f.getdetails()
f.display()

