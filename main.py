from libs.tokenizer import Tokenizer

from ast.program import PROGRAM

tokenizer = None
symbol_table = {}

if __name__ == '__main__':
    tokenizer = Tokenizer('input.cvdsl')
    tokenizer.tokenize()
    program = PROGRAM(tokenizer)
    print("\n== PARSE ==")
    program.parse()
    print("\n== EVALUATE ==")
    program.evaluate()
