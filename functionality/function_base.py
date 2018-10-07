from functionality.exceptions import *


class FunctionBase:

    def __init__(self, symbol_table, parameters):
        """
        Creates an instance of the function with the given parameters
        :param symbol_table: the symbol table
        :param parameters: a tuple of parameters
        """
        self._symbol_table = symbol_table
        self._parameters = parameters
        self._param_def = self._get_param_def()
        self._run = None

    def execute(self):
        """
        Executes the function after verifying the parameters are correct
        :return: anything
        """
        self._check_parameters()
        return self._run(*self._parameters)

    def _get_param_def(self):
        """
        Generates the dictionary of {num_args: (typedefs)} for parameters
        :return: dict
        """
        return {
            (): None
        }

    def _check_parameters(self):
        """
        Ensures that the parameters are valid before executing the function.
        Throws an InvalidParameterLengthException if there as an incorrect number of parameters
        Throws an InvalidParameterException if parameters are not valid.
        """
        # Check if the number of parameters is correct
        param_len = len(self._parameters)
        param_options = tuple(p for p in self._param_def if len(p) == param_len)
        if len(param_options) == 0:
            raise InvalidParameterLengthException(self._param_def, param_len)

        parse_dict = {}
        for option in param_options:
            parse_dict[option] = []
            for i, p in enumerate(self._parameters):
                try:
                    parse_dict[option].append(option[i](self._symbol_table, p).check())
                except InvalidParameterException as e:
                    parse_dict[option].append(e)

        least_offended = None
        least_offended_count = None
        for option, params in parse_dict.items():
            invalid_count = sum(p for p in params if isinstance(p, InvalidParameterException))
            if invalid_count == 0:
                self._parameters = params
                self._run = self._param_def[option]
                return
            if least_offended is None or invalid_count < least_offended_count:
                least_offended_count = invalid_count
                least_offended = option

        raise InvalidParameterException(self._parameters, least_offended)
