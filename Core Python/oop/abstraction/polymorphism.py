


class Dog:

    def sound(self):
        print("Dog is barks")


class Cow:

    def sound(self):
        print("cow is moo")


class Cat:

    def sound(self):
        print("cat is meow")


animals = (Dog(), Cow(),Cat() )

for a in animals:
    a.sound()


    ######################################################################################################
#
# class India:
#
#     def country(self):
#         print("india is an country")
#
#     def language(self):
#         print("india has many languages ")
#
#     def culture(self):
#         print("india has a rich culture")
#
#
# class Usa:
#
#     def country(self):
#         print("usa is a country")
#
#     def language(self):
#         print("language of usa is english ")
#
#     def culture(self):
#         print("usa has a rich culture")
#
#
# ind=India()
# usa=Usa()
#
# for con in (ind,usa):
#
#     con.country()
#     con.culture()
#     con.language()



