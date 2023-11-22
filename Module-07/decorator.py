# decorator : ak ta nested funtion .
import math
import time


def timer(func):
    def inner(*args, **kargs):  # parameter pass korbo
        print("Time started")
        start = time.time()
        # print(func)
        func(*args, **kargs)
        print("time ended")
        end = time.time()
        print(f"total time taken {end - start}")

    return inner


# timer()()


@timer  # timer function er moddy decorate kory get_factorial funtion ta ky patacchi
def get_factorial(n):
    print("factorial starting")
    result = math.factorial(n)
    print(f"Factorial of {n} is : {result}")


get_factorial(n=5)
# timer(get_factorial)()
