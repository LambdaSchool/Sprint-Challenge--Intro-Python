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
    def __init__(self): # base class
        pass

class GroundVehicle(Vehicle):
    def _init_(self): # base class
        pass

class Car(GroundVehicle):
    def _init_(self):
        pass

class Motorcycle(GroundVehicle):
    def _init_(self):
        pass

class FlightVehicle(Vehicle):
    def __init__(self): # base class
        pass

class Starship(FlightVehicle):
    def __init__(self):
        pass

class Airplane(FlightVehicle):
    def __init__(self):
        pass


