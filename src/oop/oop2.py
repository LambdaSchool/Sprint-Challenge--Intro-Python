# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels = 4):
        self.num_wheels = num_wheels

    def __repr__(self):
        print(f"This vehicle has " + str(self.num_wheels) +  " wheels.")   

    def drive(self):
        return "vroooom"    

    # TODO


## When I print these I get a third print in the middle of them that says None, what does that refer to?
gv = GroundVehicle(6)
print(gv.__repr__())
print(gv.drive())



# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels = 4):
        GroundVehicle.__init__(self, num_wheels = 2)

    def drive(self):
        return "BRAAAP!!"


m = Motorcycle()
print(m.__repr__())
print(m.drive())

# TODO

# vehicles = [
#     GroundVehicle(),
#     GroundVehicle(),
#     Motorcycle(),
#     GroundVehicle(),
#     Motorcycle(),
# ]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO
