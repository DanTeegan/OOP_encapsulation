# Here we are creating a class called Airplane
class Airplane:

    # Here are the 2 variables of airplane. They are made private.
    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 185 # Private variable cannot be called.
        self.__name = "boeing plane" # Again the variable has been made private. it cannot be called.

    # Creating a method called drive
    def drive(self):
        print("Driving" + str(self.__maxspeed))

    # Creating a method called _aircon
    def _aircon(self):
        print("The aircon is on!")

# Here we are creating an object of airplane.
plane = Airplane()
plane._aircon()
plane.__maxspeed = 500 # cannot be called as we have used encapsulation (made it private)
plane.drive()