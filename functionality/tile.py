from functionality.function_base import FunctionBase
from functionality.typedef import *
import numpy as np


class Tile(FunctionBase):

    def _get_param_def(self):
        return {
            (Image, Integer, Integer): self._tile
        }

    def _tile(self, img, x, y):
        return np.tile(img, (x, y, 1))
