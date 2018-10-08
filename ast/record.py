from functionality.exceptions import IllegalInputException
from libs import node
from libs import preset_table as pt
from libs import func_table as ft
from libs import utils


class RECORD(node.Node):
    name = None
    preset = []

    def parse(self, tokenizer):
        tokenizer.get_and_check_next('record')

        while tokenizer.peek() != 'as':
            curr = {"name": None, "using": None, "params": []}
            func_name = tokenizer.get_next()

            if func_name not in ft.FUNC_TABLE:
                raise IllegalInputException("Cannot save a record with a non-library function")
            curr["name"] = func_name

            if tokenizer.maybe_match_next('using'):
                curr["using"] = tokenizer.get_next()

            if tokenizer.maybe_match_next('with'):
                curr["params"] = utils.parse_array_params(tokenizer, True)

            self.preset.append(curr)

        if len(self.preset) == 0:
            raise IllegalInputException("Record must have at least one function")

        tokenizer.get_and_check_next('as')
        self.name = tokenizer.get_next()
        pt.preset_table[self.name] = self.preset
        prefix = '\n ' + ' ' * len(self.name)
        print(self.name, prefix.join(map(str, self.preset)))

    def evaluate(self):
        pass
