#  Sprint Challenge: Intro to Python (cityreader)

## Minimum Viable Product
To meet MVP in the city reader portion you will need to create a class to hold a city location. Call the class `City`. It should have fields for `name`, `lat` and `lon` (representing latitude and longitude).
_We have a collection of US cities with population over 750,000 stored in the file "cities.csv". (CSV stands for "comma-separated values".)_
In the body of the `cityreader` function, use Python's built-in "csv" module to read this file so that each record is imported into a City instance. Then return the list with all the City instances from the function. 
_Google "python 3 csv" for references and use your Google-fu for other examples._

`Note that the first line of the CSV is header that describes the fields, this should not be loaded into a City object.`

## Stretch Goal
Allow the user to input two points, each specified by latitude and longitude. These points form the corners of a lat/lon square. Pass these latitude and longitude values as parameters to the `cityreader_stretch` function, along with the `cities` list that holds all the City instances from the `cityreader` function. This function should output all the cities that fall within the coordinate square.

_Be aware that the user could specify either a lower-left/upper-right pair of coordinates, or an upper-left/lower-right pair of coordinates._ 

_Hint:_ `normalize` the input data so that it's `always` one or the other, then search for cities.

In the example below, inputting 32, -120 first and then 45, -100 should not change the results of what the `cityreader_stretch` function returns.

_Example I/O:_
```
Enter lat1,lon1: 45,-100
Enter lat2,lon2: 32,-120
Albuquerque: (35.1055,-106.6476)
Riverside: (33.9382,-117.3949)
San Diego: (32.8312,-117.1225)
Los Angeles: (34.114,-118.4068)
Las Vegas: (36.2288,-115.2603)
Denver: (39.7621,-104.8759)
Phoenix: (33.5722,-112.0891)
Tucson: (32.1558,-110.8777)
Salt Lake City: (40.7774,-111.9301)
```