def logger(func):
    def wrapper(*args, **kwargs):
        print("Calling function:", func.__name__)
        return func(*args, **kwargs)
    return wrapper
@logger
def greet(name):
    print("Hello", name)
greet("Tanisha")
