# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

import csv


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f'{self.name}: {self.lat}, {self.lon}'

        # We have a collection of US cities with population over 750,000 stored in the
        # file "cities.csv". (CSV stands for "comma-separated values".)
        #
        # In the body of the `cityreader` function, use Python's built-in "csv" module
        # to read this file so that each record is imported into a City instance. Then
        # return the list with all the City instances from the function.
        # Google "python 3 csv" for references and use your Google-fu for other examples.
        #
        # Store the instances in the "cities" list, below.
        #
        # Note that the first line of the CSV is header that describes the fields--this
        # should not be loaded into a City object.


cities = []


def cityreader(cities=[]):
    with open('cities.csv', 'r') as csv_archive:
        csv_reader = csv.reader(csv_archive)
        next(csv_reader)

        for city in csv_reader:
            cities.append(City(city[0], float(city[3]), float(city[4])))
        return cities

    # TODO Implement the functionality to read from the 'cities.csv' file
    # For each city record, create a new City instance and add it to the
    # `cities` list


cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(f'{c.name}, {c.lat}, {c.lon} \n')

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
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


# Step 1 - get values from user. Separate those values into usable pieces of data.

user_input = input(
    "Input coordinates as demonstrated in the example (lat1, lon1, lat2, lon2): ").split(',')


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region

    # TODO Ensure that the lat and lon values are all floats
    # Go through each city and check to see if it falls within
    # the specified coordinates.

    # Step 2 - Define the pieces of data from the user as floats to permit using decimals.
    lat1 = float(lat1)
    lon1 = float(lon1)

    lat2 = float(lat2)
    lon2 = float(lon2)

#     Rethink what you're doing with step 3 here. Consider the problem within the scope of what you've got set - up already.
#       So, given lat and lon as float values as well as a list of cities[objects]. How could you check whether just a single city object
#       can fit within the boundaries provided?

    # Step 3 - instantiate lists of the biggest and smallest values provided by the user.
    biggest = []
    smallest = []

    try:
        if lat1 > lat2:
            biggest.append(lat1)
            smallest.append(lat2)
        else:
            biggest.append(lat2)
            smallest.append(lat1)

        if lon1 > lon2:
            biggest.append(lon1)
            smallest.append(lon2)
        else:
            biggest.append(lon2)
            smallest.append(lon1)

        print(biggest)
        print(smallest)

    except Exception as error:
        print('error type: ', type(error))
        print('error args: ', error.args)

    # Step 4 - set up a list comprehension that will capture names of cities
    #   if their latitudes and longitudes are within the values provided by the user.

    # within = [city for city in cities if (city.lat > smallest[0] and city.lat <
    #                                       biggest[0]) and (city.lon > smallest[1] and city.lon < biggest[1])]

    within = [city for city in cities if (smallest[0] < city.lat < biggest[0]) and (
        smallest[1] < city.lon < biggest[1])]

    if (len(within) > 1):
        for item in within:
            print(item)

    return within


cityreader_stretch(user_input[0], user_input[1],
                   user_input[2], user_input[3], cities)
# Jacksonville, 30.3322, -81.6749

# Albuquerque, 35.1055, -106.6476


# 35.1055, -106.6476, 30.3322, -81.6749
