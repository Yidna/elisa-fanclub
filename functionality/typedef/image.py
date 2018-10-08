from functionality.typedef.type import Type
import numpy as np


class Image(Type):

    def _check(self):
        value = self._symbol_table[self._value]
        return value is not None and isinstance(value, np.ndarray)

    def _cast(self):
        return self._symbol_table[self._value].copy()
