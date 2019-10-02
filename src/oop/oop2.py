# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels):
    def __init__(self, num_wheels = 4):
        self.num_wheels = num_wheels

    # TODO
    def drive(self):
        return "vroooom"


# Subclass Motorcycle from GroundVehicle.
@@ -17,7 +18,12 @@ def __init__(self, num_wheels):
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# TODO
class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels = 2):
        super().__init__(num_wheels)

    def drive(self):
        return "BRAAAP!!"

vehicles = [
    GroundVehicle(),
# Go through the vehicles list and print the result of calling drive() on each.

# TODO
