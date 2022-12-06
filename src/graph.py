from collections import defaultdict


class Graph:

    def __init__(self):
        self.adj_list = defaultdict(list)

    def __setitem__(self, key, value):
        self.adj_list[key].append(value)

    def dfs(self, s):
        visited = defaultdict(bool)
        stack = [s]

        while stack:
            val = stack.pop()

            if not visited[val]:
                visited[val] = True

            for node in self.adj_list[val]:
                if not visited[node]:
                    stack.append(node)

        return list(visited.keys())

    def bfs(self, s):
        visited = defaultdict(bool)
        queue = [s]
        visited[s] = True

        while queue:
            s = queue.pop(0)
            for i in self.adj_list[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

        return list(visited.keys())


if __name__ == '__main__':
    g = Graph()
    g[0] = 1
    g[0] = 2
    g[1] = 2
    g[2] = 0
    g[2] = 3
    g[3] = 3

    print(g.dfs(2))
    print(g.bfs(2))
