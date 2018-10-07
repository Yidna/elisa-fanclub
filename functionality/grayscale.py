from functionality.function_base import FunctionBase
from functionality.typedef import *
import cv2


class Grayscale(FunctionBase):

    def _get_param_def(self):
        return {
            (Image,): self._grayscale
        }

    def _grayscale(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        return img
