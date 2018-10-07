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
        self._param_length = (0,)

    def _check_parameters(self):
        """
        Ensures that the parameters are valid before executing the function.
        Throws an InvalidParameterLengthException if there as an incorrect number of parameters
        Throws an InvalidParameterException if parameters are not valid.
        Loads parameters into private variables if needed.
        """
        # Check if the number of parameters is correct
        if not(self._parameters.length in self._param_length):
            raise InvalidParameterLengthException(self._param_length, self._parameters.length)
        pass

    @abstractmethod
    def _run(self):
        """
        The implementation of the function
        :return: anything
        """
        pass

    def execute(self):
        """
        Executes the function after verifying the parameters are correct
        :return: anything
        """
        self._check_parameters()
        self._run()
