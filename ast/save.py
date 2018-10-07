from libs.node import Node
from libs.symbol_table import symbol_table as st
import cv2


class SAVE(Node):
    variable = None
    path = None

    def parse(self, tokenizer):
        save = tokenizer.get_and_check_next('save')
        print("Parsing " + save + "...")
        self.variable = tokenizer.get_next()
        tokenizer.get_and_check_next('as')
        self.path = tokenizer.get_next().strip('\'\'')

    def evaluate(self):
        img = st[self.variable]
        cv2.imwrite(self.path, img)

