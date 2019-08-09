list_ = [1, 2, 3]

b = iter(list_)

print(next(b))
print(next(b))
print(next(b))


class NumberGenerator:
    def __init__(self, start, end):
        self._start = start
        self._end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self._start < self._end:
            self._start += 1

            return self._end

        raise StopIteration("The end if structure")


iterator = NumberGenerator(1, 9)

for i in iterator:
    print(i)