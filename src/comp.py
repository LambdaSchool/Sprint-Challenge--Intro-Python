import math

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "<Human: %s, %d>" % (self.name, self.age)

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':

print("Starts with D:")
r = [ i.name for i in humans if i.name[0] == 'D' ]  # TODO
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

print("Ends with e:")
# Need to split the string. If i.name[:-2] is last two character, then i.name[-1 is last character of string?]
r = [ i.name for i in humans if i.name[-1] == 'e' ]  # TODO
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

print("Starts between C and G, inclusive:")
letters = ['C', 'D', 'E', 'F', 'G']
r = [ i.name for i in humans if i.name[0] in letters ]  # TODO
print(r)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
r = [ i.age + 10 for i in humans ]  # TODO
print(r)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
r = [ '{0}-{1}'.format(i.name, i.age) for i in humans ]  # TODO
print(r)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
ages = [27, 28, 29, 30, 31, 32]
r = [ ( i.name, i.age ) for i in humans if i.age in ages ]  # TODO
print(r)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The "humans" list should be unmodified.

# Create new Humans class then?

print("All names capitalized:")
r = [ Human( i.name.upper(), i.age + 5 ) for i in humans ]  # TODO
print(r)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
r = [ math.sqrt(i.age) for i in humans ]  # TODO
print(r)