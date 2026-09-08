# functions practice

def greet(name):
    return f"hello, {name}!"

print(greet("sahil"))


def add(a, b):
    return a + b

print(add(3, 5))


# default arguments
def power(base, exp=2):
    return base ** exp

print(power(4))       # uses default exp=2
print(power(4, 3))    # overrides default


# NEVER use mutable default args, learned this the hard way
def add_item_bad(item, items=[]):
    items.append(item)
    return items

print(add_item_bad("a"))
print(add_item_bad("b"))  # you'd expect just ["b"] but it keeps the old list! weird python quirk


def add_item_good(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item_good("a"))
print(add_item_good("b"))  # correctly just ["b"] now


# multiple return values (actually returns a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = min_max([4, 1, 9, 2])
print(lo, hi)


# recursive function
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# docstrings, should probably use these more than i do
def divide(a, b):
    """Divide a by b. Raises ValueError if b is 0."""
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b

print(divide(10, 2))

try:
    divide(5, 0)
except ValueError as e:
    print("caught error:", e)


# scope - local vs global
counter = 0

def increment():
    global counter   # need this keyword or it creates a new local var instead
    counter += 1

increment()
increment()
print(counter)
