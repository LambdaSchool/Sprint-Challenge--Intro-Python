# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.

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

import csv
# open cities.csv file then read from it.
with open('cities.csv', newline='') as f:
  reader = csv.reader(f, delimiter=',', quotechar='|')

  # skip a line then print line for every single city
  next(f)
  cities = [line for line in reader]

# close file
f.close()


# TODO

# Print the list of cities (name, lat, lon), 1 record per line.
for each in cities:
  print('{}, {}, {}'.format(each[0], each[3], each[4]))

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

print('\n\n\n\nEnter Lat and Lon separated by coma')
# remove whitespace, separate string by comma
coord1 = input('\nEnter the first set of coordinates >').replace(' ', '').split(",")
coord2 = input('enter 2nd set of coordinates >').replace(' ', '').split(",")

if coord1[0] <= coord2[0]:
  bigCoord = (coord2[0])
  smallCoord = (coord1[0])
else:
  bigLatLon = (coord1[0])
  smallCoord = (coord2[0])

if coord1[1] <= coord2[0]:
  bigCoord.append()
  



  print(bigCoord, smallCoord)