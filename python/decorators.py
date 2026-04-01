import time

# Decoratos : Functions that add functionality to other functions (like middleware)

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute")
        return result
    return wrapper


@timer  # Decorator same as timer(say_hello)
def say_hello(n):
    time.sleep(n) # Pause execution for n seconds
    print("Hello")

say_hello(5)


def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{key}={value}" for key, value in kwargs.items())
        print(f"Function {func.__name__} called with arguments {args_value} and keyword arguments {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def greet(name, message):
    print(f"Hello {name}, {message}")

greet("Akash", "How are you?")


def cache(func):
    cache_dict = {}
    def wrapper(*args, **kwargs):
        if args in cache_dict:
            return cache_dict[args]
        else:
            result = func(*args, **kwargs)
            cache_dict[args] = result
            return result
    return wrapper

@cache
def sum(a, b):
    time.sleep(2)
    return a + b

print(sum(1, 2))