# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

import csv


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        # I'm using __repl__ because it gives the human readable output,
        # not necessarily just a string as is seen in __str__.
        return f'City("{self.name}", {self.lat}, {self.lon})'

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu
# for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

# This is our empty list to populate.
cities = []


def cityreader(cities=[]):
    with open('cities.csv', newline='') as csvfile:  # Opening the CSV file.
        # We don't need to specify a delimiter; read the file w/ csv reader.
        readfile = csv.reader(csvfile)
        next(readfile)  # Skip the row containing column labels.
        for row in readfile:  # For every row in the readfile...
            cities.append(City(row[0], float(row[3]), float(row[4])))  # Append
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c.name, c.lat, c.lon)
    # Alternatively, with the way I have __repr__ setup, one could simply use:
    # print(c) however this prints in a fashion more representative of the
    # objective here.

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the
# `cityreader` function. This function should output all the cities that
# fall within the coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates.
# Hint: normalize the input data so that it's always one or the other,
# then search for cities. In the example below, inputting 32, -120 first
# and then 45, -100 should not change the results of what the
# `cityreader_stretch` function returns.
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

# TODO Get latitude and longitude values from the user
lat1 = input('Enter Latitude #1: ')  # Accept lat1 input.
lon1 = input('Enter Longitude #1: ')  # Accept lon1 input.
lat2 = input('Enter Latitude #2: ')  # Accept lat2 input.
lon2 = input('Enter Longitude #2: ')  # Accept lon2 input.


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # TODO Ensure that the lat and lon valuse are all floats
    # within will hold the cities that fall within the specified region
    # Go through each city and check to see if it falls within
    # the specified coordinates.
    within = []  # Empty list to populate.
    for city in cities:  # For each city in cities...
        # Check if the city is within the specified lat/lon.
        # This will need to be done in two separate if statements
        # to ensure that the appropriate cities are appended to
        # our within list, regardless of order.
        if ((float(city.lat) < float(lat1)) &
            (float(city.lat) > float(lat2)) &
            (float(city.lon) < float(lon1)) &
                (float(city.lon) > float(lon2))):
                # And append it if so.
                    within.append(city)
        elif ((float(city.lat) > float(lat1)) &
              (float(city.lat) < float(lat2)) &
              (float(city.lon) > float(lon1)) &
                (float(city.lon) < float(lon2))):
                # And append it if so.
                    within.append(city)
    return within

# This will print cities within the range of coordinates user specified.
for city in cityreader_stretch(lat1, lon1, lat2, lon2, cities=cities):
    print(city)
