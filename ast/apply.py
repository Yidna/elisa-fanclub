from libs import node
from ast.function import FUNCTION
from libs import symbol_table as st
from matplotlib import pyplot as plt

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
        img = self.func.evaluate()
        if self.variable:
            st.symbol_table[self.variable] = img
