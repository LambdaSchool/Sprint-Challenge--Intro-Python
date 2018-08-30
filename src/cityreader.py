# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.
import csv

class City:
    def __init__(self,name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return "({}, {}, {})".format(self.name, self.latitude, self.longitude)

# TODO


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# Use Python's built-in "csv" module to read this file so that each record is
# imported into a City instance. (You're free to add more attributes to the City
# class if you wish, but this is not necessary.) Google "python 3 csv" for
# references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

cities = []
with open("cities.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)

    for row in reader:
        city = City(row[0], float(row[3]), float(row[4]))
        cities.append(city)
    # TODO

# Print the list of cities (name, lat, lon), 1 record per line.
for city in cities:
    print("{}, {}, {})".format(city.name, city.latitude, city.longitude))

# TODO

# *** STRETCH GOAL! ***
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Output the cities that fall
# within this square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO

lat1, long1 = input("Enter a latitude wand a longtitude to search for a city. Please seperate using a coma:").split(",")
lat2, long2 = input("Enter a latitude wand a longtitude to search for a city. Please seperate using a coma:").split(",")

lat1, long1 = float(lat1), float(long1)
lat2, long2 = float(lat2), float(long2)

#normalize inputs

if lat1 < lat2:
    lat1, lat2 = lat2, lat1
    long1, long2 = long2, long1

near = [city for city in cities if (lat1 > float(city.latitude) > lat2) and (long1 > float(city.longitude) > long2)]

for city in near:
    print("{}, {}, {})".format(city.name, city.latitude, city.longitude))
