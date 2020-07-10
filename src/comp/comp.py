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

# breakpoint()

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("\n1. Starts with D:")
a = [i.name for i in humans if i.name[0] == "D"]
print(a)
print("-----" * 5)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("2. Ends with e:")
b = [i.name for i in humans if i.name[-1] == "e"]
print(b)
print("-----" * 5)


# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("3. Starts between C and G, inclusive:")
c = [i.name for i in humans if i.name[0] in "CDEFG"]
print(c)
print("-----" * 5)


# Write a list comprehension that creates a list of all the ages plus 10.
print("4. Ages plus 10:")
d = [(i.age + 10) for i in humans]
print(d)
print("-----" * 5)


# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("5. Name hyphen age:")
e = [f"{i.name}-{i.age}" for i in humans]
print(e)
print("-----" * 5)


# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("6. Names and ages between 27 and 32:")
f = [(i.name, i.age) for i in humans if i.age in range(27,33)]
print(f)
print("-----" * 5)


# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("7. All names uppercase:")
g = [Human(i.name.upper(), i.age + 5) for i in humans]
# Still returning tuple, test wants full Human objects
print(g)
print("-----" * 5)

# Write a list comprehension that contains the square root of all the ages.
print("8. Square root of ages:")
import math
h = [math.sqrt(i.age) for i in humans]
print(h)
print("-----" * 5)