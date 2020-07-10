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
    #This is the base class
    pass

class GroundVehicle(Vehicle):
    #subclass of Vehicle
    pass

class Car(GroundVehicle):
    #subclass of GroundVehicle
    pass

class Motorcycle(GroundVehicle):
    #subclass of GroundVehicle
    pass

class FlightVehicle(Vehicle):
    #subclass of Vehicle
    pass

class Airplane(FlightVehicle):
    #subclass of FlightVehicle
    pass

class Starship(FlightVehicle):
    #subclass of FlightVehicle
    pass