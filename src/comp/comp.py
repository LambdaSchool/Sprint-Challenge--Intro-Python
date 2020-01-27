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
print("Starts with D:")
a = [str(person.name) for person in humans if person.name[0] == "D"]
print(sorted(a))  #Printing in ascending order 

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [str(person.name) for person in humans if person.name[-1] == "e"]
print(sorted(b))

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
name_starts = ["C", "D", "E", "F", "G" ]
c = [str(person.name) for person in humans if person.name[0] in name_starts]
print(sorted(c))

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [int(person.age + 10) for person in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [str(f"{person.name}-{person.age}") for person in humans]
print(sorted(e))

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(person.name, person.age) for person in humans if person.age >= 27 and person.age <= 32]
print(sorted(f))

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [Human((person.name).upper(), (person.age +5)) for person in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(person.age) for person in humans]
print(h)
