# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args, **kwargs):
        result = function(args[0], args[1], args[2])
        print(f"You called {function.__name__}{args}.\n"
              f"It returned: {result}.")
    return wrapper
# Use the decorator 👇


@logging_decorator
def a_function(n1, n2, n3):
    return n1 * n2 * n3


a_function(1, 2, 3)
