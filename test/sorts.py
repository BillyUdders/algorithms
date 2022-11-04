import random
import unittest

from src import quicksort, mergesort

random.seed(80081355)
state = random.getstate()
a = [random.uniform(10.5, 1090075.5) for i in range(100)]


class SortTestCase(unittest.TestCase):
    # Runs in n^2 time, n log n space
    def test_quicksort(self):
        quicksort.quicksort(a, 0, len(a) - 1)
        self.assertEqual(a, sorted(a))

    # Runs in n log n time, n space
    def test_mergesort(self):
        mergesort.mergesort_topdown(a)
        self.assertEqual(a, sorted(a))


if __name__ == '__main__':
    unittest.main()
