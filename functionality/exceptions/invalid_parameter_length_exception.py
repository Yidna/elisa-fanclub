class InvalidParameterLengthException(Exception):
    """Raised when the number parameters for a function is not correct"""

    def __init__(self, expected_lengths, actual_length):
        self.__expected_lengths = expected_lengths
        self.__actual_length = actual_length

    def __str__(self):
        return "Invalid parameter count#" + self.__actual_length + ": expecting " + self.__expected_lengths
