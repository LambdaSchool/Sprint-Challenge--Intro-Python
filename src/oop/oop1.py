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
# Base Class


class FlightVehicle(Vehicle):
    pass
    # base class for Airplane


class Airplane(FlightVehicle):
    pass


class Starship(FlightVehicle):
    pass


class GroundVehicle(Vehicle):
    pass
    # Base class for Car and Motorcycle


class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass
