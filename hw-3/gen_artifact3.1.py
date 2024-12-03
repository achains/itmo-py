import numpy as np
from pymatrix import PyMatrix


def main():
    np.random.seed(0)
    x, y = (np.random.randint(0, 10, (10, 10)) for _ in range(2))
    print("x, y", x, y, sep='\n')

    x_pymatrix = PyMatrix(x.tolist())
    y_pymatrix = PyMatrix(y.tolist())

    expected_add = x + y
    actual_add = x_pymatrix + y_pymatrix
    assert(expected_add.tolist() == actual_add.matrix)
    print("x + y", actual_add, sep='\n')

    expected_mul = x * y
    actual_mul   = x_pymatrix * y_pymatrix
    assert(expected_mul.tolist() == actual_mul.matrix)
    print("x * y", actual_mul, sep='\n')

    expected_matmul = x @ y
    actual_matmul = x_pymatrix @ y_pymatrix
    assert(expected_matmul.tolist() == actual_matmul.matrix)
    print("x @ y", actual_matmul, sep='\n')

if __name__ == "__main__":
    main()
