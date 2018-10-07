from functionality.function_base import FunctionBase
from functionality.typedef import *
import cv2


class Blur(FunctionBase):

    def _get_param_def(self):
        return {
            (Image, Integer, Integer): self._blur
        }

    def _blur(self, img_name, x, y):
        img = self._symbol_table[img_name]

        img = cv2.GaussianBlur(img, (x, y), 0)

        return img
