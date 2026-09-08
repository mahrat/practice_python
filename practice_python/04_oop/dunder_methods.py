# dunder (double underscore) methods - these make custom objects behave like builtins
# spent a while on this file, kinda cool once it works

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # for print() / str() - human readable
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        # for debugging / repl, should ideally be unambiguous
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        # kinda arbitrary here but shows it's possible, using it as "magnitude" rounded
        return int((self.x ** 2 + self.y ** 2) ** 0.5)


v1 = Vector(2, 3)
v2 = Vector(1, 1)

print(v1 + v2)      # uses __add__
print(v1 - v2)      # uses __sub__
print(v1 == Vector(2, 3))   # uses __eq__, True
print(len(v1))      # uses __len__
print(v1)           # uses __str__


# property decorator - makes a method act like an attribute, use this instead of getter/setter boilerplate
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("radius can't be negative")
        self._radius = value

    @property
    def area(self):
        # read-only computed property, no setter defined
        return 3.14159 * self._radius ** 2


c = Circle(5)
print(c.radius)
print(c.area)

c.radius = 10   # calls the setter behind the scenes, looks like a normal attribute assignment
print(c.area)

try:
    c.radius = -5
except ValueError as e:
    print("error:", e)


# __getitem__ / __setitem__ - lets your object use square bracket syntax like a list/dict
class Playlist:
    def __init__(self):
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __getitem__(self, index):
        return self.songs[index]

    def __len__(self):
        return len(self.songs)


pl = Playlist()
pl.add("song a")
pl.add("song b")
print(pl[0])
print(len(pl))
