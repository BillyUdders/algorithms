import unittest

from src.trie import Trie


class MyTestCase(unittest.TestCase):
    def test_trie_membership(self):
        tr = Trie()
        tr.insert("here")
        tr.insert("hear")
        tr.insert("he")
        tr.insert("hello")
        tr.insert("how ")
        tr.insert("her")

        result = tr.search('her')
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], 2)


if __name__ == '__main__':
    unittest.main()
