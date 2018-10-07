from functionality.function_base import FunctionBase
from functionality.exceptions.invalid_parameter_exception import InvalidParameterException
import cv2


class Grayscale(FunctionBase):

    def __init__(self, symbol_table, parameters):
        super(Grayscale, self).__init__(symbol_table, parameters)
        self._param_length = 1

    def _check_parameters(self):
        super(Grayscale, self)._check_parameters()

        # Check if the image exists
        if self._parameters[0] in self._symbol_table:
            self.__image_name = str(self._parameters[0])
            self.__image = self._symbol_table[self.__image_name]
        else:
            raise InvalidParameterException(0, "Variable")

    def _run(self):
        self.__image = cv2.cvtColor(self.__image, cv2.COLOR_BGR2GRAY)
        self._symbol_table[self.__image_name] = self.__image
