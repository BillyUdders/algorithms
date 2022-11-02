import unittest

import src.binary_search as bs


class MyTestCase(unittest.TestCase):
    test_good = [1, 3, 5, 9, 12, 15]
    test_fail = [1, 2, 4, 8, 16, 25]

    def test_iterative(self):
        res = bs.binary_search_iterative(self.test_good, 3)
        self.assertEqual(res, 1)

        res = bs.binary_search_iterative(self.test_fail, 3)
        self.assertEqual(res, -1)

    def test_recursive(self):
        res = bs.binary_search_recursive(self.test_good, 0, len(self.test_good) - 1, 3)
        self.assertEqual(res, 1)

        res = bs.binary_search_recursive(self.test_fail, 0, len(self.test_fail) - 1, 3)
        self.assertEqual(res, -1)

    def test_bisect_left(self):
        res = bs.binary_search_bisect_left(self.test_good, 3)
        self.assertEqual(res, 1)

        res = bs.binary_search_bisect_left(self.test_fail, 3)
        self.assertEqual(res, -1)


if __name__ == '__main__':
    unittest.main()
