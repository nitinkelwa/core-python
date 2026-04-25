class LoginException(Exception):

    def __init__(self, msg):
        super().__init__(msg)


login_id = "admin"
password = "admin"

try:
    if login_id == "admn" and password == "admin":
        print("valid user")

    else:
       raise LoginException("invalid user ")

except Exception as e:
    print("LoginException",e)
