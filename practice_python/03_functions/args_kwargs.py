# *args and **kwargs - took me a while to actually get comfortable with these

def add_all(*args):
    # args comes in as a tuple
    print("args:", args, type(args))
    return sum(args)

print(add_all(1, 2, 3, 4))


def print_info(**kwargs):
    # kwargs comes in as a dict
    print("kwargs:", kwargs)
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_info(name="sahil", age=22, city="dehradun")


# combining normal args, *args, **kwargs
def full_example(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("extra positional:", args)
    print("extra keyword:", kwargs)

full_example(1, 2, 3, 4, x=10, y=20)


# unpacking when CALLING a function (the reverse direction, confusing at first)
def add3(x, y, z):
    return x + y + z

nums = [1, 2, 3]
print(add3(*nums))   # unpack list into positional args

info = {"x": 1, "y": 2, "z": 3}
print(add3(**info))  # unpack dict into keyword args


# keyword-only args (force caller to use keyword, forget the syntax sometimes)
def make_profile(name, *, age, city):
    return f"{name} ({age}) from {city}"

print(make_profile("sahil", age=22, city="dehradun"))
# make_profile("sahil", 22, "dehradun")  -> this would error, age/city MUST be keyword
