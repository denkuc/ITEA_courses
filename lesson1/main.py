# loops
numbers = range(100)
our_list1 = []
for n in numbers:
    if n % 2 == 0:
        our_list1.append(n)
our_list2 = [n for n in numbers if n % 2 == 0]
print(our_list1)
print(our_list2)
print(our_list1 == our_list2)

# dicts
countries_with_capitals = {'Ukraine': 'Kyiv', 'Brazil': 'Brasilia', 'Japan': 'Tokio', 'China': 'Beijing', 'Slovakia': 'Bratislava', 'Estonia': 'Tallinn'}
countries_list = ['Ukraine', 'Russia', 'Kazakhstan', 'Moldova', 'Latvia', 'Lithuania', 'Belarus', 'Estonia', 'Uzbekistan', 'Georgia', 'Armenia', 'Tajikistan', 'Azeibarjan', 'Turkmenistan']

for country in countries_list:
    if country in countries_with_capitals:
        print(countries_with_capitals[country])

a = {}
b = 10

# try-catch
try:
    # a['a']
    b = 1 / 0
except KeyError as e:
    print("Dictionary doesn't have key ", e)
except ZeroDivisionError as e:
    print("You caught the error ", e)


try:
    file = open('read.txt', 'w')
except:
    #Some Code
    pass
finally:
    pass


# functions
def hello_world():
    print('Hello world')


def division(func, arg1, arg2):
    try:
        func()
        result = arg1/arg2
        return result
    except ZeroDivisionError:
        print("Inside except block")


print(division(hello_world, 10, 20))
print(division(hello_world, 10, 0))


# args
def add1(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


def add2(*args):
    if len(args) > 0:
        return sum(args)


print(add1(1, 2, 5, 4, 6, 7, 3))
print(add2(19, 12, 231, 4, 3))
print(add2())
