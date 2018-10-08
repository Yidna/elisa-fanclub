from functionality.typedef.type import Type
from numpy import ndarray


class Image(Type):

    def _check(self):
        value = self._symbol_table[self._value]
        return value is not None and isinstance(value, ndarray)

    def _cast(self):
        return self._symbol_table[self._value].copy()
