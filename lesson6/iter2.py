class MyArray:
    __slots__ = "_size", "_type", "_array"

    def __init__(self, size, vartype):
        self._size = size
        self._type = vartype
        self._array = [0] * size

    def __getitem__(self, idx):
        if idx > self._size - 1:
            raise StopIteration('Out of range')

        return self._array[idx]

    def __setitem__(self, idx, value):

        if isinstance(value, self._type) and idx < self._size:
            self._array[idx] = value
        else:
            raise TypeError("Take care of type and range")

    def __len__(self):
        return len(self._array)


arr = MyArray(10, int)
arr[0] = 2
print(arr)

for i in arr:
    print(i)
