from time import time
import requests as r


def outer_decorator(number_of_executions):
    def inner_decorator(func):
        def wrapper():
            for i in range(number_of_executions):
                time_start = time()

                func()

                time_of_execution = time() - time_start
                print(f'Request #{i+1} is executed in {time_of_execution} sec')
            print(f'Function name is {func.__name__}')
        return wrapper
    return inner_decorator


@outer_decorator(10)
def go_to_python_org():
    r.get('http://python.org')


go_to_python_org()
