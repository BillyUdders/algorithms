import unittest
from pprint import pprint

from src.linked_list import LinkedList


class MyTestCase(unittest.TestCase):

    def test_linked_list_basic(self):
        l = LinkedList()
        l.insert("a")
        l.insert("b")
        l.insert("c")
        l.insert("d")
        l.insert("e")

        l.insert("blah", 3)
        l.insert("blah", 4, False)

        print(len(l))
        pprint(l)
        print(l[3])

        del l[3]
        print(len(l))
        pprint(l)
        del l[2]
        print(len(l))
        pprint(l)


if __name__ == '__main__':
    unittest.main()
