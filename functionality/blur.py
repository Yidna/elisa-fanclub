from functionality.function_base import FunctionBase
from functionality.typedef import *
import cv2


class Blur(FunctionBase):

    def _get_param_def(self):
        return {
            (Image, Integer, Integer): self._blur
        }

    def _blur(self, img, x, y):
        img = cv2.GaussianBlur(img, (x, y), 0)

        return img
