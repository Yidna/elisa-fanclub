import re # Python regex library


class Tokenizer():
    def __init__(self):
        # Constructor
        pass

    def tokenize(self):
        """
        Tokenize the input text
        :return:
        """
        pass

    def check_next(self):
        """
        Checks if there are any more tokens left
        :return:
        """
        pass

    def get_next(self):
        """
        Returns the next token
        :return:
        """
        pass

    def check_token(self, regex):
        """
        Checks that the token matches the regex
        :param regex:
        :return: boolean
        """
        pass

    def get_and_check_next(self, regex):
        """
        Gets the next token and checks if it matches the regex
        :param regex:
        :return: string
        """
        pass

    def is_empty(self):
        """
        Checks if the tokenizer is empty
        :return: boolean
        """
        pass
