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

class Vehicle:   #Base Class
    pass

    #inherits from vehicle class
class FlightVehicle(Vehicle):   
    pass

class GroundVehicle(Vehicle):
    pass
   
    #inherits from flight vehicle class
class Starship(FlightVehicle):  
    pass

class Airplane(FlightVehicle):
    pass

    #inherits from ground vehicle class
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass


