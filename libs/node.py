from abc import ABC as abstract_class
from abc import abstractmethod


class Node(abstract_class):

    @abstractmethod
    def parse(self, tokenizer):
        """
        Parses an AST node to it's corresponding object.
        :return:
        """
        pass

    @abstractmethod
    def evaluate(self):
        """
        Evaluates an AST node.
        :return:
        """
        pass

