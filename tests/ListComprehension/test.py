import unittest
from list import list


class ListComprehension(unittest.TestCase):
    """docstring for ListComprehension"""

    def test_list(self):
        self.assertEqual(len(list(10)), 10)


if __name__ == '__main__':
    unittest.main()
