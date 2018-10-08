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

    def _param_def_to_str(self):
        # To log possible param_defs.
        res = ""
        for t in self._param_def:
            res += "("
            for param_type in t:
                if res[-1] is not "(":
                    res += ", "
                res += param_type.__name__
            res += ") or "
        return res[:-4]

    def _maybe_cast_types(self, types):
        maybe_casts = [expected_type(self._symbol_table, value) for expected_type, value in zip(types, self._parameters)]
        if all([val.check() for val in maybe_casts]):
            return tuple([val.cast() for val in maybe_casts])
        else:
            return None

    def _check_parameters(self):
        """
        Ensures that the parameters are valid types before executing the function.
        Throws InvalidParameterLengthException and InvalidParameterTypeException.
        """
        param_len = len(self._parameters)
        possible_params = [p for p in self._param_def if len(p) == param_len]

        if len(possible_params) == 0:
            raise InvalidParameterLengthException(self._param_def_to_str(), param_len)

        for types_tuple in possible_params:
            casted = self._maybe_cast_types(types_tuple)
            if casted is not None:
                self._parameters = casted
                self._run = self._param_def[types_tuple]
                return

        raise InvalidParameterTypeException(self._parameters, self._param_def_to_str())
