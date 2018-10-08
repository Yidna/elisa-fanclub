from functionality.exceptions import InvalidParameterTypeException
from functionality.typedef.type import Type
from copy import deepcopy


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

    @staticmethod
    def iterate(f):
        def do(directory, *args):
            if directory is None or "files" not in directory:
                raise InvalidParameterTypeException(directory, Directory.__name__)
            copy = deepcopy(directory)
            for k, v in copy["files"].items():
                copy["files"][k] = f(v, *args)
            return copy
        return do
