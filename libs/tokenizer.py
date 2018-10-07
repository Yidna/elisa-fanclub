from functionality.exceptions import IllegalInputException


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
        Split the input text into words and store in tokens.
        :return: void
        """
        self.tokens = [word for line in self.file for word in line.split() if word]
        print(self.tokens)

    def peek(self):
        if self.is_empty():
            raise Exception("Reached end of token buffer.")
        return self.tokens[self.cur]

    def check_next(self, literal):
        """
        Determine whether the next token is valid.
        :param literal: str | dict
        :return: boolean
        """
        return (self.peek() in literal) if isinstance(literal, dict) else (self.peek() == literal)

    def get_next(self):
        """
        Consume and return the next token.
        :return: str
        """
        ret = self.peek()
        self.cur += 1
        return ret

    def maybe_match_next(self, literal):
        """
        Consume the next token only if it matches the given literal.
        :param literal: str
        :return: boolean
        """
        return self.check_next(literal) and self.get_next()

    def get_and_check_next(self, literal):
        """
        Consume the next token and verify it matches the literal.
        :param literal: str | dict
        :return: str
        """
        if not self.check_next(literal):
            raise IllegalInputException("Invalid token: expected {}, actual {}".format(literal, self.peek()))
        return self.get_next()

    def is_empty(self):
        return self.cur >= len(self.tokens)
