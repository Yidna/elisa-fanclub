class InvalidParameterTypeException(Exception):
    """Raised when parameters for a function are invalid"""

    def __init__(self, offending_value, expecting):
        self.__offending_value = offending_value
        self.__expecting = expecting

    def __str__(self):
        return "Invalid parameter '{}': expecting a value of type '{}'".format(self.__offending_value, self.__expecting)
