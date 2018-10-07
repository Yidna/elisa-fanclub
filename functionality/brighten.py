from functionality.function_base import FunctionBase
from functionality.typedef import *
import cv2


class Brighten(FunctionBase):

    def _get_param_def(self):
        return {
            (Image, Integer): self._brighten
        }

    def _brighten(self, img, amount):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        lim = 255 - amount
        v[v > lim] = 255
        v[v <= lim] += amount

        final_hsv = cv2.merge((h, s, v))
        img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

        return img
