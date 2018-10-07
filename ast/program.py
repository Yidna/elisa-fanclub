from ast.load import LOAD
from ast.apply import APPLY
from ast.show import SHOW
from ast.save import SAVE


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
            elif self.tokenizer.check_next('save'):
                node = SAVE()
            else:
                raise Exception('Unsupported program statement type: ' + self.tokenizer.peek())

            node.parse(self.tokenizer)
            self.nodes.append(node)

    def evaluate(self):
        for node in self.nodes:
            node.evaluate()
