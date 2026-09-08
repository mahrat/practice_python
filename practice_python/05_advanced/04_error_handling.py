# exception handling practice

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("can't divide by zero")
        return None
    else:
        # only runs if NO exception happened, kept forgetting this exists
        print("division worked fine")
        return result
    finally:
        # always runs no matter what
        print("divide() finished")


print(divide(10, 2))
print(divide(10, 0))


# catching multiple exception types
def parse_number(s):
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print(f"couldn't parse '{s}': {e}")
        return None


print(parse_number("42"))
print(parse_number("abc"))
print(parse_number(None))


# custom exceptions - subclass Exception, felt fancy the first time i did this
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"tried to withdraw {amount} but balance is only {balance}")


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


try:
    withdraw(100, 500)
except InsufficientFundsError as e:
    print("custom error caught:", e)


# catching everything (generally considered bad practice unless you re-raise or log properly)
def risky_operation(x):
    try:
        return 10 / x
    except Exception as e:
        # too broad usually, but fine for quick scripts / learning
        print(f"something went wrong: {type(e).__name__}: {e}")
        return None


print(risky_operation(0))
print(risky_operation("string"))   # TypeError, still gets caught by the broad except


# re-raising an exception after logging it
def process(data):
    try:
        return data["key"]
    except KeyError:
        print("missing key, re-raising after logging")
        raise   # re-raises the SAME exception, keeps original traceback


try:
    process({"other_key": 1})
except KeyError as e:
    print("caught after re-raise:", e)

# assert statements - quick sanity checks, not for real validation (can be disabled with -O flag)
def get_average(nums):
    assert len(nums) > 0, "list can't be empty"
    return sum(nums) / len(nums)

print(get_average([1, 2, 3]))
