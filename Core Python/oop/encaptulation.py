class Automobile:
    def __init__(self):
        print("Details of my car  Mahendra scorpio ")

        self.__model = None
        self.__colour = None
        self.__speed = 0
        self.__gear = 0

        # setter getter for model

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

        # setter and getter for colour

    def get_colour(self):
        return self.__colour

    def set_colour(self, colour):
        self.__colour = colour

    # setter and getter for  speed
    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    # setter and getter for gear
    def get_gear(self):
        return self.__gear

    def set_gear(self, gear):
        self.__gear = gear

    # object creation


car = Automobile()
car.set_model(" Mahendra scorpio s11")
car.set_colour(" Dark Black")
car.set_speed("160/170 km/h")
car.set_gear("5+Reverse ")

print("car model: ", car.get_model())
print("car colour:", car.get_colour())
print("car speed: ", car.get_speed())
print("No of gear in car: ",car.get_gear())






