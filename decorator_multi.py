import functools


def upper_decorator(function):
    @functools.wraps(function)  # Make sure metadata from original func is preserved throughout stacking
    def wrapper():
        func = function()
        to_uppercase = func.upper()
        return to_uppercase
    return wrapper


def add_decorator(function):
    @functools.wraps(function)
    def wrapper():
        func = function()
        added_string = func + ", world!"
        return added_string
    return wrapper


# --------------------------------------
@add_decorator  # Second, add string world
@upper_decorator  # First, put hello in uppercase
def say_hello():
    return 'hello'


print(say_hello())
