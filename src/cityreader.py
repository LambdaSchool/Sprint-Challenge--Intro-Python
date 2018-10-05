import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.

# TODO
class City:
    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lng = lng

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

# TODO
with open("./src/cities.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for line in reader:
        cities.append(line)

# print(cities)
# Print the list of cities (name, lat, lon), 1 record per line.
for city in cities:
    print(city[0], city[3], city[4])
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
class Coords:
    def __init__(self, lat, lng):
        self.lat = float(lat)
        self.lng = float(lng)

coords1 = Coords(input("Please enter starting latitude => "),input("Please enter starting longitude => "))
coords2 = Coords(input("Please enter ending latitude => "),input("Please enter ending longitude => "))

for line in cities:
    if float(line[3]) >= coords1.lat and float(line[3]) <=coords2.lat:
        if float(line[4]) > coords1.lng and float(line[4]) < coords2.lng:
            print(f"{line[0]}: {line[3]},{line[4]}")
