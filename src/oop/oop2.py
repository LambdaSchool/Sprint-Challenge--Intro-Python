# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels = 4): # only works for immutable (cant change) variables otherwise use []
        self.num_wheels = num_wheels

    # TODO
    def drive(self):
        return "vroooom"

# Subclass Motorcycle from GroundVehicle. (motorcycle in groundvehicle)
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels = 2): # set number, doesn't change for now (why do we need __ instead of _?)
        self.num_wheels = num_wheels # because it is a special defined method in python. it is used when an object is created from a class
# TODO                                 # and used to initialize the attributes of said class
    def drive(self):
        return "BRAAAP!!"

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.
# through the vehicles list = for loop 
# vehicle = groundvehicle = car 
# vehicles = list
# call drive on each , attach drive to vehicle on the end
# TODO

for vehicle in vehicles:
    print (vehicle.drive())
