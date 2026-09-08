# if / elif / else practice

age = 19

if age < 13:
    print("kid")
elif age < 20:
    print("teenager")
else:
    print("adult")

# ternary operator, kinda love this once you get used to it
status = "adult" if age >= 18 else "minor"
print(status)

# and / or / not
a = True
b = False
print(a and b)
print(a or b)
print(not a)

# checking multiple conditions
temp = 30
is_sunny = True

if temp > 25 and is_sunny:
    print("go to the beach")
elif temp <= 25 and is_sunny:
    print("nice day but kinda cold")
else:
    print("stay home")

# nested if (try not to do this too much, gets messy fast)
num = 15
if num > 0:
    if num % 2 == 0:
        print("positive even")
    else:
        print("positive odd")
else:
    print("not positive")

# match-case (python 3.10+, finally basically a switch statement)
day = 3
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case _:
        print("some other day")

# gotcha: comparing floats directly can be sketchy
x = 0.1 + 0.2
print(x == 0.3)          # False!! classic floating point issue
print(round(x, 1) == 0.3)  # True
