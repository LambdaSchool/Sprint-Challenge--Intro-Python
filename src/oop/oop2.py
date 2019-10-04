# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    def drive(self, sound="vroooom"):
        self.sound = sound
        return sound

    def __repr__(self):
        return sound

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle): # Vehicle based
    def __init__(self, num_wheels=2):
        super().__init__(num_wheels)
    
    def drive(self, sound="BRAAAP!!"):
        self.sound = sound
        return sound

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

results = [print(vehicle.drive()) for vehicle in vehicles]
results
