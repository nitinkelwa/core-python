# class Shape:
#     def __init__(self):
#         self.color = ''
#         self.borderWidth = 0
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
#     def __init__(self):
#         self.length = 0
#         self.width = 0
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
# r = Rectangle()
# r.setLength(10)
# r.setWidth(20)
# r.setColor("red")
# r.setBorderWidth(100)
#
# print("Length:", r.getLength())
# print("Width:", r.getWidth())
# print("Color:", r.getColor())
# print("Border Width:", r.getBorderWidth())


#####################################################################################################################


class Bank:


    def __init__(self):
        self.customer_name = ''
        self.account_number = 0

    def setCustomer_name(self, c):
        self.customer_name = c

    def getcustomer_name(self):
        return self.customer_name

    def setaccount_number(self, a):
        self.account_number = a

    def getaccount_number(self):
        return self.account_number


class Finance(Bank):
    def __init__(self):
        self.aadhar_number= 0
        self.pan_no = 0

    def setaadhar_number(self, b):
        self.aadhar_number = b

    def getaadhar_number(self):
        return self.aadhar_number

    def setpan_no(self, p):
        self.pan_no = p

    def getpan_no(self):
        return self.pan_no


f = Finance()
f.setaadhar_number(9314690000)
f.setpan_no("pub54661")
f.setCustomer_name("nitin")
f.setaccount_number(882410110001000)

print("customer name:",f.getcustomer_name())
print("account number:", f.getaccount_number())
print("aadhar number no:",f.getaadhar_number())
print("cutomer pan no:", f.getpan_no())
