class InvalidParameterException(Exception):
    """Raised when parameters for a function are invalid"""

    def __init__(self, offending_index, expecting):
        self.__offending_index = offending_index
        self.__expecting = expecting

    def __str__(self):
        return "Invalid parameter #{}: expecting a {}".format(self.__offending_index, self.__expecting)
