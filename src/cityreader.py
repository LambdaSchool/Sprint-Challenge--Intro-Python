import csv
# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# Use Python's built-in "csv" module to read this file so that each record is
# imported into a City instance. (You're free to add more attributes to the City
# class if you wish, but this is not necessary.) Google "python 3 csv" for
# references and use your Google-fu for other examples.
#


temp = []


with open('cities.csv', newline='') as csvfile:
    c = csv.reader(csvfile)
    for row in c:
        temp.append(row)

temp.pop(0)
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

cities = [City(city[0], city[3], city[4]) for city in temp]

# TODO

# Print the list of cities (name, lat, lon), 1 record per line.
for city in cities:
    print(city.name, city.lat, city.lon)

# TODO

# *** STRETCH GOAL! ***
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Output the cities that fall
# within this square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other (what is latMin, latMax?)
# then search for cities.
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

l1 = input('Enter lat1,lon1:\n').split(',')
l2 = input('Enter lat2,lon2:\n').split(',')
lat_min = min(float(l1[0]), float(l2[0]))
lat_max = max(float(l1[0]), float(l2[0]))
lon_min = min(float(l1[1]), float(l2[1]))
lon_max = max(float(l1[1]), float(l2[1]))

for city in cities:
    if lat_min <= float(city.lat) <= lat_max and lon_min <= float(city.lon) <= lon_max:
        print(f'{city.name}: {city.lat}, {city.lon}')
