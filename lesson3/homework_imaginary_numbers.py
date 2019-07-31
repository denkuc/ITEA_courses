

class ImaginaryNumber:
    """number in the form of x+yi"""
    IMAGINARY = "i"

    def __init__(self, real_part, i_part):
        self.__real_part = real_part
        self.__i_part = i_part

    def __get_real_part(self):
        return self.__real_part

    def __get_i_part(self):
        return self.__i_part

    def __repr__(self):
        x = self.__real_part
        y = self.__i_part
        i = self.IMAGINARY

        if y == 0:
            return f"{x}"
        elif y < 0:
            return f"{x}{y}{i}"
        else:
            return f"{x}+{y}{i}"

    def __add__(self, other):
        x1 = self.__get_real_part()
        x2 = other.__get_real_part()
        y1 = self.__get_i_part()
        y2 = other.__get_i_part()

        result_real_part = x1 + x2
        result_i_part = y1 + y2

        return ImaginaryNumber(result_real_part, result_i_part)

    def __sub__(self, other):
        x1 = self.__get_real_part()
        x2 = other.__get_real_part()
        y1 = self.__get_i_part()
        y2 = other.__get_i_part()

        result_real_part = x1 - x2
        result_i_part = y1 - y2

        return ImaginaryNumber(result_real_part, result_i_part)

    def __mul__(self, other):
        x1 = self.__get_real_part()
        x2 = other.__get_real_part()
        y1 = self.__get_i_part()
        y2 = other.__get_i_part()

        result_real_part = x1 * x2 - y1 * y2
        result_i_part = x1 * y2 + x2 * y1

        return ImaginaryNumber(result_real_part, result_i_part)

    def __truediv__(self, other):
        x1 = self.__get_real_part()
        x2 = other.__get_real_part()
        y1 = self.__get_i_part()
        y2 = other.__get_i_part()

        result_real_part = (x1 * x2 + y1 * y2)/(x2 ** 2 + y2 ** 2)
        result_i_part = (x2 * y1 - x1 * y2)/(x2 ** 2 + y2 ** 2)

        return ImaginaryNumber(result_real_part, result_i_part)

    def __neg__(self):
        result_real_part = -1 * self.__get_real_part()
        result_i_part = -2 * self.__get_i_part()

        return ImaginaryNumber(result_real_part, result_i_part)


complex1 = ImaginaryNumber(2, 5)
complex2 = ImaginaryNumber(-60, -5)
complex3 = ImaginaryNumber(5.5, 42)
complex4 = ImaginaryNumber(1 / 3, 88)

print(complex1 + complex3)
print(complex4 * complex2)
print(complex2 / complex1)
print(complex3 - complex4)
print(-(complex2 + complex2))

example1 = ImaginaryNumber(2, 5)
example2 = ImaginaryNumber(3, -2)
print(example1/example2)
