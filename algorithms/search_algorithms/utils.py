
import time
import random
import csv

# Measure the time for a given sorting function and a list of input sizes
def measure_time(algorithm, input_sizes):
    execution_times = []
    for size in input_sizes:
        arr = [random.randint(1, 1000) for _ in range(size)]  # Generate random list
        start_time = time.time()  # Start timing
        algorithm(arr)  # Run the sorting algorithm
        end_time = time.time()  # End timing
        execution_times.append(end_time - start_time)  # Calculate execution time
    return execution_times

# Write performance results to a CSV file
def write_performance_to_csv(algorithm_name, input_sizes, execution_times, filename="performance_results.csv"):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        # If the file is empty, write the header
        file.seek(0, 2)
        if file.tell() == 0:
            writer.writerow(['Algorithm', 'Input Size', 'Execution Time'])
        for size, time_taken in zip(input_sizes, execution_times):
            writer.writerow([algorithm_name, size, time_taken])