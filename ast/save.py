import os
from os.path import join, normpath, isfile

from functionality.exceptions import IllegalInputException
from functionality.typedef import Directory
from libs.node import Node
from libs.symbol_table import symbol_table as st
import cv2


class SAVE(Node):
    variable = None
    path = None

    def parse(self, tokenizer):
        save = tokenizer.get_and_check_next('save')
        print("Parsing " + save + "...")
        self.variable = tokenizer.get_next()
        if tokenizer.maybe_match_next('as'):
            self.path = tokenizer.get_next().strip('\'\'')

    def evaluate(self):
        maybe_directory = Directory(st, self.variable)
        print("Saving {}!".format(self.variable))

        if maybe_directory.check():
            d = maybe_directory.cast()

            if self.path:
                if isfile(self.path):
                    raise IllegalInputException("Path specified was not a directory.")
                os.makedirs(self.path, exist_ok=True)
                root = self.path
            else:
                root = d["root"]

            for file, data in d["files"].items():
                cv2.imwrite(normpath(join(root, file)), data)

        elif self.path:
            img = st[self.variable]
            cv2.imwrite(self.path, img)

        else:
            raise IllegalInputException("Must specify a path to save singular images.")
