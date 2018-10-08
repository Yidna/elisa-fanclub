from functionality.exceptions import InvalidParameterValueException
from functionality.function_base import FunctionBase
from functionality.typedef import *
import cv2


class Blur(FunctionBase):

    def _get_param_def(self):
        return {
            (Image, Integer, Integer): self._blur,
            (Directory, Integer, Integer): self._blur_all
        }

    def _blur_all(self, dir, x, y):
        for k, v in dir["files"].items():
            dir["files"][k] = self._blur(v, x, y)
        return dir

    def _blur(self, img, x, y):
        if self._validate_int(x) and self._validate_int(y):
            img = cv2.GaussianBlur(img, (x, y), 0)
            return img
        raise InvalidParameterValueException("Blur parameters must be positive and odd", str((x, y)))

    @staticmethod
    def _validate_int(i): return i > 0 and i % 2 == 1
