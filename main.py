from libs.tokenizer import Tokenizer

from ast.program import PROGRAM

tokenizer = None
symbol_table = {}

if __name__ == '__main__':
    functions = ['darken', 'brighten', 'resize', 'find', 'draw', 'hybrid']
    literals = ['load', 'save', 'apply']
    literals = literals + functions
    tokenizer = Tokenizer('input.cvdsl', literals)
    tokenizer.tokenize()
    program = PROGRAM(tokenizer=tokenizer)
    program.parse()
    program.evaluate()
