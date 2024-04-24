class Graph:
    def __init__(self, vertices):
        self.num_vertices = vertices
        self.edges = []

    def add_edge(self, start, end, weight):
        self.edges.append((start, end, weight))

    def find(self, parent, node):
        if parent[node] == node:
            return node
        return self.find(parent, parent[node])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal(self):
        minimum_spanning_tree = []
        self.edges.sort(key=lambda edge: edge[2])
        parent = [i for i in range(self.num_vertices)]
        rank = [0] * self.num_vertices

        for edge in self.edges:
            start, end, weight = edge
            x = self.find(parent, start)
            y = self.find(parent, end)

            if x != y:
                minimum_spanning_tree.append(edge)
                self.union(parent, rank, x, y)

        print("Edges in the Minimum Spanning Tree:")
        for start, end, weight in minimum_spanning_tree:
            print(f"{start} -- {end} == {weight}")

# Example usage and test
g = Graph(5)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)
g.add_edge(2, 4, 8)
g.add_edge(3, 4, 9)

g.kruskal()
