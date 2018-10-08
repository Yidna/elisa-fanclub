from functionality.typedef.type import Type


class Directory(Type):
    """
    Example:
        # this is an entry in _symbol_table
        bbt-dir: {
            root: "./images/bbt-dir",
            files: {
                expired-bbt.jpg: [1, 2, 3, ...]
                smiley-bbt.jpg: [3, 2, 1, ...]
            }
        }
    """

    def _check(self):
        value = self._symbol_table[self._value]
        return value is not None and "root" in value and "files" in value

    def _cast(self):
        return self._symbol_table[self._value].copy()
