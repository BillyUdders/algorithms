from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass(frozen=True)
class Node:
    name: str | int


@dataclass
class Vertex:
    data: Node
    weight: int = field(default=1)


AdjacencyList = Dict[Node, List[Vertex]]


class Graph:

    def __init__(self, initial_adj_list: dict = None):
        if initial_adj_list:
            self._adjacency_list: AdjacencyList = defaultdict(list, initial_adj_list)
        else:
            self._adjacency_list: AdjacencyList = defaultdict(list)

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

        for i, vertices in self._adjacency_list.items():
            for vtx in vertices:
                matrix[keys.index(i)][keys.index(vtx.data)] = vtx.weight

        return matrix

    @property
    def adj_list(self) -> AdjacencyList:
        return self._adjacency_list

    def depth_first_search(self, s: Node) -> List[Node]:
        return self.search(s)

    def breadth_first_search(self, s: Node) -> List[Node]:
        return self.search(s, True)

    def search(self, s: Node, breadth_first: bool = False) -> List[Node]:
        queue = [s]
        visited = []

        while queue:
            current = queue.pop(0) if breadth_first else queue.pop()
            current = current if isinstance(current, Node) else current.data
            visited.append(current)
            for node in self._adjacency_list[current]:
                queue.append(node)

        return visited

    def djisktras_shortest_path(self):
        pass
