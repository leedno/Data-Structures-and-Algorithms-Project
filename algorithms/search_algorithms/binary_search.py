import time
from utils import measure_time, write_performance_to_csv

# Binary search algorithm
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Target found at this index
        elif target < mid_value:
            right = mid - 1  # Narrow down to the left half
        else:
            left = mid + 1  # Narrow down to the right half

    return -1  # Target not found

# Measure the time for binary search
def measure_binary_search_time(n):
    arr = list(range(1, n + 1))  # Create a sorted list of size n
    target = n  # Arbitrary target; can be any number within the range
    start_time = time.perf_counter()  # Use higher resolution timer
    binary_search(arr, target)  # Perform binary search
    end_time = time.perf_counter()
    return end_time - start_time

if __name__ == "__main__":
    input_sizes = [1000, 2000, 3000, 4000, 5000]
    execution_times = []

    for size in input_sizes:
        execution_times.append(measure_binary_search_time(size))  # Measure time for binary search with different array sizes

    # Write the performance data to CSV
    write_performance_to_csv('Binary Search', input_sizes, execution_times)
