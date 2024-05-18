def upper_decorator(function):  # Enclosing function
    def wrapper():  # Nested function
        func = function()  # Closure - nested func access the outer scope
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


# --------------------------------------
def say_hi():  # Defining func to pass to decorator
    return "hi"


decorate = upper_decorator(
    say_hi
)  # Passing func as param and assigning decorator func to a var
print(decorate())


# --------------------------------------
@upper_decorator  # With this we don't have to assign decorator to a var anymore
def say_hello():
    return "hello"


print(say_hello())
