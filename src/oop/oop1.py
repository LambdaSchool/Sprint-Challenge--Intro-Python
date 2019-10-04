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

# this class is the base class
class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f'{self.name}: and is {self.color}'


# this is a child of the vehcile class
class FlightVehicle(Vehicle):
    def __init__(self, name, color, size):
        super().__init__(name, color)
        self.size = size

    def __str__(self):
        return f'{self.name} is this size: {self.size}'

# this is a child of flightvehicle
class Airplane(FlightVehicle):
    def __init__(self, name, color, size, speed, cargo_space):
        super().__init__(name,color,size)
        self.speed = speed
        self.cargo_space = cargo_space

    def __str__(self):
        return f'{self.name} is {self.color} color is {self.size} large can go {self.speed} fast and can hold {self.cargo_space} space.'

# this is a child of flightvehicle
class Starship(FlightVehicle):
    def __init__(self,name,color,size, parsecs, main_hull_material):
        super().__init__(name,color,size)
        self.parsecs = parsecs
        self.main_hull_material = main_hull_material

    def __str__(self):
        return f'{self.name} has a color of {self.color} is {self.size} large can go {self.parsecs} fast and is made out of {self.main_hull_material}.'

# child of vehicle
class GroundVehicle(Vehicle):
    def __init__(self, name,color,size):
        super().__init__(name,color)
        self.color = color
        self.size = size

    def __str__(self):
        return f'{self.name} is {self.color} color and is {self.size} large.'
    def 

# child of ground vehicle
class Car(GroundVehicle):
    def __init__(self, name, color, size, wheels, doors, speed):
        super().__init__(name, color, size)
        self.wheels = wheels
        self.doors = doors
        self.speed = speed

    def __str__(self):
        return f'{self.name} has color of {self.color} is {self.size} large can go {self.speed} fast has {self.wheels} amount of wheels and {self.doors} amound of doors'

# child of ground vehicle
class Motorcycle(GroundVehicle):
    def __init__(self, name, color, size, wheels, speed):
        super().__init__(name, color, size)
        self.wheels = wheels
        self.speed = speed

    def __str__(self):
        return f'{self.name} has color of {self.color} is {self.size} large can go {self.speed} fast has {self.wheels} amount of wheels'
