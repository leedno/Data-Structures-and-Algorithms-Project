from utils import measure_time, write_performance_to_csv


# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Original array:", arr)
    sorted_arr = insertion_sort(arr)
    print("Sorted array:", sorted_arr)

    # Measure and record performance
    input_sizes = [1000, 2000, 3000, 4000, 5000]  # Input sizes to test
    execution_times = measure_time(insertion_sort, input_sizes)
    write_performance_to_csv('Insertion Sort', input_sizes, execution_times)