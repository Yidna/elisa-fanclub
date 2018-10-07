from functionality.function_base import FunctionBase
from functionality.typedef import *
import cv2


class Grayscale(FunctionBase):

    def _get_param_def(self):
        return {
            (Image,): self._grayscale
        }

    def _grayscale(self, img_name):
        img = self._symbol_table[img_name]

        return img
