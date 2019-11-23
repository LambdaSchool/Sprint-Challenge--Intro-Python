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


#Base Class
class Vehicle (object):
    #constructor
    pass
    

class FlightVehicle (Vehicle):
    #constructor
    pass

class Starship (FlightVehicle):
#constructor
    pass

class GroundVehicle(Vehicle):# Constructor 
    pass

class Airplane(FlightVehicle):# Constructor 
    pass
        
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass
