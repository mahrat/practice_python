# dicts, sets, tuples

# --- dictionaries ---
person = {
    "name": "sahil",
    "age": 22,
    "city": "dehradun"
}

print(person["name"])
print(person.get("age"))
print(person.get("country", "not found"))  # default value when key missing, useful

person["email"] = "sahil@example.com"  # add new key
print(person)

del person["city"]
print(person)

# loop through a dict
for key, value in person.items():
    print(key, "->", value)

for key in person.keys():
    print(key)

for value in person.values():
    print(value)

# dict comprehension
squares_dict = {n: n**2 for n in range(5)}
print(squares_dict)

# nested dict
students = {
    "s1": {"name": "a", "grade": 90},
    "s2": {"name": "b", "grade": 75}
}
print(students["s1"]["name"])

# merging dicts (python 3.9+)
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = d1 | d2   # d2 wins on conflicts
print(merged)

# --- sets ---
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))

s1.add(10)
print(s1)

# sets remove duplicates automatically, useful trick
dupes = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(dupes))
print(unique)  # NOTE: order not guaranteed, sets are unordered

# --- tuples ---
point = (3, 4)
print(point[0], point[1])

# tuples are immutable
# point[0] = 5  -> this throws TypeError, tried it, learned the hard way

x, y = point   # unpacking
print(x, y)

# tuple of tuples
coords = ((0, 0), (1, 1), (2, 4))
for cx, cy in coords:
    print(cx, cy)

# namedtuple - cleaner than plain tuples when you have fixed fields
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)
