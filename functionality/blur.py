from functionality.function_base import FunctionBase
from functionality.exceptions.invalid_parameter_exception import InvalidParameterException
import cv2


class Blur(FunctionBase):

    def __init__(self, symbol_table, parameters):
        super(Blur, self).__init__(symbol_table, parameters)
        self._param_length = (3,)

    def _check_parameters(self):
        super(Blur, self)._check_parameters()

        # Check if the image exists
        if self._parameters[0] in self._symbol_table:
            self.__image_name = str(self._parameters[0])
            self.__image = self._symbol_table[self.__image_name]
        else:
            raise InvalidParameterException(0, "Variable")

        # Check if parameters for the blur are valid
        if isinstance(self._parameters[1], int):
            self.__x = self._parameters[1]
        else:
            raise InvalidParameterException(1, "Integer")

        if isinstance(self._parameters[2], int):
            self.__y = self._parameters[2]
        else:
            raise InvalidParameterException(2, "Integer")

    def _run(self):
        self.__image = cv2.GaussianBlur(self.__image, (self.__x, self.__y), 0)
        self._symbol_table[self.__image_name] = self.__image
