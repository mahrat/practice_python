
name = "sahil"          # str
age = 22                # int
height = 5.9             # float
is_student = True        # bool

print(name, age, height, is_student)

# type() tells you the type of something
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# python is dynamically typed so this is fine (you can reassign to a different type)
x = 10
print(type(x))
x = "now im a string"
print(type(x))

# basic type casting
num_str = "100"
num = int(num_str)
print(num + 1)


pi = 3.14159
print(round(pi, 2))

# multiple assignment
a, b, c = 1, 2, 3
print(a, b, c)

a, b = b, a
print("after swap:", a, b)

# None type
result = None
if result is None:
    print("nothing here yet")

# quick input practice (commented out bc annoying to run in a script every time)
# user_input = input("enter your name: ")
# print(f"hello {user_input}")
