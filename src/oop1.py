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

# Vehicle is the base class

class Vehicle:
  def __init__(self, name):
    self.name = name

class GroundVehicle(Vehicle):
  def __init__(self, name):
    Vehicle.__init__(self, name)

class Car(GroundVehicle):
  def __init__(self, name):
    GroundVehicle.__init__(self, name)

class Motorcycle(GroundVehicle):
  def __init__(self, name):
    GroundVehicle.__init__(self, name)

# Vehicle is again the base class, here

class FlightVehicle(Vehicle):
  def __init__(self, name):
    Vehicle.__init__(self, name)

class Airplane(FlightVehicle):
  def __init__(self, name):
    FlightVehicle.__init__(self, name)
  
class Starship(FlightVehicle):
  def __init__(self, name):
    FlightVehicle.__init__(self, name)

