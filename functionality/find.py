from functionality.function_base import FunctionBase
from functionality.typedef import *

import cv2


class Find(FunctionBase):

    def _get_param_def(self):
        print('got to check params')
        return {
            (Image, Image, Integer): self._find,
        }

    def _find(self, template, img, width):
        method = cv2.TM_CCORR_NORMED
        w, h, _ = template.shape
        res = cv2.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(img, top_left, bottom_right, 255, width)
        return img
