from functionality.function_base import FunctionBase
from functionality.typedef import *
import cv2


class Resize(FunctionBase):

    def _get_param_def(self):
        return {
            2: (Image, Integer),
            3: (Image, Integer, Integer)
        }

    def _run(self):
        img_name = self._parameters[0]
        x_scale = self._parameters[1]
        y_scale = self._parameters[2] if len(self._parameters) == 2 else x_scale
        img = self._symbol_table[img_name]

        y, x = img.shape[:2]
        x, y = x * x_scale // 100, y * y_scale // 100
        img = cv2.resize(img, (x, y), interpolation=cv2.INTER_CUBIC)
        self._symbol_table[img_name] = img
        return img
