from functionality.function_base import FunctionBase
from functionality.typedef import *


class Crop(FunctionBase):

    def _get_param_def(self):
        return {
            (Image, Integer, Integer): self._crop
        }

    def _crop(self, img_name, w, h):
        img = self._symbol_table[img_name]

        img_h, img_w = img.shape[:2]
        x0, x1 = img_w // 2 - w // 2, img_w // 2 + w // 2
        y0, y1 = img_h // 2 - h // 2, img_h // 2 + h // 2
        img = img[x0:x1, y0:y1]
        self._symbol_table[img_name] = img
        return img
