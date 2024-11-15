from utils import measure_time, write_performance_to_csv

# Bubble Sort 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    sorted_arr = bubble_sort(arr)
    print("Sorted array:", sorted_arr)

    input_sizes = [1000, 2000, 3000, 4000, 5000]
    execution_times = measure_time(bubble_sort, input_sizes)
    write_performance_to_csv('Bubble Sort', input_sizes, execution_times)