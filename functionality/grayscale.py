from functionality.function_base import FunctionBase
from functionality.typedef import *
import cv2


class Grayscale(FunctionBase):

    def _get_param_def(self):
        return {
            1: (Image,)
        }

    def _run(self):
        img_name = self._parameters[0]
        img = self._symbol_table[img_name]

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        self._symbol_table[img_name] = img
