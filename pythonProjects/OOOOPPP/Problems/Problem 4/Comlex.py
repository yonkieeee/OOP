import math


class ComplexNumber():

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def __abs__(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        denom = other.real ** 2 + other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(real, imag)

    def __str__(self):
        sign = "+" if self.imag > 0 else ''
        return f"{self.real}{sign}{self.imag}i"


def test_complex():
    z1 = ComplexNumber(1, 2)
    z2 = ComplexNumber(3, 4)
    z3 = ComplexNumber(1, 2)

    print(f"Z1: {z1}")
    print(f"Z2: {z2}")
    print(f"Z3: {z3}", end="\n\n")

    print("Z1 == Z3:", z1 == z3)
    print("Z1 == Z2: ", z1 == z2, end="\n\n")

    print("ABS Z1: ", abs(z1), end="\n\n")

    print("Z1 + Z2: ", z1 + z2)
    print("Z1 - Z2: ", z1 - z2)
    print("Z1 * Z2: ", z1 * z2)
    print("Z1 / Z2: ", z1 / z2)


if "__main__" == __name__:
    test_complex()