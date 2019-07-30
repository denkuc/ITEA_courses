def a(k):
    print(k)

    def b(c):
        print(c)

        def e(f):
            print("The end")
        return e
    return b


result = a(10)(39)(1000)
print(result)


def outer_decorator(number_of_repeats):
    def inner_decorator(func):
        def wrapper(*args):
            print('Beginning')
            for i in range(number_of_repeats):
                func()
            print('End')
            return func.__name__
        return wrapper
    return inner_decorator


@outer_decorator(10)
def lol():
    print('a')


lol()
