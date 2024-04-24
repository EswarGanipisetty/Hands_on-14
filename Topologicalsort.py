class DirectedGraph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, start, end):
        if start not in self.adj_list:
            self.adj_list[start] = []
        self.adj_list[start].append(end)

    def topological_sort_util(self, vertex, visited, stack):
        visited[vertex] = True
        for neighbor in self.adj_list.get(vertex, []):
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)
        stack.insert(0, vertex)

    def topological_sort(self):
        visited = {vertex: False for vertex in self.adj_list}
        stack = []
        for vertex in self.adj_list:
            if not visited[vertex]:
                self.topological_sort_util(vertex, visited, stack)
        return stack

# Test the implementation with an example from Barron's book
graph = DirectedGraph()
graph.add_edge(7, 5)
graph.add_edge(7, 6)
graph.add_edge(5, 3)
graph.add_edge(6, 4)
graph.add_edge(3, 1)
graph.add_edge(4, 2)
graph.add_edge(1, 0)

print("Topological Sort:", graph.topological_sort())
