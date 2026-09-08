# practicing importing my own module (my_helpers.py in this same folder)

import my_helpers

print(my_helpers.is_even(10))
print(my_helpers.celsius_to_fahrenheit(0))
print(my_helpers.PI)

# importing specific things instead of the whole module
from my_helpers import is_even, PI

print(is_even(7))
print(PI)

# renaming on import with "as", useful when module names are long or clash
import my_helpers as h
print(h.is_even(3))

# __name__ note: when we run THIS file, my_helpers is being imported (not run directly)
# so the "if __name__ == '__main__'" block inside my_helpers.py does NOT execute here
# only prints stuff if you run "python my_helpers.py" directly, try it and compare
