import unittest

import numpy as np

from src.game_of_life import update, DEAD, ALIVE


class MyTestCase(unittest.TestCase):
    def test_gol_update(self):
        input_a = np.array([[DEAD, ALIVE, DEAD, ALIVE],
                            [DEAD, ALIVE, ALIVE, ALIVE],
                            [DEAD, DEAD, ALIVE, DEAD],
                            [ALIVE, DEAD, ALIVE, DEAD]])

        expected = np.array([[DEAD, ALIVE, DEAD, ALIVE],
                             [DEAD, ALIVE, DEAD, ALIVE],
                             [DEAD, DEAD, DEAD, DEAD],
                             [DEAD, ALIVE, DEAD, DEAD]])

        n = update(input_a)
        self.assertTrue(np.array_equal(n, expected))


if __name__ == '__main__':
    unittest.main()
