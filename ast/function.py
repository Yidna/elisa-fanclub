from libs import node
import cv2


class FUNCTION(node.Node):

    func_name = None
    using_variable = None
    parameters = None
    to_variable = None

    def parse(self, tokenizer):
        pass

    def evaluate(self):
        pass