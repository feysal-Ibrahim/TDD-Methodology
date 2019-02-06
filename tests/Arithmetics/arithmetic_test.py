import unittest
from ad import sum
from divide import divide


class TestAddDiv(unittest.TestCase):

    """docstring for TestAddDiv"unittest.TestCasef __init__(self, arg):
            super(TestAddDiv,unittest.TestCase.__init__()
            self.arg = arg
            """

    def test_add(self):
        self.assertEqual(sum(1, 2), 3)
        self.assertNotEqual(sum(1, 2), 2)

    def test_divide(self):
        self.assertEqual(divide(5, 2), 2.5)
        self.assertNotEqual(divide(5, 2), 2)


if __name__ == '__main__':
    unittest.main()
