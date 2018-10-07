from functionality.function_base import FunctionBase
from functionality.typedef import *

import cv2
import numpy as np


class Darken(FunctionBase):

    def _get_param_def(self):
        return {
            (Image, Integer): self._darken
        }

    def _darken(self, img_name, darken):
        """
        When we execute darken, we want to be able to adjust the gamma by 0 <= darken <= 100
        If user provides upper or lower bound we will adjust to the min and max
        :return:
        """
        if darken < 0:
            darken = 0
        if darken > 100:
            darken = 100
        img = self._symbol_table[img_name]
        img = self.adjust_gamma(img, gamma=np.abs(darken/100 - 1))

        return img

    def adjust_gamma(self, img, gamma=1.0):
        # build a lookup table mapping the pixel values [0, 255] to
        # their adjusted gamma values
        inv_gamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** inv_gamma) * 255
                          for i in np.arange(0, 256)]).astype("uint8")

        # apply gamma correction using the lookup table
        return cv2.LUT(img, table)
