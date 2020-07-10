import sys
# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
class City:
  """
  Class for city location
  """
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon

  def __str__(self):
    return f'{self.name}, at ({self.lat}, {self.lon})'

  def __repr__(self):
    return f'City({self.name}, {self.lat}, {self.lon})'

city1 = City('Worcestershire', 52.192001, -2.22)
print(city1)

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
import csv
cities = []

def cityreader(cities=[]):
  # Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
  with open('src/cityreader/cities.csv', "r") as file:
    reader = csv.reader(file)
    # This next line skips the header
    next(reader)
    for row in reader:
      city = City(row[0], float(row[3]), float(row[4]))
      cities.append(city)
  return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
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

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = []

  # Ensure that the lat and lon valuse are all floats
  lat1, lon1, lat2, lon2 = map(float, [lat1, lon1, lat2, lon2])

  if lat1 > lat2:
    if lon1 > lon2:
      upper_right = [lat1, lon1]
      bottom_left = [lat2, lon2]
    else:
      upper_right = [lat1, lon2]
      bottom_left = [lat2, lon1]
  if lat1 < lat2:
    if lon1 < lon2:
      upper_right = [lat2, lon2]
      bottom_left = [lat1, lon1]
    else:
      upper_right = [lat2, lon1]
      bottom_left = [lat1, lon2]

  # Go through each city and check to see if it falls within 
  # the specified coordinates.

  # The city will be in range if City.lat < upper_right[0] and > bottom_left[0]
  # while meeting the same for lon

  for c in cities:
    if c.lat < upper_right[0] and c.lat > bottom_left[0]:
      if c.lon < upper_right[1] and c.lon > bottom_left[1]:
        within.append(c)

  return within

# Tests weren't running properly when imported,
#  so this will run if this script ran directly
if __name__ == "__main__":
  inputting = True
  while inputting:
    print("Please enter with no spaces")
    try:
      corner1 = list(map(float, input("Enter the first coordinate: lat1,long1 ").split(",")))
    # split the input string into a list, map the float function to that list
    # need to make it a list after
      corner2 = list(map(float, input("Enter the second coordinate: lat2,long2 ").split(",")))
      inputting = False
    except ValueError:
      print("Try again with floats and no spaces. (eg. 45,-120.55)")
      print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

  print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
  # lat = corner[0] and lon = corner[1]. We can input that into the function
  print("The following cities are within that range: \n",
  cityreader_stretch(corner1[0], corner1[1], corner2[0], corner2[1], cities))
