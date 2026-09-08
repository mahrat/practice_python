# a little helper module i made just to practice importing my own code
# instead of always importing from built-in / third party stuff

def is_even(n):
    return n % 2 == 0


def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


PI = 3.14159


if __name__ == "__main__":
    # this block only runs if you run THIS file directly, not when it's imported
    # took me a while to get why this pattern matters
    print("running my_helpers.py directly")
    print(is_even(4))
    print(celsius_to_fahrenheit(100))
