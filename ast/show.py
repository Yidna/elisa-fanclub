from libs.node import Node
import libs.symbol_table as st
import cv2
from matplotlib import pyplot as plt


class SHOW(Node):
    variable = None

    def parse(self, tokenizer):
        tokenizer.get_and_check_next('show')
        self.variable = tokenizer.get_next()

    def evaluate(self):
        img = st.symbol_table[self.variable]
        if len(img.shape) == 3:
            plt.figure()
            plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            plt.show()
        else:
            plt.figure()
            plt.imshow(img, cmap='gray')
            plt.show()
