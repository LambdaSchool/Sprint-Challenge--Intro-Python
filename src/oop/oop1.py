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
    def __init__(self, wheels=4, doors=2):
        self.wheels = wheels
        self.doors = doors
    def __repr__(self):
        return self.wheels, self.doors

class GroundVehicle(Vehicle): # Vehicle based
    def __init__(self, wheels=4, doors=2, cylinders=4):
        super().__init__(wheels, doors)
        self.cylinders = cylinders

class Motorcycle(GroundVehicle): # GroundVehicle based
    def __init__(self, wheels=2, doors=0, cylinders=2, hp=10):
        super().__init__(wheels, doors, cylinders)
        self.hp = hp

class Car(GroundVehicle): # GroundVehicle based
    def __init__(self, wheels=4, doors=4, cylinders=4, engine=1):
        super().__init__(wheels, doors, cylinders)
        self.engine = engine

class FlightVehicle(Vehicle): # Vehicle based
    def __init__(self, wheels=2, doors=1, propellers=4):
        super().__init__(wheels, doors)
        self.propellers = propellers

class Airplane(FlightVehicle): # FlightVehicle based
    def __init__(self, wheels=2, doors=1, propellers=4, wings=2):
        super().__init__(wheels, doors, propellers)
        self.wings = wings

class Starship(FlightVehicle): # FlightVehicle based
    def __init__(self, wheels=0, doors=2, propellers=12, laser_guns=24):
        super().__init__(wheels, doors, propellers)
        self.laser_guns = laser_guns