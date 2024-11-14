import time
from utils import measure_time, write_performance_to_csv

# Depth-First Search (DFS) for a graph
class Graph:
    def __init__(self):
        self.graph = {}

    # Add a new edge to the graph
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    # DFS recursive function
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Measure performance for DFS with varying graph sizes
def measure_dfs_time(n, iterations=5):
    g = Graph()
    # Create a simple graph with n nodes in a chain-like structure
    for i in range(1, n):
        g.add_edge(i, i + 1)  # Connect each node to the next
    
    # Perform multiple DFS iterations and average the results
    total_time = 0
    for _ in range(iterations):
        start_time = time.perf_counter()  # Use perf_counter for better precision
        g.dfs(1)  # Perform DFS starting from node 1
        end_time = time.perf_counter()
        total_time += (end_time - start_time)
    
    return total_time / iterations  # Average the time over multiple iterations

if __name__ == "__main__":
    # Test performance with varying graph sizes (number of nodes)
    input_sizes = [100, 200, 300, 400, 500]
    execution_times = []

    for size in input_sizes:
        execution_times.append(measure_dfs_time(size))  # Measure time for DFS with different graph sizes

    # Write the performance data to CSV
    write_performance_to_csv('DFS', input_sizes, execution_times)
