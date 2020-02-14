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

class Vehicle:  #base
    def __init__(self):
        pass

class Ground_Vehicle(Vehicle):
    def __init__(self):
        pass

class Car(Ground_Vehicle):
    def __init__(self):
        pass

class Motorcycle(Ground_Vehicle):
    def __init__(self):
        pass


class Flight_Vehicle(Vehicle):
    def __init__(self):
        pass

class Airplane(Flight_Vehicle):
    def __init__(self):
        pass

class Starship(Flight_Vehicle):
    def __init__(self):
        pass
