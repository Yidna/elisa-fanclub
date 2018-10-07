from functionality.typedef.type import Type


class Integer(Type):

    def _check(self):
        return isinstance(self._value, int)
