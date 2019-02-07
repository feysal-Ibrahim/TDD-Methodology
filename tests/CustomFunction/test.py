import unittest
from custom import custom


class Custom(unittest.TestCase):

    def test_custom(self):
        self.assertEqual(custom(3, 2, 3), 54)


if __name__ == '__main__':
    unittest.main()
