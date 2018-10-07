class InvalidParameterValueException(Exception):
    """Raised when values for a function are invalid"""

    def __init__(self, message, value):
        msg = message if message is not None else "Invalid parameter value"
        super().__init__(msg + ": " + value)
