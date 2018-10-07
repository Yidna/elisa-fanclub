from functionality.exceptions import InvalidParameterValueException
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

        if w > img_w or h > img_h:
            raise InvalidParameterValueException(
                "Cropped dimensions cannot be greater than image dimensions", "({},{})".format(w, h)
            )

        x0, x1 = img_w // 2 - w // 2, img_w // 2 + w // 2
        y0, y1 = img_h // 2 - h // 2, img_h // 2 + h // 2
        img = img[y0:y1, x0:x1]
        self._symbol_table[img_name] = img
        return img
