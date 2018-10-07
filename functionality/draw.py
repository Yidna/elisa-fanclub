from functionality.function_base import FunctionBase
from functionality.typedef import *


class Draw(FunctionBase):

    def _get_param_def(self):
        return {
            (Image, Image, Integer, Integer): self._draw
        }

    def _draw(self, u_img_name, t_img_name, x, y):
        u_img = self._symbol_table[u_img_name]
        t_img = self._symbol_table[t_img_name]

        if u_img.shape > t_img.shape:
            img = u_img
        else:
            x_offset, y_offset, _ = u_img.shape
            t_img[x:x + x_offset, y:y + y_offset] = u_img
            img = t_img

        self._symbol_table[t_img_name] = img
        return img
