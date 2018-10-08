from functionality.exceptions import IllegalInputException
from libs import func_table as ft
from libs import node
from libs import preset_table as pt
from libs import symbol_table as st
from libs import utils


class APPLY(node.Node):
    parameters = []
    to_variables = []
    as_variables = []
    func_name = None
    func = None
    using_variable = None
    preset_name = None

    def parse(self, tokenizer):
        tokenizer.get_and_check_next('apply')
        if tokenizer.check_next(pt.preset_table):
            self.preset_name = tokenizer.get_next()
        else:
            try:
                self.func_name = tokenizer.get_and_check_next(ft.FUNC_TABLE)
            except IllegalInputException:
                raise IllegalInputException("Call to unsupported function '{}'.".format(tokenizer.peek()))

        func = self.func_name if self.func_name else self.preset_name
        print("Parsing {}...".format(func))

        if self.preset_name is None:
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
        func_type = ft.FUNC_TABLE.get(self.func_name)
        print("Applying {} to {}".format(
            self.func_name if self.func_name else self.preset_name,
            str(self.to_variables).replace("'", "")
        ))

        for idx, to_variable in enumerate(self.to_variables):
            if self.preset_name is None:
                raw_params = [self.using_variable, to_variable, *self.parameters]
                params = [p for p in raw_params if p is not None]
                res.append(func_type(st.symbol_table, params).execute())
            else:
                func_list = pt.preset_table[self.preset_name]
                orig = st.symbol_table[to_variable].copy()
                curr_result = None

                for func in func_list:
                    raw_params = [func["using"], to_variable, *func["params"]]
                    params = [p for p in raw_params if p is not None]
                    curr_result = ft.FUNC_TABLE[func["name"]](st.symbol_table, params).execute()
                    st.symbol_table[to_variable] = curr_result

                res.append(curr_result)
                st.symbol_table[to_variable] = orig

            if len(self.as_variables) == 0:
                st.symbol_table[to_variable] = res[-1]
            else:
                st.symbol_table[self.as_variables[idx]] = res[-1]

        return res
