import time


def speed_calc_decorator(function):

    def wrapper_function():
        before_time = time.time()
        function()
        after_time = time.time()
        time_taken = after_time - before_time
        print(f"{function.__name__} run speed: {time_taken}s")
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
