from functionality.function_base import FunctionBase
from functionality.exceptions.invalid_parameter_exception import InvalidParameterException
import cv2


class Draw(FunctionBase):

    def __init__(self, symbol_table, parameters):
        super(Draw, self).__init__(symbol_table, parameters)
        self._param_length = 4

    def _check_parameters(self):
        super(Draw, self)._check_parameters()

        # Check if the using image exists
        if self._parameters[0] in self._symbol_table:
            self.__using_image_name = str(self._parameters[0])
            self.__using_image = self._symbol_table[self.__using_image_name]
        else:
            raise InvalidParameterException(0, "Variable")

        # Check if the to image exists
        if self._parameters[1] in self._symbol_table:
            self.__to_image_name = str(self._parameters[0])
            self.__to_image = self._symbol_table[self.__to_image_name]
        else:
            raise InvalidParameterException(1, "Variable")

        # Check if the x value is an integer
        if isinstance(self._parameters[2], int):
            self.__x = self._parameters[2]
        else:
            raise InvalidParameterException(2, "Integer")

        # Check if the y value is an integer
        if isinstance(self._parameters[3], int):
            self.__y = self._parameters[3]
        else:
            raise InvalidParameterException(3, "Integer")

    def _run(self):
        if self.__using_image.shape > self.__to_image.shape:
            img = self.__using_image
        else:
            x_offset, y_offset, _ = self.__using_image.shape
            self.__to_image[self.__x:self.__x + x_offset, self.__y:self.__y + y_offset] = self.__using_image
            img = self.__to_image

        self._symbol_table[self.__to_image_name] = img
