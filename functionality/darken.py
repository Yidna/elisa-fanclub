from functionality.function_base import FunctionBase
from functionality.exceptions.invalid_parameter_exception import InvalidParameterException
import cv2


class Darken(FunctionBase):

    def __init__(self, symbol_table, parameters):
        super(Darken, self).__init__(symbol_table, parameters)
        self._param_length = 2

    def _check_parameters(self):
        super(Darken, self)._check_parameters()

        # Check if the image exists
        if self._parameters[0] in self._symbol_table:
            self.__image_name = str(self._parameters[0])
            self.__image = self._symbol_table[self.__image_name]
        else:
            raise InvalidParameterException(0, "Variable")

        # Check if the darken value is an integer
        if isinstance(self._parameters[1], int):
            self.__amount = self._parameters[1]
        else:
            raise InvalidParameterException(1, "Integer")

    def _run(self):
        # TODO
        pass
