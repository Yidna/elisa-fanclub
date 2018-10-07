from functionality.function_base import FunctionBase
from functionality.typedef import *


class Crop(FunctionBase):

    def _get_param_def(self):
        return {
            3: (Image, Integer, Integer)
        }

    def _run(self):
        img_name = self._parameters[0]
        w = self._parameters[1]
        h = self._parameters[2]
        img = self._symbol_table[img_name]

        img_h, img_w = img.shape[:2]
        x0, x1 = img_w // 2 - w // 2, img_w // 2 + w // 2
        y0, y1 = img_h // 2 - h // 2, img_h // 2 + h // 2
        img = img[x0:x1, y0:y1]
        self._symbol_table[img_name] = img
        return img
