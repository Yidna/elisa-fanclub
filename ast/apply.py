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

    def _do_preset(self):
        func_list = pt.preset_table[self.preset_name]

        def fn(to_variable):
            curr_result = None
            orig = st.symbol_table[to_variable].copy()
            for func in func_list:
                params = self._flatten(func["using"], to_variable, *func["params"])
                curr_result = self._get_function(func["name"], params).execute()
                st.symbol_table[to_variable] = curr_result
            st.symbol_table[to_variable] = orig
            return curr_result
        return fn

    def _do_function(self, to_variable):
        params = self._flatten(self.using_variable, to_variable, *self.parameters)
        return self._get_function(self.func_name, params).execute()

    def evaluate(self):
        fn = self._do_preset() if self.preset_name else self._do_function
        print("Applying {} to {}".format(
            self.func_name if self.func_name else self.preset_name,
            str(self.to_variables).replace("'", "")
        ))

        for idx, var in enumerate(self.to_variables):
            modified_img = fn(var)
            if self.as_variables:
                st.symbol_table[self.as_variables[idx]] = modified_img

    @staticmethod
    def _get_function(name, params):
        return ft.FUNC_TABLE.get(name)(st.symbol_table, params)

    @staticmethod
    def _flatten(*collection):
        return list(filter(None, collection))
