# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle(object): # Vehicle is base class

    def __init__(self):
        pass
        # self.ground_vehicle = ground_vehicle
        # self.flight_vehicle = flight_vehicle

class GroundVehicle(Vehicle):

    def __init__(self):
        Vehicle.__init__(self)
        # self.car = car
        # self.motorcycle = motorcycle
        
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

class FlightVehicle(Vehicle):

    def __init__(self):
        Vehicle.__init__(self)

        # def __init__(self, starship, airplane):
        #     self.starship = starship
        #     self.airplane = airplane
        
class Starship(FlightVehicle):
    pass
class Airplane(FlightVehicle):
    pass
    

