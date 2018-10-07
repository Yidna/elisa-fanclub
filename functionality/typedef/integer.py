from functionality.typedef.type import Type


class Integer(Type):

    def _check(self):
        try:
            self._cast()
            return True
        except ValueError:
            return False

    def _cast(self):
        return int(self._value)
