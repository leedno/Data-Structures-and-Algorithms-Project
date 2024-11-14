from utils import measure_time, write_performance_to_csv

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in unsorted part of array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)

    # Measure and record performance
    input_sizes = [1000, 2000, 3000, 4000, 5000]  # Input sizes to test
    execution_times = measure_time(selection_sort, input_sizes)
    write_performance_to_csv('Selection Sort', input_sizes, execution_times)