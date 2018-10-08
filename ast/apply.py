from functionality import *
from functionality.exceptions import IllegalInputException
from libs import node
from libs import symbol_table as st
from libs import utils


class APPLY(node.Node):
    FUNC_MAP = {
        'blur': Blur,
        'draw': Draw,
        'darken': Darken,
        'brighten': Brighten,
        'grayscale': Grayscale,
        'resize': Resize,
        # TODO: implement find
        'crop': Crop
        # TODO: implement tile
    }
    parameters = []
    to_variables = []
    as_variables = []
    func_name = None
    func = None
    using_variable = None

    def parse(self, tokenizer):
        tokenizer.get_and_check_next('apply')
        self.func_name = tokenizer.get_and_check_next(self.FUNC_MAP)
        print("Parsing " + self.func_name + "...")

        if tokenizer.maybe_match_next('using'):
            self.using_variable = tokenizer.get_next()

        if tokenizer.maybe_match_next('with'):
            self.parameters = utils.parse_array_params(tokenizer)
        else:
            self.parameters = []

        tokenizer.get_and_check_next('to')
        self.to_variables = utils.parse_array_params(tokenizer)

        if tokenizer.maybe_match_next('as'):
            self.as_variables = utils.parse_array_params(tokenizer)

        if len(self.as_variables) > 0 and len(self.as_variables) != len(self.to_variables):
            raise IllegalInputException("Cardinality mismatch in AS and TO")

        # print(self.using_variable)
        # print(self.to_variables)
        # print(self.as_variables)

    def evaluate(self):
        res = []
        func_type = self.FUNC_MAP[self.func_name]

        for idx, to_variable in enumerate(self.to_variables):
            raw_params = [self.using_variable, to_variable, *self.parameters]
            params = [p for p in raw_params if p is not None]
            res.append(func_type(st.symbol_table, params).execute())

            if len(self.as_variables) == 0:
                st.symbol_table[to_variable] = res[-1]
            else:
                st.symbol_table[self.as_variables[idx]] = res[-1]

        return res
