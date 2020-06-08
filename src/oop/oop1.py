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
    pass
# subclass of vehicle
class GroundVehicle(Vehicle):
    pass
# subclass of GroundVehicle
class Car(GroundVehicle):
    pass
# subclass of GroundVehicle
class Motorcycle(GroundVehicle):
    pass
# subclass of Vehicle
class FlightVehicle(Vehicle):
    pass
# subclass of FlightVehicle
class Starship(FlightVehicle):
    pass
# subclass of FlightVehicle
class Airplane(FlightVehicle):
    pass




