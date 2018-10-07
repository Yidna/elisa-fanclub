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
        self.func_name = tokenizer.get_next()

        if tokenizer.get_and_check_next('using'):
            self.using_variable = tokenizer.get_next()

        tokenizer.get_and_check_next('with')
        param_1 = tokenizer.get_next()
        if param_1[-1] == ',':
            # self.parameters.extend([int(param_1[:-1]), int(tokenizer.get_next())])
            self.parameters = (int(param_1[:-1]), int(tokenizer.get_next()))
        else:
            self.parameters = (int(param_1),)

        tokenizer.get_and_check_next('to')
        self.to_variable = tokenizer.get_next()

    def evaluate(self):
        func_type = None
        if self.func_name == 'blur':
            func_type = Blur
        if self.func_name == 'draw':
            func_type = Draw
        if self.func_name == 'darken':
            func_type = Darken
        if self.func_name == 'brighten':
            func_type = Brighten
        if self.func_name == 'grayscale':
            func_type = Grayscale
        if self.func_name == 'resize':
            func_type = Resize
        if self.func_name == 'crop':
            func_type = Crop

        raw_params = [self.using_variable, self.to_variable, *self.parameters]
        params = [p for p in raw_params if p is not None]
        func = func_type(st.symbol_table, params)
        return func.execute()