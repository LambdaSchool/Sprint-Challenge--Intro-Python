import unittest
import oop1


# used this as reference: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
class TestOop1(unittest.TestCase):
    def test_vehicle(self):
        """ Does the Vehicle class exist? """
        try:
            self.test = oop1.Vehicle()
            self.assertIsInstance(self.test, oop1.Vehicle)
            print("\nVehicle Class Exists\n")
        except NameError as e:
            print(e)

    def test_flight_vehicle(self):
        """ Does the FlightVehicle class exist? """
        try:
            self.test = oop1.FlightVehicle()
            self.assertIsInstance(self.test, oop1.FlightVehicle)
            print("\nFlightVehicle Class Exists\n")
        except NameError as e:
            print(e)


if __name__ == '__main__':
    unittest.main()