from libs import node
import cv2


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
            self.parameters.extend([int(param_1[:-1]), int(tokenizer.get_next())])
        else:
            self.parameters.append(int(param_1))

        tokenizer.get_and_check_next('to')
        self.to_variable = tokenizer.get_next()

    def evaluate(self):
        pass