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

class Vehicle:		# Base for Everything
	pass

class GroundVehicle(Vehicle):		# Base for Car and Motorcycle, child of Vehicle
	pass

class Car(GroundVehicle):			# Child of GroundVehicle and Grandchild of Vehicle
	pass

class Motorcycle(GroundVehicle):		# Child of GroundVehicle and Grandchild of Vehicle
	pass

class FlightVehicle(Vehicle):		# Base for Airplane and Child of Vehicle
	pass

class Airplane(FlightVehicle):		# Child of FlightVehicle and Grandchild of Vehicle
	pass

class Starship(FlightVehicle): 	# Child of FlightVehicle and Grandchild of Vehicle
	pass