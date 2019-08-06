# class File:
#     def __init__(self, a, b):
#         self._a = a
#         self._b = b
#
#     def __enter__(self):
#         print(f"Entered args are {self._a, self._b}")
#         return "Hello"
#
#     def __exit__(self, *args):
#         print("The end of context manager")
#         print(args)
#
#
# with File(1, 2) as f:
#     print(f)


class File:
    def __init__(self, filename, regime):
        self.filename = filename
        self.regime = regime
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.regime)
        return self.file

    def __exit__(self, *args):
        if args[0]:
            f.write(f"{args[0]}\n{args[1]}\n{args[2]}")
        self.file.close()


with File("Aaaa.txt", "w") as f:
    print(1/0)
    f.write('Hello Earth!')
