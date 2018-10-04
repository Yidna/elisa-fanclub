# https://docs.python.org/3/library/unittest.html
import unittest


class TestTokenizer(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(1, 1)

    def test_fail(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()