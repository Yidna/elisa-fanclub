from functionality.function_base import FunctionBase
from functionality.typedef import *


class Draw(FunctionBase):

    def _get_param_def(self):
        return {
            4: (Image, Image, Integer, Integer)
        }

    def _run(self):
        u_img_name = self._parameters[0]
        t_img_name = self._parameters[1]
        x = self._parameters[2]
        y = self._parameters[3]
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