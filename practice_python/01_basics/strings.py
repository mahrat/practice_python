# string practice

s = "Hello, World"

print(s.lower())
print(s.upper())
print(s.replace("World", "Python"))
print(len(s))

# slicing - still gotta think about this every time lol
print(s[0])       # H
print(s[-1])      # d
print(s[0:5])     # Hello
print(s[7:])      # World
print(s[::-1])    # reversed string, this trick is cool

# f-strings, way better than .format
name = "mahesh"
age = 22
print(f"my name is {name} and i am {age} years old")

# old way (keeping for reference, don't use this anymore)
print("my name is {} and i am {} years old".format(name, age))

# split and join
sentence = "the quick brown fox"
words = sentence.split(" ")
print(words)
print("-".join(words))

# strip whitespace
messy = "   lots of spaces   "
print(f"'{messy.strip()}'")

# check stuff
print("quick" in sentence)
print(sentence.startswith("the"))
print(sentence.endswith("fox"))

# string is immutable, this doesn't change s
s.upper()
print(s)  # still "Hello, World" bc upper() returns a new string, doesn't mutate

# building a string in a loop - learned that += in a loop is not great for huge strings
# but fine for small stuff like this
result = ""
for ch in "abc":
    result += ch.upper()
print(result)

# multi-line string
paragraph = """this is
a multi line
string"""
print(paragraph)
