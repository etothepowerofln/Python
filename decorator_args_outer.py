def decorator_maker(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Begin wrapper function")
            print(f"\t- From decorator maker: {decorator_arg1} {decorator_arg2} {decorator_arg3}")
            print(f"\t- From cities function: {args[0]} {args[1]} {args[2]}")
            print("End wrapper function")
            return func(*args, **kwargs)
        return wrapper
    return decorator

flor = "Florianópolis"
@decorator_maker(flor, "Milano","Roma")
def cities(city_one, city_two, city_three):
    print("Cities function called")
    return f"{city_one}, {city_two} and {city_three} are cities I visited"

print(cities(flor, "Porto Alegre", "São Paulo"))
