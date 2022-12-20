import unittest

from src.graph import Graph, Vertex, Node


class GraphTestCase(unittest.TestCase):
    # Change here if you change the Graph in setUp
    expected_adj_dict = {
        Node("a"): [Vertex(Node("c")), Vertex(Node("b"))],
        Node("b"): [Vertex(Node("d"), 14)],
        Node("c"): [Vertex(Node("e"), 10)],
        Node("d"): [Vertex(Node("f"), 100)],
        Node("e"): [],
        Node("f"): []
    }

    def setUp(self) -> None:
        super().setUp()

        g = Graph()
        g[Node("a")] = [Vertex(Node("c")), Vertex(Node("b"))]
        g[Node("b")] = Vertex(Node("d"), 14)
        g[Node("c")] = Vertex(Node("e"), 10)
        g[Node("d")] = Vertex(Node("f"), 100)
        g[Node("e")] = []
        g[Node("f")] = []

        self.g = g

    def test_dict_initialization(self):
        actual = Graph(self.expected_adj_dict).adj_list

        self.assertDictEqual(self.expected_adj_dict, actual)

    def test_adjacency_list(self):
        self.assertDictEqual(self.g.adj_list, self.method_name())

    def method_name(self):
        expected = self.expected_adj_dict
        return expected

    def test_adjacency_matrix(self):
        expected = [
            [0, 1, 1, 0, 0, 0],
            [0, 0, 0, 14, 0, 0],
            [0, 0, 0, 0, 10, 0],
            [0, 0, 0, 0, 0, 100],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]

        self.assertEqual(self.g.adj_matrix, expected)

    def test_breadth_first_search(self):
        expected = ["a", "c", "b", "e", "d", "f"]
        result = [i.name for i in self.g.breadth_first_search(Node('a'))]

        self.assertEqual(expected, result)

    def test_depth_first_search(self):
        expected = ["a", "b", "d", "f", "c", "e"]
        result = [i.name for i in self.g.depth_first_search(Node('a'))]

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
