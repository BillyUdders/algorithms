import unittest

from src.graph import Graph, Vertex, Node


class GraphTestCase(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        g = Graph()
        g[Node("a")] = [Vertex(Node("c")), Vertex(Node("b"))]
        g[Node("b")] = Vertex(Node("d"), 14)
        g[Node("c")] = Vertex(Node("e"), 10)
        g[Node("d")] = Vertex(Node("f"), 100)
        g[Node("e")] = []
        g[Node("f")] = [Vertex(Node('a'))]
        g[Node("g")] = []
        self.graph = g

        # Change here if you change the Graph ^
        self.input_adj_list = {
            "a": ["c", "b"],
            "b": [("d", 14)],
            "c": [("e", 10)],
            "d": [("f", 100)],
            "e": [],
            "f": ['a'],
            "g": []
        }

        # Change here if you change the Graph ^
        self.expected_adj_dict = {
            Node("a"): [Vertex(Node("c")), Vertex(Node("b"))],
            Node("b"): [Vertex(Node("d"), 14)],
            Node("c"): [Vertex(Node("e"), 10)],
            Node("d"): [Vertex(Node("f"), 100)],
            Node("e"): [],
            Node("f"): [Vertex(Node('a'))],
            Node("g"): []
        }

    def test_dict_initialization(self):
        expected = self.expected_adj_dict
        actual = Graph(self.input_adj_list).adj_list
        self.assertDictEqual(expected, actual)

    def test_adjacency_list(self):
        expected = self.expected_adj_dict
        actual = self.graph.adj_list
        self.assertDictEqual(expected, actual)

    def test_adjacency_matrix(self):
        expected = [
            [0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 14, 0, 0, 0],
            [0, 0, 0, 0, 10, 0, 0],
            [0, 0, 0, 0, 0, 100, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(expected, self.graph.adj_matrix)

    def test_breadth_first_search(self):
        expected = ["a", "c", "b", "e", "d", "f"]
        result = [i.name for i in self.graph.breadth_first_search(Node('a'))]
        self.assertEqual(expected, result)

    def test_depth_first_search(self):
        expected = ["a", "b", "d", "f", "c", "e"]
        result = [i.name for i in self.graph.depth_first_search(Node('a'))]
        self.assertEqual(expected, result)

    def test_has_path(self):
        self.assertTrue(self.graph.has_path(Node('a'), Node('f')), "Node A and F aren't connected and should be")
        self.assertFalse(self.graph.has_path(Node('a'), Node('g')), "Node A and G are connected and shouldn't be")


if __name__ == '__main__':
    unittest.main()
