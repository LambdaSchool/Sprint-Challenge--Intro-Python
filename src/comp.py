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
r = []  # TODO
for human in humans:
    if human.name[0] == "D":
        r.append(human)
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

print("Ends with e:")
r = []  # TODO
for human in humans:
    if human.name[-1] == "e":
        r.append(human)
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

print("Starts between C and G, inclusive:")
r = []  # TODO
for human in humans:
    if human.name[0] >= "C" and human.name[0] <= "G":
        r.append(human)
print(r)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
r = []  # TODO
for human in humans:
    age = human.age + 10
    r.append(age)
print(r)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
r = []  # TODO
for human in humans:
    name = "%s-%d" % (human.name, human.age)
    r.append(name)
print(r)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
r = []  # TODO
for human in humans:
    if human.age >= 27 and human.age <= 32:
        r.append("%s, %d" % (human.name, human.age))
print(r)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names capitalized:")
r = []  # TODO
for human in humans:
    person = "Human: %s, %d" % (human.name.upper(), human.age + 5)
    r.append(person)
print(r)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
r = []  # TODO
for human in humans:
    sqRoot = "%s: %d" % (human.name, math.sqrt(human.age))
    r.append(sqRoot)
print(r)