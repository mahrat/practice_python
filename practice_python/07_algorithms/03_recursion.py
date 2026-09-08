# recursion practice - functions that call themselves
# key ingredients: base case (when to stop) + recursive case (call itself with smaller problem)
# messed up base cases a LOT when starting out (infinite recursion -> RecursionError)

def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)   # recursive case


def fibonacci(n):
    return n


# memoized version - way faster, learned this after fibonacci(35) took forever to run
from functools import lru_cache

# @lru_cache(maxsize=None)
# def fibonacci_fast(n):
#     if n <= 1:
#         return n
#     return fibonacci_fast(n - 1) + fibonacci_fast(n - 2)


def sum_list(lst):
    if not lst:            # empty list = base case
        return 0
    return lst[0] + sum_list(lst[1:])


def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


def is_palindrome(s):
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])   # check inner substring


# recursion on nested data structures, this one felt like a big "aha" moment
def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))   # recurse into the nested list
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    print("factorial(5):", factorial(5))
    print("fibonacci(10):", fibonacci(10))
    print("fibonacci_fast(50):", fibonacci_fast(50))   # would basically never finish with plain fibonacci()
    print("sum_list:", sum_list([1, 2, 3, 4, 5]))
    print("reverse_string:", reverse_string("hello"))
    print("is_palindrome('racecar'):", is_palindrome("racecar"))
    print("is_palindrome('hello'):", is_palindrome("hello"))
    print("is_palindrome('nurses run'):", is_palindrome("nurses run"))
    print("flatten:", flatten([1, [2, 3, [4, 5, [6]], 7], 8]))

    # this would crash with RecursionError if i uncomment it, python has a recursion depth limit
    # print(factorial(5000))
