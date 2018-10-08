from functionality.function_base import FunctionBase
from functionality.typedef import *


class Draw(FunctionBase):

    def _get_param_def(self):
        return {
            (Image, Image, Integer, Integer): self._draw,
            (Image, Directory, Integer, Integer): self._draw_on_all
        }

    def _draw_on_all(self, img, folder, x, y):
        from copy import deepcopy
        copy = deepcopy(folder)
        for k, v in copy["files"].items():
            copy["files"][k] = self._draw(img, v, x, y)
        return copy

    def _draw(self, u_img, t_img, x, y):
        if u_img.shape >= t_img.shape:
            img = u_img
        else:
            x_offset, y_offset, _ = u_img.shape
            t_img[x:x + x_offset, y:y + y_offset] = u_img
            img = t_img

        return img
