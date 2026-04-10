class Automobile:
    def __init__(self):
        print("Details of my car  Mahendra scorpio ")

        self.model = "model"
        self.colour = "colour"
        self.speed = "speed"
        self.gear = "gear"

        # setter getter for model

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model


  # setter and getter for colour

    def set_colour(self, colour):
        self.colour = colour

    def get_colour(self):
        return self.colour


    # setter and getter for  speed

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed


    # setter and getter for gear

    def set_gear(self, gear):
        self.gear = gear

    def get_gear(self):
        return self.gear


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






