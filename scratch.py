# just a scratch file, random stuff i was testing, don't judge the mess

# testing walrus operator (python 3.8+), kinda weird syntax at first
data = [1, 2, 3, 4, 5]
if (n := len(data)) > 3:
    print(f"list is long, has {n} items")

# testing string formatting alignment stuff for a table i wanted to print
for i in range(1, 4):
    print(f"{i:>3} | {i*i:<5} | {'x'*i}")

# quick fizzbuzz bc why not, classic
for i in range(1, 21):
    if i % 15 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

# messing with enumerate start param
for i, letter in enumerate("abc", start=1):
    print(i, letter)

# testing chained comparisons, didn't know python could do this
x = 5
print(1 < x < 10)

# quick check on how truthy/falsy works for different types
for val in [0, 1, "", "a", [], [1], None, {}, {"a": 1}]:
    print(val, "->", bool(val))

# was trying to remember how to reverse a dict (swap keys/values)
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
print(reversed_dict)

# random practice - counting word frequency, might turn this into a real exercise later
text = "the quick brown fox jumps over the lazy dog the fox runs"
word_counts = {}
for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1
print(word_counts)

# same thing but using Counter, way less code
from collections import Counter
print(Counter(text.split()))

# leaving this here, not done with it yet
# def some_incomplete_idea():
#     pass
