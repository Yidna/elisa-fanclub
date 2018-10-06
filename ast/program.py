from ast.load import LOAD
from ast.apply import APPLY
from ast.show import SHOW

class PROGRAM:

    nodes = []

    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    def parse(self):
        while not self.tokenizer.is_empty():
            print(self.tokenizer.check_next() == 'load')
            if self.tokenizer.check_next() == 'load':
                node = LOAD()
                node.parse(self.tokenizer)

            if self.tokenizer.check_next() == 'apply':
                node = APPLY()
                node.parse(self.tokenizer)

            if self.tokenizer.check_next() == 'show':
                node = SHOW()
                node.parse(self.tokenizer)

            if node is not None:
                self.nodes.append(node)
            else:
                raise Exception('Unable to parse')

    def evaluate(self):
        map(lambda x: x.evaluate(), self.nodes)
