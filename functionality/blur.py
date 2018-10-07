from functionality.function_base import FunctionBase
from functionality.exceptions.invalid_parameter_exception import InvalidParameterException
import cv2


class Blur(FunctionBase):

    def __init__(self, symbol_table, parameters):
        super(Blur, self).__init__(symbol_table, parameters)
        self._param_length = (2,)

    def _check_parameters(self):
        super(Blur, self)._check_parameters()

        # Check if the image exists
        if self._parameters[0] in self._symbol_table:
            self.__image_name = str(self._parameters[0])
            self.__image = self._symbol_table[self.__image_name]
        else:
            raise InvalidParameterException(0, "Variable")

        # Check if parameters for the blur are valid
        param = self._parameters[1]
        if isinstance(param, tuple) and len(param) == 2 and all(isinstance(value, int) for value in param):
            self.__filter = self._parameters[1]
        else:
            raise InvalidParameterException(1, "2-Integer Tuple")

    def _run(self):
        self.__image = cv2.GaussianBlur(self.__image, self.__filter, 0)
        self._symbol_table[self.__image_name] = self.__image
