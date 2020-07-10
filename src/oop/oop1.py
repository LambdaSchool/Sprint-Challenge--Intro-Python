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


class Vehicle:
    # Base class for all other vehicles
    pass


class FlightVehicle(Vehicle):
    # Base class for all flight vehicles (starship, airplane)
    # inherits from vehicle
    pass


class Starship(FlightVehicle):
    pass


class Airplane(FlightVehicle):
    pass


class GroundVehicle(Vehicle):
    # Base class for all ground vehicles (car, motorcycle)
    # inherits from vehicle
    pass


class Motorcycle(GroundVehicle):
    pass


class Car(GroundVehicle):
    pass
