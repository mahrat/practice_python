# inheritance practice

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        # base class doesn't know how each animal speaks
        raise NotImplementedError("subclass must implement speak()")

    def describe(self):
        return f"{self.name} is an animal"


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"


animals = [Dog("Rex"), Cat("Whiskers")]

for a in animals:
    print(a.describe())     # inherited method, works for both
    print(a.speak())        # polymorphism - same method call, different behavior per class


# using super() to call parent constructor
class Puppy(Dog):
    def __init__(self, name, age):
        super().__init__(name)   # reuse parent init instead of repeating self.name = name
        self.age = age

    def speak(self):
        # override + still use parent version
        base_sound = super().speak()
        return f"{base_sound} (but it's a puppy so it's more of a yip)"


p = Puppy("Max", 1)
print(p.speak())
print(p.describe())   # inherited all the way from Animal


# multiple inheritance (used rarely but good to know it exists)
class Swimmer:
    def swim(self):
        return "swimming"


class Flyer:
    def fly(self):
        return "flying"


class Duck(Animal, Swimmer, Flyer):
    def speak(self):
        return f"{self.name} says Quack"


duck = Duck("Donald")
print(duck.speak())
print(duck.swim())
print(duck.fly())

# checking types
print(isinstance(duck, Animal))
print(isinstance(duck, Dog))       # False, duck isn't a dog
print(issubclass(Puppy, Dog))
print(issubclass(Puppy, Animal))   # True, transitively

# MRO (method resolution order) - checked this once when multiple inheritance got confusing
print(Duck.__mro__)
