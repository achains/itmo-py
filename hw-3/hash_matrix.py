import numpy as np
from mixin import ArithmeticsMixin, DisplayMixin, AccessMixin

class HashMixin:
    def __hash__(self):
        return hash((np.prod(self.data), self.data.shape))


class HashedMatrix(HashMixin, ArithmeticsMixin, DisplayMixin, AccessMixin):
    _mul_cache = {}

    def __init__(self, data):
        self.data = data

    def __matmul__(self, other):
        key = (hash(self), hash(other))
        if key not in self._mul_cache:
            result = self.data @ other.data
            self._mul_cache[key] = HashedMatrix(result)
        return self._mul_cache[key]
