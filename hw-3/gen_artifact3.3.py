import numpy as np
from hash_matrix import HashedMatrix


def main():
    a = np.asarray([[2, 3], [2, 1]])
    c = np.asarray([[1, 6], [2, 1]])
    b = np.eye(2)
    d = np.eye(2)


    assert(not np.array_equal(a, c))
    assert(hash(HashedMatrix(a)) == hash(HashedMatrix(c)))

    ab_hashed = HashedMatrix(a) @ HashedMatrix(b)
    cd_hashed = HashedMatrix(c) @ HashedMatrix(d)
    assert(np.array_equal(ab_hashed.data, cd_hashed.data))

    cd_true = c @ d
    assert(not np.array_equal(cd_true, cd_hashed.data))

    print(ab_hashed)
    print(hash(ab_hashed))


if __name__ == "__main__":
    main()
