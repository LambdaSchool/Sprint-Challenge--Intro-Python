# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

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
print("\n Starts with D:")
a = [guy.name for guy in humans if guy.name[0] == "D"]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("\nEnds with e:")
b = [guy.name for guy in humans if guy.name[-1] == "e"]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("\nStarts between C and G, inclusive:")
CandG = ('C', 'D', 'E', 'F', 'G')
c = [guy.name for guy in humans if guy.name[0] in CandG]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("\nAges plus 10:")
d = [guy.age + 10 for guy in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("\nName hyphen age:")
e = [(guy.name + "-" + str(guy.age)) for guy in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("\nNames and ages between 27 and 32:")
ageRange = (27, 28, 29, 30, 31, 32)
f = [(guy.name, guy.age) for guy in humans if guy.age in ageRange]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("\nAll names uppercase:")
g = [Human(guy.name.upper(), guy.age + 5) for guy in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("\nSquare root of ages:")
import math
# print(math.sqrt(4))
h = [math.sqrt(guy.age) for guy in humans]
print(h)
