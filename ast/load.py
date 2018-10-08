from functionality.exceptions import InvalidFileTypeException
from libs import node
from libs import symbol_table as st

import cv2
import os


class LOAD(node.Node):
    path = None
    variable = None

    def parse(self, tokenizer):
        """
        Parses the tokenizer for a load node
        :return:
        """
        tokenizer.get_and_check_next('load')
        self.path = tokenizer.get_next().strip('\'\'')
        tokenizer.get_and_check_next('as')
        self.variable = tokenizer.get_next()

    def get_files(self):
        for folder, _, files in os.walk(self.path):
            # Only retrieves files in the top level
            if folder == self.path:
                return files

    def get_img(self, path):
        path = os.path.normpath(path)
        img = cv2.imread(path)
        if img is None:
            raise InvalidFileTypeException("{} is not an image.".format(path))
        print("Loaded image: {} as {}".format(path, self.variable))
        return img

    def evaluate(self):
        """
        Evaluates the load node
        :return:
        """
        if os.path.isfile(self.path):
            st.symbol_table[self.variable] = self.get_img(self.path)
        elif os.path.isdir(self.path):
            table = {}
            for file in self.get_files():
                path = None
                try:
                    path = os.path.join(self.path, file)
                    table[file] = self.get_img(path)
                except InvalidFileTypeException:
                    print("Skipping file {}".format(file if path is None else path))
            st.symbol_table[self.variable] = table
        else:
            raise Exception('Cannot find file path: {}'.format(self.path))
