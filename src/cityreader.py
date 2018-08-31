import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.

# TODO

class City:
    def __init__(self, name, lat, lon, pop):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.pop = pop

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

# Print the list of cities (name, lat, lon), 1 record per line.

with open('src/cities.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        cities.append(City(row[0], row[3], row[4], row[5]))

# TODO

for city in cities:
    print('\n' + city.name + ' is located at the following coordinates:' + ' ' + str(city.lat) + ', ' + str(city.lon) + ' and has a population of ' + str(city.pop) + '.')

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

while True:

    print("\nEnter two points on the map, each specified by latitude\nand longitude. These points will form a square, and\nthe cities with 750,000 or more people will be listed.")
    pt1 = (input('\nEnter first coordinates (ex. 45, -100): '))
    pt2 = (input('Enter second coordinates (ex. 32, -120): '))

    if len(pt1) or len(pt2) != 2:

        print ("\nPlease enter latitude and longitude (ex. 35, -107 or 41, -112).")

    lat1 = pt1.split(", ")[0]
    lon1 = pt1.split(", ")[1]
    lat2 = pt2.split(", ")[0]
    lon2 = pt2.split(", ")[1]

    # if lat2 < lat1:
    #     lat1, lat2 = lat2, lat1
    #     lat2 = lat1
    # if lon2 < lon1:
    #     lon1, lon2 = lon2, lon1

    print(lat1)
    print(lon1)
    print(lat2)
    print(lon2)
        
    print("\nThe following cities with 750,000 or more people are in the specified area.\n")
    for city in cities:
        if city.lat >= lat1 and city.lat <= lat2 and city.lon >= lon1 and city.lon <= lon2:
            print(city.name + ':' + ' ' + str(city.lat) + ', ' + str(city.lon))