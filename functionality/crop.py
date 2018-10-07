from functionality.function_base import FunctionBase
from functionality.exceptions.invalid_parameter_exception import InvalidParameterException
import cv2


class Crop(FunctionBase):

    def __init__(self, symbol_table, parameters):
        super(Crop, self).__init__(symbol_table, parameters)
        self._param_length = (3,)

    def _check_parameters(self):
        super(Crop, self)._check_parameters()

        # Check if the image exists
        if self._parameters[0] in self._symbol_table:
            self.__image_name = str(self._parameters[0])
            self.__image = self._symbol_table[self.__image_name]
        else:
            raise InvalidParameterException(0, "Variable")

        # Check if the width value is an integer
        if isinstance(self._parameters[1], int):
            self.__w = self._parameters[1]
        else:
            raise InvalidParameterException(1, "Integer")

        # Check if the height value is an integer
        if isinstance(self._parameters[2], int):
            self.__h = self._parameters[2]
        else:
            raise InvalidParameterException(2, "Integer")

    def _run(self):
        img_w, img_h = self.__image.shape[:2]
        x0, x1 = img_w // 2 - self.__w // 2, img_w // 2 + self.__w // 2
        y0, y1 = img_h // 2 - self.__h // 2, img_h // 2 + self.__h // 2
        self.image = self.image[x0:x1, y0:y1]
        self._symbol_table[self.__image_name] = self.image
