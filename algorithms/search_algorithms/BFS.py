import time
from utils import measure_time, write_performance_to_csv
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Measure performance for BFS with varying graph sizes (nodes and edges)
def measure_bfs_time(num_nodes):
    g = Graph()
    # Adding edges between consecutive nodes to simulate a simple graph
    for i in range(1, num_nodes):
        g.add_edge(i, i + 1)

    # Perform BFS and measure execution time
    start_time = time.time()
    g.bfs(1)  # Starting BFS from node 1
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    # Test performance with varying input sizes (number of nodes)
    input_sizes = [1000, 2000, 3000, 4000, 5000]
    execution_times = []

    for size in input_sizes:
        execution_times.append(measure_bfs_time(size))  # Measure time for BFS with different graph sizes

    # Write the performance data to CSV
    write_performance_to_csv('BFS', input_sizes, execution_times)
