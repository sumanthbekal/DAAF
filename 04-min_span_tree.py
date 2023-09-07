import sys

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = [[0] * V for _ in range(V)]

    def add_edge(self, src, dest, weight):
        self.graph[src][dest] = self.graph[dest][src] = weight

    def prim_mst(self):
        key, parent, mst_set = [sys.maxsize] * self.V, [-1] * self.V, [False] * self.V
        key[0] = 0

        for _ in range(self.V):
            u = min((key[v], v) for v in range(self.V) if not mst_set[v])[1]
            mst_set[u] = True
            for v in range(self.V):
                if 0 < self.graph[u][v] < key[v] and not mst_set[v]:
                    key[v], parent[v] = self.graph[u][v], u

        print("MST:")
        total_cost = sum(self.graph[v][parent[v]] for v in range(1, self.V))
        for v in range(1, self.V):
            print(f"Edge: {parent[v]} - {v}, Weight: {self.graph[v][parent[v]]}")
        print(f"Total Cost: {total_cost}")

g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)
g.prim_mst()
