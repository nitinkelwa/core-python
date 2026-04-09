class Bank:
    def __init__(self):
        print("Details about customer ")

        self.customer_name = ''
        self.account_number = 0
        self.address = ''
        self.ifsc_code = ''

        # setter $ getter for name

    def getcustomer_name(self):
        return self.customer_name

    def setcustomer_name(self, customer_name):
        self.customer_name = customer_name

        # setter and getter for account number

    def getaccount_number(self):
        return self.account_number

    def setaccount_number(self, account_number):
        self.account_number = account_number

    # setter and getter for  address
    def getaddress(self):
        return self.address

    def setaddress(self, address):
        self.address = address

    # setter and getter for ifsc code
    def getifsc_code(self):
        return self.ifsc_code

    def setifsc_code(self, ifsc_code):
        self.ifsc_code = ifsc_code




class Finance(Bank):

    def __init__(self):
        self.aadhar_no = 0
        self.pan_no = 0

        # setter and getter for aadhar no

    def setaadhar_no(self, a):
        self.aadhar_no = a

    def getaadhar_no(self):
        return self.aadhar_no

    # setter getter for pan no

    def setpan_no(self, p):
        self.pan_no = p

    def getpan_no(self):
        return self.pan_no

b1 = Bank()
b1.setcustomer_name("Nitin ")
b1.setaccount_number("882410110000")
b1.setaddress("Memdi")
b1.setifsc_code("Bkid00088")




print("customer name : ", b1.getcustomer_name())
print("customer account number:", b1.getaccount_number())
print("customer address: ", b1.getaddress())
print(" customer ifsc code : ", b1.getifsc_code())


