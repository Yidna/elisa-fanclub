from abc import ABC as ABSTRACT_CLASS
from abc import abstractmethod


class FunctionBase(ABSTRACT_CLASS):



    @abstractmethod
    def __init__(self, parameters):
        """
        Creates an instance of the function with the given parameters
        :param parameters: a tuple of parameters
        """
        self.parameters = parameters

    @abstractmethod
    def _parameters_valid(self):
        """
        Ensures that the parameters are valid before executing the function
        :return: true or false
        """
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
        if self._parameters_valid():
            return self._run()
        else:
            raise Exception("Invalid parameters for executing: " + self.__class__.__name__)


