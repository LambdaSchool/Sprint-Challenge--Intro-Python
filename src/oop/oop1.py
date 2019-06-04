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
class vehicle:
    pass
    # No Base Class
class FlightVehicle(vehicle):
    pass
    # Vehicle is Base Class
class Starship(FlightVehicle):
    pass
    # FlightVehicle is Base Class
class GroundVehicle(vehicle):
    pass
    # Vehicle is Base Class
class Airplane(FlightVehicle):
    pass
    # FlightVehicle is Base Class
class Car(GroundVehicle):
    pass
    # GroundVehicle is Base Class
class Motorcycle(GroundVehicle):
    pass
      # GroundVehicle is Base Class