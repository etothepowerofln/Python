def decorator(function):
    def wrapper(*args, **kwargs):
        print("My arguments: {0}, {1}".format(*args, **kwargs))
        func = function(*args, **kwargs)
        to_uppercase = func.upper()
        return to_uppercase
    return wrapper

@decorator
def cities(city_one, city_two):
    print("Cities function called")
    return f"{city_one} and {city_two} are cities I visited"

print(cities("Florianópolis", "Porto Alegre"))
