import numpy as np


class ArithmeticsMixin:
    def __add__(self, other):
        return self.__class__(self.data + other.data)

    def __sub__(self, other):
        return self.__class__(self.data - other.data)

    def __mul__(self, other):
        return self.__class__(self.data * other.data)

    def __matmul__(self, other):
        return self.__class__(self.data @ other.data)


class FileMixin:
    def save(self, filename):
        with open(filename, 'wb') as f:
            np.save(f, self.data)

    @classmethod
    def load(cls, filename):
        with open(filename, 'rb') as f:
            data = np.load(f)
        return cls(data)


class DisplayMixin:
    def __str__(self):
        return f"{self.__class__.__name__}({self.data})"


class AccessMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = np.array(value, dtype=np.float64)


class MatrixOnMixins(ArithmeticsMixin, FileMixin, DisplayMixin, AccessMixin):
    def __init__(self, data):
        self.data = data
