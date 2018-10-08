from functionality.function_base import FunctionBase
from functionality.typedef import *


class Find(FunctionBase):

    def _get_param_def(self):
        print('got to check params')
        return {
            (Image, Image, Integer): self._find,
        }

    def _find(self, using_img, to_img, width):
        print('hello')
        return using_img
