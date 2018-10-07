class InvalidParameterLengthException(Exception):
    """Raised when the number parameters for a function is not correct"""

    def __init__(self, expected_length, actual_length):
        self.__expected_length = expected_length
        self.__actual_length = actual_length

    def __str__(self):
        return "Invalid parameter count#" + self.__actual_length + ": expecting " + self.__expected_length
