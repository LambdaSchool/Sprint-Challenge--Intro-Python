from string import ascii_uppercase
from math import sqrt

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

print("\nStarts with D:")
r = [human.name for human in humans if human.name[0] is "D"]
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

print("\nEnds with e:")
r = [human.name for human in humans if human.name[-1] is "e"]
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

print("\nStarts between C and G, inclusive:")
r = [human.name for human in humans if human.name[0] in ascii_uppercase[2:7]]
print(r)

# Write a list comprehension that creates a list of all the ages plus 10.

print("\nAges plus 10:")
r = [human.age + 10 for human in humans]
print(r)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.

print("\nName hyphen age:")
r = ["%s-%d" % (human.name, human.age) for human in humans]
print(r)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.

print("\nNames and ages between 27 and 32:")
r = [(human.name, human.age) for human in humans if human.age in range(27, 33)]
print(r)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The "humans" list should be unmodified.

print("\nAll names capitalized:")
r = [Human(human.name.upper(), (human.age + 5)) for human in humans]
print(r)

# Write a list comprehension that contains the square root of all the ages.

print("\nSquare root of ages:")
r = [sqrt(human.age) for human in humans]
print(r)