from functionality.typedef.type import Type


class Image(Type):

    def _check(self):
        return self._value in self._symbol_table