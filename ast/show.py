from libs.node import Node


class SHOW(Node):

    variable = None

    def parse(self, tokenizer):
        tokenizer.get_and_check_next('show')
        self.variable = tokenizer.get_next()

    def evaluate(self):
        pass