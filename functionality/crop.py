from functionality.exceptions import InvalidParameterValueException
from functionality.function_base import FunctionBase
from functionality.typedef import *


class Crop(FunctionBase):

    def _get_param_def(self):
        return {
            (Image, Integer, Integer): self._crop,
            (Directory, Integer, Integer): Directory.iterate(self._crop)
        }

    def _crop(self, img, w, h):
        img_h, img_w = img.shape[:2]

        if w > img_w or h > img_h:
            raise InvalidParameterValueException((w, h), "dimensions smaller than image dimensions")

        x0, x1 = img_w // 2 - w // 2, img_w // 2 + w // 2
        y0, y1 = img_h // 2 - h // 2, img_h // 2 + h // 2
        img = img[x0:x1, y0:y1]
        
        return img
