import numpy as np
from mixin import MatrixOnMixins


def main():
    np.random.seed(0)
    x, y = (np.random.randint(0, 10, (10, 10)) for _ in range(2))

    x = MatrixOnMixins(x)
    print("Mixin first:", x, sep='\n')
    y = MatrixOnMixins(y)
    print("Mixin second:", y, sep='\n')

    add_result = x + y
    print("Add:", add_result, sep='\n')
    mul_result = x * y
    print("Mul:", mul_result, sep='\n')
    matmul_result = x @ y
    print("MatMul:", matmul_result, sep='\n')


if __name__ == "__main__":
    main()
