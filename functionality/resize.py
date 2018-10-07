from functionality.function_base import FunctionBase
from functionality.exceptions.invalid_parameter_exception import InvalidParameterException
import cv2


class Resize(FunctionBase):

    def __init__(self, symbol_table, parameters):
        super(Resize, self).__init__(symbol_table, parameters)
        self._param_length = (3,)

    def _check_parameters(self):
        super(Resize, self)._check_parameters()

        # Check if the image exists
        if self._parameters[0] in self._symbol_table:
            self.__image_name = str(self._parameters[0])
            self.__image = self._symbol_table[self.__image_name]
        else:
            raise InvalidParameterException(0, "Variable")

        # Check if the resize value is a tuple of 1 or 2 integers
        param = self._parameters[1]
        if isinstance(param, tuple) and 0 < param.length <= 2 and all(isinstance(value, int) for value in param):
            self.__x_scale, self.__y_scale = param if param.length == 2 else (param[0],) * 2
        else:
            raise InvalidParameterException(1, "[1, 2]-Integer Tuple")

    def _run(self):
        x, y = self.__image.shape[:2]
        x, y = x * self.__x_scale // 100, y * self.__y_scale // 100
        self.__image = cv2.resize(self.__image, (x, y), interpolation=cv2.INTER_CUBIC)
        self._symbol_table[self.__image_name] = self.__image
