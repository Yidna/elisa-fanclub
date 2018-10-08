from functionality.function_base import FunctionBase
from functionality.typedef import *
import cv2


class Resize(FunctionBase):

    def _get_param_def(self):
        return {
            (Image, Integer): self._resize,
            (Image, Integer, Integer): self._resize,
            (Directory, Integer): Directory.iterate(self._resize),
            (Directory, Integer, Integer): Directory.iterate(self._resize),
        }

    def _resize(self, img, x_scale, y_scale=None):
        if y_scale is None:
            y_scale = x_scale

        y, x = img.shape[:2]
        x, y = x * x_scale // 100, y * y_scale // 100
        img = cv2.resize(img, (x, y), interpolation=cv2.INTER_CUBIC)

        return img
