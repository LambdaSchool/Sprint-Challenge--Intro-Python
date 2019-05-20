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

#connect vehicle to flight vehicle 

class FlightVehicle(Vehicle):
  pass

#connect starship to flight vehicle

class Starship(FlightVehicle):
  pass

#connect airplane to flight vehicle

class Airplane(FlightVehicle):
  pass

#connect ground vehicle to vehicle

class GroundVehicle(Vehicle):
  pass

#connect car to ground vehicle
class Car(GroundVehicle):
  pass

#connect motorcycle to ground vehicle
class Motorcycle(GroundVehicle):
  pass