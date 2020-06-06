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
class Vehicle():
    pass
class FlightVehicle(Vehicle):
    # we pass Vehicle Class as direct base class
    pass

class Starship(FlightVehicle):
     # we pass FlightVehicle Class as direct parent class
    pass

class Airplane(FlightVehicle):
     # we pass FlightVehicle Class as direct parent class
    pass

class GroundVehicle(Vehicle):
    # we pass Vehicle Class as direct base class
    pass

class Car(GroundVehicle):
     # we pass GroundVehicle Class as direct parent class
    pass

class Motorcycle(GroundVehicle):
     # we pass GroundVehicle Class as direct parent class
    pass
