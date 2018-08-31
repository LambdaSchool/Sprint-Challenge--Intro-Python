import re
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
    Human("harrison", 12),
    Human("igon", 41),
    Human("david", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':

print("Starts with D:")
r = [human for human in humans if human.name[0] == 'D' ]  # TODO
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".

print("Ends with e:")
r = [human for human in humans if human.name[len(human.name)-1] == 'e']  # TODO
print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

print("Starts between C and G, inclusive:")
specified_Letters_List = [chr(i) for i in range(67,72)]
r = [human for human in humans if human.name[0] in specified_Letters_List]
print(r)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
r = [human.age + 10 for human in humans]  # TODO
print(r)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
r = [f'{human.name}-{human.age}' for human in humans]  # TODO
print(r)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
r = [(human.name, human.age) for human in humans if human.age in range(27,33)]  # TODO
print(r)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names capitalized:") #Names already capitalized, so I edited some in the original list
r = [Human(human.name.capitalize(), human.age + 5) for human in humans]  # TODO
print(r)

print("All names uppercased:") #Extra comprehension added since previous one is meaningless
r = [Human(human.name.upper(), human.age +5) for human in humans]
print(r)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:") #Would've been more interesting if some of their ages were perfect squares
r = [human.age**(.5) for human in humans]  # TODO
print(r)
