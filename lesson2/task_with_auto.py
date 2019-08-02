class Automobile:
    _seats = 4
    _wheels = 4
    _electro = False

    def get_seats(self):
        return self._seats

    def get_wheels(self):
        return self._wheels

    def beep(self):
        print('Beep!')

    def move(self):
        print('Wroom')

    def __add__(self, other):
        result = self.get_seats() + other.get_seats()
        return result

    def __eq__(self, other):
        result = self.__class__ == other.__class__
        return result

    def __neg__(self):
        result = self.get_seats() * -1
        return result


class Bus(Automobile):
    _seats = 40
    _wheels = 6

    def beep(self):
        print('BEEP-BEEP!')


class Car(Automobile):
    _seats = 5
    _wheels = 4

    def beep(self):
        print('BEEP!')


class ElectroCar(Automobile):
    _seats = 4
    _electro = True

    def move(self):
        print('Wroom')


class Lorry(Automobile):
    _seats = 2
    _electro = False

    def move(self):
        print('TU-TU!')


car1 = ElectroCar()
lorry = Lorry()
car2 = Car()
bus = Bus()

print(car1.__class__)
print(lorry.__class__)
print(lorry == bus)
print(lorry+car1)
print(-car1)
