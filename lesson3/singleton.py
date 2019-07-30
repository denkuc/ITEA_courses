class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)

            return cls._instance
        else:
            raise Exception("Instance already exists")


class A(Singleton):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


a1 = A("1")
a2 = A("2")

print(a1.get_name())
print(a2.get_name())
