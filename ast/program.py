from ast.load import LOAD
from ast.apply import APPLY
from ast.show import SHOW
from ast.save import SAVE
from ast.record import RECORD
from functionality.exceptions import IllegalInputException


class PROGRAM:

    FACTORY = {
        'load': LOAD,
        'apply': APPLY,
        'show': SHOW,
        'save': SAVE,
        'record': RECORD
    }

    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.nodes = []

    def parse(self):
        while not self.tokenizer.is_empty():
            try:
                builder = PROGRAM.FACTORY[self.tokenizer.peek()]
            except IllegalInputException:
                raise IllegalInputException('Unsupported program statement type: ' + self.tokenizer.peek())

            node = builder()
            node.parse(self.tokenizer)
            self.nodes.append(node)

    def evaluate(self):
        for node in self.nodes:
            node.evaluate()
