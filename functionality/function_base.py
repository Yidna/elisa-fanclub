from abc import ABC as ABSTRACT_CLASS
from abc import abstractmethod
from functionality.exceptions.invalid_parameter_length_exception import InvalidParameterLengthException


class FunctionBase(ABSTRACT_CLASS):

    def __init__(self, symbol_table, parameters):
        """
        Creates an instance of the function with the given parameters
        :param symbol_table: the symbol table
        :param parameters: a tuple of parameters
        """
        self._symbol_table = symbol_table
        self._parameters = parameters
        self._param_def = self._get_param_def()

    def execute(self):
        """
        Executes the function after verifying the parameters are correct
        :return: anything
        """
        self._check_parameters()
        return self._run()

    def _get_param_def(self):
        """
        Generates the dictionary of {num_args: (typedefs)} for parameters
        :return: dict
        """
        return {
            0: ()
        }

    def _check_parameters(self):
        """
        Ensures that the parameters are valid before executing the function.
        Throws an InvalidParameterLengthException if there as an incorrect number of parameters
        Throws an InvalidParameterException if parameters are not valid.
        """
        # Check if the number of parameters is correct
        param_len = len(self._parameters)
        if not(param_len in self._param_def):
            raise InvalidParameterLengthException(self._param_def, param_len)

        # Check if the types of parameters are correct
        for i, p in enumerate(self._parameters):
            self._param_def[param_len - 1][i](p).check()

    @abstractmethod
    def _run(self):
        """
        The implementation of the function
        :return: anything
        """
        pass
