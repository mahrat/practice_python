# classes 101

class Dog:
    # class variable, shared across all instances
    species = "Canis familiaris"

    def __init__(self, name, age):
        # instance variables, unique per object
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

    def birthday(self):
        self.age += 1
        return f"{self.name} is now {self.age}"


d1 = Dog("Rex", 3)
d2 = Dog("Buddy", 5)

print(d1.bark())
print(d2.bark())
print(d1.species, d2.species)   # same class variable

d1.birthday()
print(d1.age)

# instance vs class variable gotcha
d1.species = "changed just for d1"   # this creates an INSTANCE variable, doesn't touch class var
print(d1.species)
print(d2.species)   # still original, wasn't expecting this at first


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance   # underscore = "protected", convention not enforced by python

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount

    def get_balance(self):
        return self._balance

    # __str__ controls what print(obj) shows, way better than default <object at 0x...>
    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance={self._balance})"


acc = BankAccount("sahil", 100)
acc.deposit(50)
acc.withdraw(30)
print(acc)
print(acc.get_balance())

try:
    acc.withdraw(10000)
except ValueError as e:
    print("error:", e)


# class methods and static methods, kept forgetting the difference
class MathHelper:
    @staticmethod
    def add(a, b):
        # doesn't need self or cls, just a regular function living in the class
        return a + b

    @classmethod
    def description(cls):
        # gets the class itself as first arg
        return f"this is the {cls.__name__} class"


print(MathHelper.add(2, 3))
print(MathHelper.description())
