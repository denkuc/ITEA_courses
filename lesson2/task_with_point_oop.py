class Point:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def set_x(self, x):
        self._x = x

    def get_x(self):
        return self._x

    def set_y(self, y):
        self._y = y

    def get_y(self):
        return self._y

    def set_z(self, z):
        self._z = z

    def get_z(self):
        return self._z

    def __add__(self, other):
        result_x = self.get_x() + other.get_x()
        result_y = self.get_y() + other.get_y()
        result_z = self.get_z() + other.get_z()
        result_point = Point(result_x, result_y, result_z)

        return result_point

    def __sub__(self, other):
        result_x = self.get_x() - other.get_x()
        result_y = self.get_y() - other.get_y()
        result_z = self.get_z() - other.get_z()
        result_point = Point(result_x, result_y, result_z)

        return result_point

    def __mul__(self, other):
        result_x = self.get_x() * other.get_x()
        result_y = self.get_y() * other.get_y()
        result_z = self.get_z() * other.get_z()
        result_point = Point(result_x, result_y, result_z)

        return result_point

    def __truediv__(self, other):
        result_x = self.get_x() / other.get_x()
        result_y = self.get_y() / other.get_y()
        result_z = self.get_z() / other.get_z()
        result_point = Point(result_x, result_y, result_z)

        return result_point

    def __neg__(self):
        result_x = self.get_x() * -1
        result_y = self.get_y() * -1
        result_z = self.get_z() * -1
        result_point = Point(result_x, result_y, result_z)

        return result_point

    def __repr__(self):
        return 'Point({}, {}, {})'.format(self._x, self._y, self._z)


point1 = Point(1, 2, 3)
point2 = Point(1, 2, 3)

print(point1*point2)
