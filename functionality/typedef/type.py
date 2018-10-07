from abc import ABC as ABSTRACT_CLASS
from abc import abstractmethod
from functionality.exceptions.invalid_parameter_exception import InvalidParameterException


class Type(ABSTRACT_CLASS):

    def __init__(self, symbol_table, value):
        self._symbol_table = symbol_table
        self._value = value

    def check(self):
        if not self._check():
            raise InvalidParameterException(self._value, self.__class__.__name__)
        return self._cast()

    @abstractmethod
    def _check(self):
        pass

    @abstractmethod
    def _cast(self):
        pass
