from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict

# Node name
Label = str | int


# Simple edge class
@dataclass(frozen=True, order=True)
class Node:
    name: Label = field(compare=True)


# Represents a directed vertex in the adjacency list
@dataclass
class Vertex:
    node: Node
    weight: int = field(default=1)


# Adjacency list is a mapping of nodes to lists of vertices.
AdjList = Dict[Node, List[Vertex]]


class Graph:

    def __init__(self, initial_values: Dict[Label, List[Label]] = None):
        self._adjacency_list: AdjList = defaultdict(list)
        if initial_values:
            for name, vertices in initial_values.items():
                if not vertices:
                    self._adjacency_list[Node(name)] = []
                for vtx in vertices:
                    if isinstance(vtx, str):
                        self._adjacency_list[Node(name)].append(Vertex(Node(vtx)))
                    if isinstance(vtx, tuple):
                        self._adjacency_list[Node(name)].append(Vertex(Node(vtx[0]), vtx[1]))

    def __setitem__(self, key, value) -> None:
        if isinstance(value, list):
            self._adjacency_list[key] += value
        else:
            self._adjacency_list[key].append(value)

    @property
    def adj_matrix(self) -> List[List[int]]:
        size = len(self._adjacency_list)
        keys = list(self._adjacency_list)
        matrix = [[0 for _ in range(size)] for _ in range(size)]

        for node, vertices in self._adjacency_list.items():
            for vtx in vertices:
                matrix[keys.index(node)][keys.index(vtx.node)] = vtx.weight

        return matrix

    @property
    def adj_list(self) -> AdjList:
        return self._adjacency_list

    def depth_first_search(self, s: Node) -> List[Node]:
        return self.search(s)

    def breadth_first_search(self, s: Node) -> List[Node]:
        return self.search(s, breadth_first=True)

    def has_path(self, src: Node, dst: Node) -> bool:
        return dst in self.search(src)

    def search(self, s: Node, breadth_first: bool = False) -> List[Node]:
        queue = [s]
        visited = []

        while queue:
            current: Node = self.get_node(queue.pop(0) if breadth_first else queue.pop())
            visited.append(current)
            for vertex in self._adjacency_list[current]:
                if vertex.node not in visited:
                    queue.append(vertex)

        return visited

    @staticmethod
    def get_node(current: Node | Vertex) -> Node:
        return current if isinstance(current, Node) else current.node

    def djisktras_shortest_path(self):
        pass
        # Mark all the vertices as not visited
