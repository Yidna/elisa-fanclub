from libs import node
from ast.function import FUNCTION
import cv2


class APPLY(node.Node):
    func = None
    variable = None

    def parse(self, tokenizer):
        tokenizer.get_and_check_next('apply')
        self.func = FUNCTION()
        self.func.parse(tokenizer)
        if tokenizer.get_and_check_next('as'):
            self.variable = tokenizer.get_next()

    def evaluate(self):
        pass
