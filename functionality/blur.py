from functionality.function_base import FunctionBase
from functionality.typedef import *
import cv2


class Blur(FunctionBase):

    def _get_param_def(self):
        return {
            3: (Image, Integer, Integer)
        }

    def _run(self):
        img_name = str(self._parameters[0])
        x = self._parameters[1]
        y = self._parameters[2]
        img = self._symbol_table[img_name]

        img = cv2.GaussianBlur(img, (x, y), 0)
        self._symbol_table[img_name] = img
