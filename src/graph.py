from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class GraphItem:
    data: Any = field(compare=False)
    weight: int = field(default=0)


class Graph:

    def __init__(self, initial_adj_list: dict = None):
        if initial_adj_list:
            self.adj_list = defaultdict(list, initial_adj_list)
        else:
            self.adj_list = defaultdict(list)

    def __setitem__(self, key, value) -> None:
        if isinstance(value, list):
            self.adj_list[key] += value
        else:
            self.adj_list[key].append(value)

    def get_adj_list(self) -> Dict:
        return self.adj_list

    def depth_first_search(self, s) -> List:
        return self.search(s)

    def breadth_first_search(self, s) -> List:
        return self.search(s, True)

    def search(self, s, breadth_first=False):
        queue = [s]
        visited = []
        while queue:
            current = queue.pop(0) if breadth_first else queue.pop()
            visited.append(current)
            for node in self.adj_list[current]:
                queue.append(node)
        return visited

    def djisktras_shortest_path(self):
        pass


if __name__ == '__main__':
    g = Graph()
    g["a"] = ["c", "b"]
    g["b"] = "d"
    g["c"] = "e"
    g["d"] = "f"
    g["e"] = []
    g["f"] = []

    print("\nAdjacency List:\n")
    for k, v in g.get_adj_list().items():
        print(k, v)
    print("\nAlgorithms:\n")
    print("Depth first", g.depth_first_search('a'))
    print("Breadth first", g.breadth_first_search('a'))
