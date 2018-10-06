from ast.load import LOAD
from ast.apply import APPLY
from ast.show import SHOW


class PROGRAM:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.nodes = []

    def parse(self):
        while not self.tokenizer.is_empty():
            if self.tokenizer.check_next('load'):
                node = LOAD()
            elif self.tokenizer.check_next('apply'):
                node = APPLY()
            elif self.tokenizer.check_next('show'):
                node = SHOW()

            if node is not None:
                node.parse(self.tokenizer)
                self.nodes.append(node)
            else:
                raise Exception('Unable to parse')

    def evaluate(self):
        for node in self.nodes:
            node.evaluate()
