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

# Base Class

class Vehicle:
  pass

#Type of Vehicle -- Children of Vehicle

class GroundVehicle(Vehicle):
  pass

class FlightVehicle(Vehicle):
  pass

# Type of Ground Vehicles (children)

class Car(GroundVehicle):
  pass

class Motorcycle(GroundVehicle):
  pass

# Type of flight vehicles 

class Airplane(FlightVehicle):
  pass

class Starship(FlightVehicle):
  pass