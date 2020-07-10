# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return "{self.name}, {self.lat}, {self.lon}".format(self=self)

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
    with open("cities.csv", newline="") as csvfile:
        next(csvfile)
        for line in csvfile:
            city_info = line.split(",")
            cities.append(City(city_info[0], float(city_info[3]), float(city_info[4])))
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

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

first_point = input("Please input the first latitude and longitude separated by commas: ").split(",")
second_point = input("Please input the second latitude and longitude separated by commas: ").split(",")

try:
    first_lat = first_point[0].strip()
    first_lon = first_point[1].strip()
    second_lat = second_point[0].strip()
    second_lon = second_point[1].strip()
except IndexError:
    print("ERROR: Did not input proper latitude and longitude")
    exit(-1)


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    within = []

    lat1 = float(lat1)
    lon1 = float(lon1)
    lat2 = float(lat2)
    lon2 = float(lon2)

    # Find out which lat/lon combo is on the left
    if lon1 < lon2:
        left_lat = lat1
        left_lon = lon1
        right_lat = lat2
        right_lon = lon2
    else:
        left_lat = lat2
        left_lon = lon2
        right_lat = lat1
        right_lon = lon1

    # Find out if is top left or bottom left
    if left_lat < right_lat:
        for city in cities:
            city_lat = city.lat
            city_lon = city.lon
            if left_lat < city_lat < right_lat and left_lon < city_lon < right_lon:
                within.append(city)
    else:
        for city in cities:
            city_lat = city.lat
            city_lon = city.lon
            if left_lat > city_lat > right_lat and left_lon < city_lon < right_lon:
                within.append(city)
    return within


contained_cities = cityreader_stretch(first_lat, first_lon, second_lat, second_lon, cities)

for city in contained_cities:
    print(city)
