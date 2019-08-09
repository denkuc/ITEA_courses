class List:
    def __init__(self, list_=None):
        if list_:
            self.__list = list_
        else:
            self.__list = []

    def __iter__(self):
        return self

    def __getitem__(self, idx):
        if 0 <= idx < self.__len__() or idx == -1:
            return self.__list[idx]

        raise Exception("Index is out of range")

    def __setitem__(self, key, value):
        self.__list[key] = value

    def __delitem__(self, idx):
        if 0 <= idx < self.__len__() or idx == -1:
            del self.__list[idx]
        else:
            raise Exception("Index is out of range")

    def __len__(self):
        return len(self.__list)

    def pop(self, idx=-1):
        if 0 <= idx < self.__len__() or idx == -1:
            item = self.__getitem__(idx)
            self.__delitem__(idx)
            return item

        raise Exception("Index is out of range")

    def append(self, item):
        if self.__list:
            self.__list = self.__list + [item]
        else:
            self.__list = [item]

    def insert(self, idx, item):
        if 0 <= idx < self.__len__():
            self.__list[idx] = item
        else:
            raise Exception("Index is out of range")

    def remove(self, idx):
        if 0 <= idx < self.__len__():
            self.__delitem__(idx)
        else:
            raise Exception("Index is out of range")

    def clear(self):
        self.__list = []

    def __add__(self, other):
        return List(self.__list + other.__list)

    def __str__(self):
        return str(self.__list)


class Dict:
    def __init__(self):
        pass


a = List()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(4)
a.append(4)
a.append(4)
a.remove(1)
print(a.pop())
print(a.pop(0))
print(a)
a.insert(3, 100)
print(a)


b = List([5, 6, 7, 98])
print(b)
c = a + b
print(c)
c.clear()
print(c)
