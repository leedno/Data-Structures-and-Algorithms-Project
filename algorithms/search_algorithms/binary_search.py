# Binary search

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

arr = [1, 2, 3, 5, 9]  # Must be sorted
target = 3
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
