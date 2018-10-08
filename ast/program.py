from ast.load import LOAD
from ast.apply import APPLY
from ast.show import SHOW
from ast.save import SAVE
from ast.record import RECORD
from functionality.exceptions import IllegalInputException


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
            elif self.tokenizer.check_next('record'):
                node = RECORD()
            else:
                raise IllegalInputException('Unsupported program statement type: ' + self.tokenizer.peek())

            node.parse(self.tokenizer)
            self.nodes.append(node)

    def evaluate(self):
        for node in self.nodes:
            node.evaluate()
