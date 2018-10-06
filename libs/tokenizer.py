import re # Python regex library
from operator import add
from functools import reduce


class Tokenizer:
    tokens = []
    cur = None

    def __init__(self, file_path, literals):
        # Constructor
        self.literals = literals
        self.cur = 0
        with open(file_path, 'r') as f:
            self.file = f.read().splitlines()

    def tokenize(self):
        """
        Tokenize the input text
        :return:
        """
        # Split array into tokens by spaces
        self.tokens = [x.split(' ') for x in self.file]
        # Flatten array using reduce and list concat
        self.tokens = reduce(add, self.tokens)

    def check_next(self):
        """
        Returns a copy of the current index in the tokens
        :return:
        """
        return self.tokens[self.cur]

    def get_next(self):
        """
        Returns the next token
        :return:
        """
        ret = self.tokens[self.cur]
        self.cur += 1
        return ret

    def check_token(self, regex):
        """
        Checks that the token matches the regex
        :param regex:
        :return: boolean
        """
        return self.tokens[self.cur] is regex

    def get_and_check_next(self, regex):
        """
        Gets the next token and checks if it matches the regex
        :param regex:
        :return: string
        """
        ret = False
        if self.check_token(regex):
            self.cur += 1
            ret = True
        return ret

    def is_empty(self):
        """
        Checks if the tokenizer is empty
        :return: boolean
        """
        return self.cur >= len(self.tokens) - 1
