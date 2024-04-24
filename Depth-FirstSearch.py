class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, node1, node2):
        if node1 not in self.adjacency_list:
            self.adjacency_list[node1] = []
        self.adjacency_list[node1].append(node2)

    def depth_first_search(self, start_node):
        visited = {node: False for node in self.adjacency_list}
        print("Depth-First Traversal:")
        self._dfs_util(start_node, visited)
        print()

    def _dfs_util(self, current_node, visited):
        visited[current_node] = True
        print(current_node, end=' ')
        neighbors = self.adjacency_list.get(current_node, [])
        for neighbor in neighbors:
            if not visited.get(neighbor, False):
                self._dfs_util(neighbor, visited)

# Example usage and test
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 4)
graph.add_edge(2, 5)

graph.depth_first_search(0)
