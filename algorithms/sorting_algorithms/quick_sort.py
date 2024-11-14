from utils import measure_time, write_performance_to_csv

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    sorted_arr = quick_sort(arr)
    print("Sorted array:", sorted_arr)

    # Measure and record performance
    input_sizes = [1000, 2000, 3000, 4000, 5000]  # Input sizes to test
    execution_times = measure_time(quick_sort, input_sizes)
    write_performance_to_csv('Quick Sort', input_sizes, execution_times)