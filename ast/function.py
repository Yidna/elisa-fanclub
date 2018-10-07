from libs import node
from libs import symbol_table as st
from functionality import *
from scipy import signal
import cv2
import numpy as np


class FUNCTION(node.Node):
    FUNC_MAP = {
        'blur': Blur,
        'draw': Draw,
        'darken': Darken,
        'brighten': Brighten,
        'grayscale': Grayscale,
        'resize': Resize,
        # TODO: implement find
        'crop': Crop
        # TODO: implement tile
    }
    func_name = None
    using_variable = None
    parameters = []
    to_variable = None

    def parse(self, tokenizer):
        self.func_name = tokenizer.get_and_check_next(self.FUNC_MAP)

        if tokenizer.get_and_check_next('using'):
            self.using_variable = tokenizer.get_next()

        if tokenizer.get_and_check_next('with'):
            param_1 = tokenizer.get_next()
            if param_1[-1] == ',':
                # self.parameters.extend([int(param_1[:-1]), int(tokenizer.get_next())])
                self.parameters = (param_1[:-1], tokenizer.get_next())
            else:
                self.parameters = (param_1,)
        else:
            self.parameters = ()

        tokenizer.get_and_check_next('to')
        self.to_variable = tokenizer.get_next()

    def evaluate(self):
        func_type = self.FUNC_MAP[self.func_name]
        raw_params = [self.using_variable, self.to_variable, *self.parameters]
        params = [p for p in raw_params if p is not None]
        func = func_type(st.symbol_table, params)
        return func.execute()
