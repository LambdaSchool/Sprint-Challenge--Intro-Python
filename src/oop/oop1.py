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

#Base class
class Vehicle:
    # def __init__(self, year, make):
    #     self.year = year
    #     self.make = make
    pass

#Inherits from Vehicle
class FlightVehicle(Vehicle):
    # def __init__(self, year, make, wings):
    #     super().__init__(year, make)
    #     self.wings = wings
    pass

#Inherits from FlightVehicle
class Starship(FlightVehicle):
    # def __init__(self, year, make, wings):
    #     super().__init__(year, make, wings)
    pass

#Inherits from vehicle
class GroundVehicle(Vehicle):
    # def __init__(self, year, make, wheels):
    #     super().__init__(year, make)  
    #     self.wheels = wheels
    pass

#Inherits from flight vehicle
class Airplane(FlightVehicle):
    # def __init__(self, year, make, wings, cabin):
    #     super().__init__(year, make, wings)
    #     self.cabin = cabin 
    pass             

#Inherits from GroundVehicle
class Car(GroundVehicle):
    # def __init__(self, year, make, wheels):
    #     super().__init__(year, make, wheels)
    pass  

#Inherits from GroundVehicle
class Motorcycle(GroundVehicle):
    # def __init__(self, year, make, wheels):
    #     super().__init__(year, make, wheels)
    pass

