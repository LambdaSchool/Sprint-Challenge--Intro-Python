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

class Vehicle:  # baseclass
    pass

class FlightVehicle(Vehicle):  # baseclass for Starship
    pass

class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass

class GroundVehicle(Vehicle):  # baseclass for Car & Motorcycle
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
