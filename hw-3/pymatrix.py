import copy


class PyMatrix:
    def __init__(self, matrix):
        self.__matrix = copy.deepcopy(matrix)
        self.__shape = len(self.__matrix), (len(self.__matrix[0]) if self.__matrix else 0)

    @property
    def shape(self):
        return self.__shape

    @property
    def matrix(self):
        return self.__matrix

    def __add__(self, other):
        if not isinstance(other, PyMatrix):
            raise TypeError("Add operation is supported only with PyMatrix class")
        if self.__shape != other.__shape:
            raise ValueError(f"Add is valid only for matrices of the same shape: {self.__shape} != {other.__shape}")
        return PyMatrix([[self.__matrix[r][c] + other.__matrix[r][c] for c in range(self.__shape[1])] for r in range(self.__shape[0])])

    def __mul__(self, other):
        if not isinstance(other, PyMatrix):
            raise TypeError("Multiply operation is supported only with PyMatrix class")
        if self.__shape != other.__shape:
            raise ValueError(f"Multiply is valid for matrices of same shape (consider using matmul instead)")
        return PyMatrix([[self.__matrix[r][c] * other.__matrix[r][c] for c in range(self.__shape[1])] for r in
                         range(self.__shape[0])])

    def __matmul__(self, other):
        if not isinstance(other, PyMatrix):
            raise TypeError("Can only multiply matrix by matrix")
        if self.__shape[1] != other.__shape[0]:
            raise ValueError(f"Cannot multiply matrices of incompatible shapes: col {self.__shape[1]} != row {other.__shape[0]}")

        mul_result = [[0 for _ in range(other.__shape[1])] for _ in range(self.__shape[0])]
        for r in range(self.__shape[0]):
            for c in range(other.__shape[1]):
                mul_result[r][c] = sum(self.__matrix[r][i] * other.__matrix[i][c] for i in range(self.__shape[1]))
        return PyMatrix(mul_result)

    def __repr__(self):
        return "[" + "\n".join(["[" + " ".join(map(str, row)) + "]" for row in self.__matrix]) + "]"
