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

    def check_next(self, token):
        """
        Checks that the token matches the regex
        :param token:
        :return: boolean
        """
        return self.tokens[self.cur] == token

    def get_and_check_next(self, token):
        """
        Gets the next token and checks if it matches the regex
        :param token:
        :return: string
        """
        ret = ""

        if self.check_next(token):
            ret = self.tokens[self.cur]
            self.cur += 1
        print("Checked {} against {}!".format(token, ret))
        return ret

    def is_empty(self):
        """
        Checks if the tokenizer is empty
        :return: boolean
        """
        return self.cur >= len(self.tokens)
