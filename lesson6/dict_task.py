class Dict:
    def __init__(self, dict_=None):
        if dict_:
            self.__dictionary = dict_
        else:
            self.__dictionary = {}

        self.__current_item = 0

    def __getitem__(self, item):
        return self.__dictionary[item]

    def get(self, key):
        if key in self.__dictionary:
            return self.__getitem__(key)
        raise KeyError(f"There is no key {key} in this Dict")

    def keys(self):
        return [key for key in self.__dictionary]

    def values(self):
        return [self.__dictionary[key] for key in self.__dictionary]

    def items(self):
        return [(key, self.__dictionary[key]) for key in self.__dictionary]

    def __add__(self, other):
        return Dict({**self.__dictionary, **other.__dictionary})


a = Dict({1: 2, 3: 4})
print(a.get(1))
print(a.keys())
print(a.values())
print(a.items())
b = Dict({5: 9, 8: 6})
c = a + b
print(c.items())

