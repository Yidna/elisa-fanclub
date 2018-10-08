import cv2
from matplotlib import pyplot as plt
from numpy import ndarray

import libs.symbol_table as st
from functionality.exceptions import IllegalInputException
from libs.node import Node


class SHOW(Node):
    variable = None

    def parse(self, tokenizer):
        tokenizer.get_and_check_next('show')
        self.variable = tokenizer.get_next()

    def evaluate(self):
        symbol = st.symbol_table[self.variable]

        if isinstance(symbol, ndarray):
            print("> Showing image: {}".format(self.variable))
            files = [symbol]
        elif "files" in symbol:  # directory
            print("> Showing folder: {}".format(self.variable))
            files = list(symbol["files"].values())
        else:
            raise IllegalInputException("The symbol ({}: {}) cannot be shown.".format(self.variable, symbol))

        for img in files:
            plt.figure()
            plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            plt.show()
