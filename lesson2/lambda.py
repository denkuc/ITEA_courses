addition = lambda x, y: x + y

print(addition(1, 3))

list_var = [0, 1, 333, -27, 42, 88, 69]

map_var1 = map(lambda x: x ** 2, list_var)
map_var2 = list(filter(lambda x: x > 0, list_var))
print(list(map_var1))
print(map_var2)
print([print(i) for i in map_var1])
