from libs import node

import cv2
import os


class LOAD(node.Node):
    path = None
    variable = None

    def parse(self, tokenizer):
        """
        Parses the tokenizer for a load node
        :return:
        """
        tokenizer.get_and_check_next('load')
        self.path = tokenizer.get_next()
        tokenizer.get_and_check_next('as')
        self.variable = tokenizer.get_next()
        print(self.path, self.variable)

    def evaluate(self):
        """
        Evaluates the load node
        :return:
        """
        if os.path.exists(self.path):
            pass
        else:
            raise Exception('Cannot find file path: {}'.format(self.path))
