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

#base class
class Vehicle:
    pass

#first level subclasses
class FlightVehicle(Vehicle):
    pass

class GroundVehicle(Vehicle):
    pass

#second level subclasses from ground vehicle
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

#second level subclasses from Flight Vehicle
class Airplane(FlightVehicle):
    pass

class Starship(FlightVehicle):
    pass