from functionality.function_base import FunctionBase
from functionality.exceptions.invalid_parameter_exception import InvalidParameterException
import cv2


class Brighten(FunctionBase):

    def __init__(self, symbol_table, parameters):
        super(Brighten, self).__init__(symbol_table, parameters)
        self._param_length = 2

    def _check_parameters(self):
        super(Brighten, self)._check_parameters()

        # Check if the image exists
        if self._parameters[0] in self._symbol_table:
            self.__image_name = str(self._parameters[0])
            self.__image = self._symbol_table[self.__image_name]
        else:
            raise InvalidParameterException(0, "Variable")

        # Check if the brighten value is an integer
        if isinstance(self._parameters[1], int):
            self.__amount = self._parameters[1]
        else:
            raise InvalidParameterException(1, "Integer")

    def _run(self):
        hsv = cv2.cvtColor(self.__image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        lim = 255 - self.__amount
        v[v > lim] = 255
        v[v <= lim] += self.__amount

        final_hsv = cv2.merge((h, s, v))
        self.__image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        self._symbol_table[self.__image_name] = self.__image
