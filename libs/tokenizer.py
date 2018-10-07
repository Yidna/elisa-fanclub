import collections


class Tokenizer:
    tokens = []
    cur = None

    def __init__(self, file_path):
        # Constructor
        self.cur = 0
        with open(file_path, 'r') as f:
            self.file = f.read().splitlines()

    def tokenize(self):
        """
        Tokenize the input text
        :return:
        """
        self.tokens = [word for line in self.file for word in line.split() if word]
        print(self.tokens)

    def get_next(self):
        """
        Returns the next token
        :return:
        """
        ret = self.tokens[self.cur]
        self.cur += 1
        print("returned {}".format(ret))
        return ret

    def check_next(self, regex):
        """
        Checks that the token matches the regex
        :param regex:
        :return: boolean
        """
        if isinstance(regex, collections.Iterable):
            return self.tokens[self.cur] in regex
        else:
            return self.tokens[self.cur] == regex

    def get_and_check_next(self, regex):
        """
        Gets the next token and checks if it matches the regex
        :param regex:
        :return: string
        """
        ret = ""

        if self.check_next(regex):
            ret = self.tokens[self.cur]
            self.cur += 1
        print("Checked {} against {}!".format(regex, ret))
        return ret

    def is_empty(self):
        """
        Checks if the tokenizer is empty
        :return: boolean
        """
        return self.cur >= len(self.tokens)
