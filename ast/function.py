from libs import node
from libs import symbol_table as st
import cv2
import numpy as np


class FUNCTION(node.Node):
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
            self.parameters = int(param_1)

        tokenizer.get_and_check_next('to')
        self.to_variable = tokenizer.get_next()

    def evaluate(self):
        img = None

        if self.func_name == 'blur':
            if not self.using_variable:
                img = st.symbol_table[str(self.to_variable)]
                # TODO: Use parameter to adjust blur not just set to a 13x13 gaussian filter
                img = cv2.GaussianBlur(img, (13, 13), 0)
                st.symbol_table[str(self.to_variable)] = img
            else:
                raise NotImplementedError('Can you really blur with something onto something?')

        if self.func_name == 'draw':
            if type(self.parameters) is int:
                raise AssertionError('Draw must have two arguments')

            x, y = self.parameters

            using_img = st.symbol_table[self.using_variable]
            to_img = st.symbol_table[self.to_variable]
            if using_img.shape > to_img.shape:
                img = using_img
            else:
                x_offset, y_offset, _ = using_img.shape
                to_img[x:x+x_offset, y:y+y_offset] = using_img
                img = to_img

            st.symbol_table[self.to_variable] = img

        if self.func_name == 'darken':
            if type(self.parameters) is not int:
                raise AssertionError('You can only darken with one value')
            img = st.symbol_table[self.to_variable]
            # TODO
            st.symbol_table[self.to_variable] = img

        if self.func_name == 'brighten':
            img = st.symbol_table[self.to_variable]
            img = self.increase_brightness(img, self.parameters)
            st.symbol_table[self.to_variable] = img

        if self.func_name == 'gray':
            img = st.symbol_table[self.to_variable]
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            st.symbol_table[self.to_variable] = img

        if self.func_name == 'resize':
            pass

        if self.func_name == 'find':
            pass

        if self.func_name == 'crop':
            pass

        if self.func_name == 'tile':
            pass

        return img

    def increase_brightness(self, img, value):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)

        lim = 255 - value
        v[v > lim] = 255
        v[v <= lim] += value

        final_hsv = cv2.merge((h, s, v))
        img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        return img
