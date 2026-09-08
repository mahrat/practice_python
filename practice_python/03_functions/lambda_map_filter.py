# lambda, map, filter, reduce
# functional-ish python stuff, kinda fun once it clicks

square = lambda x: x ** 2
print(square(5))

add = lambda a, b: a + b
print(add(3, 4))

nums = [1, 2, 3, 4, 5, 6, 7, 8]

# map - apply function to every item
squared = list(map(lambda x: x ** 2, nums))
print(squared)

# filter - keep items where function returns True
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# map + filter combined (getting a bit fancy here)
even_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(even_squares)

# honestly list comprehensions do this more readably imo:
even_squares_v2 = [x**2 for x in nums if x % 2 == 0]
print(even_squares_v2)

# reduce - needs an import, not built-in like map/filter
from functools import reduce

total = reduce(lambda acc, x: acc + x, nums)
print(total)

product = reduce(lambda acc, x: acc * x, nums)
print(product)

# sorting with a lambda key - use this ALL the time
people = [("sahil", 22), ("amit", 19), ("riya", 25)]
sorted_by_age = sorted(people, key=lambda p: p[1])
print(sorted_by_age)

words = ["banana", "kiwi", "apple", "fig"]
sorted_by_len = sorted(words, key=len)
print(sorted_by_len)

# sorting dicts by value
scores = {"a": 90, "b": 70, "c": 85}
sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
print(sorted_scores)
