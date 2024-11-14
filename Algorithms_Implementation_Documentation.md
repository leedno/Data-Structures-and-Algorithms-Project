Algorithms Implementation Documentation
Overview
This document explains the algorithms implemented in the project, including sorting algorithms, searching algorithms, and tree traversal algorithms. Each algorithm is implemented in Python, and their time and space complexities are discussed. The code snippets are explained to provide a better understanding of the underlying logic.

1. Sorting Algorithms
1.1 Bubble Sort
Description:
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

Time Complexity:
Best: O(n) — when the array is already sorted.
Average: O(n^2) — for random data.
Worst: O(n^2) — for a list sorted in reverse order.
Space Complexity:
O(1) — Bubble Sort is an in-place sorting algorithm.
Code:
python
Copy code
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap if the element is greater
    return arr
Explanation:
The outer loop runs for n iterations, where n is the number of elements in the list.
The inner loop compares each adjacent pair and swaps them if the left element is greater than the right element.
This process repeats until the list is sorted.
1.2 Insertion Sort
Description:
Insertion Sort works by taking one element at a time from the unsorted portion of the list and inserting it into its correct position in the sorted portion.

Time Complexity:
Best: O(n) — when the list is already sorted.
Average: O(n^2) — for random data.
Worst: O(n^2) — when the list is sorted in reverse order.
Space Complexity:
O(1) — Insertion Sort is an in-place algorithm.
Code:
python
Copy code
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
Explanation:
The algorithm iterates over the list, and for each element, it finds the correct position in the sorted portion of the list.
The key element is inserted in its correct position by shifting larger elements one position to the right.
1.3 Merge Sort
Description:
Merge Sort is a divide-and-conquer algorithm that splits the list into two halves, recursively sorts each half, and then merges the two sorted halves back together.

Time Complexity:
Best: O(n log n)
Average: O(n log n)
Worst: O(n log n)
Space Complexity:
O(n) — Merge Sort requires additional space to store the temporary arrays during merging.
Code:
python
Copy code
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle point
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)  # Sort the left half
        merge_sort(right_half)  # Sort the right half

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr
Explanation:
The list is recursively divided into two halves until each half contains a single element.
The merge step combines the two sorted halves back together into one sorted list.
1.4 Quick Sort
Description:
Quick Sort is another divide-and-conquer algorithm. It works by selecting a pivot element and partitioning the array into two sub-arrays such that elements less than the pivot are on the left and elements greater than the pivot are on the right. The sub-arrays are recursively sorted.

Time Complexity:
Best: O(n log n)
Average: O(n log n)
Worst: O(n^2) — when the pivot selection is poor (e.g., always picking the smallest or largest element).
Space Complexity:
O(log n) — Quick Sort is an in-place sorting algorithm.
Code:
python
Copy code
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Select the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
Explanation:
A pivot is chosen from the list, and the list is partitioned into three sub-lists: elements less than the pivot, elements equal to the pivot, and elements greater than the pivot.
These sub-lists are recursively sorted and combined.
2. Searching Algorithms
2.1 Linear Search
Description:
Linear Search is the simplest search algorithm. It sequentially checks each element in the list until the target element is found.

Time Complexity:
Best: O(1) — when the target is the first element.
Average: O(n) — for random data.
Worst: O(n) — when the target is the last element or not present at all.
Space Complexity:
O(1) — Linear Search uses no extra space.
Code:
python
Copy code
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Return -1 if target is not found
Explanation:
The algorithm iterates over the entire list and compares each element with the target. If a match is found, it returns the index of the target.
2.2 Binary Search
Description:
Binary Search is an efficient algorithm for finding an item from a sorted list. It works by repeatedly dividing the search interval in half.

Time Complexity:
Best: O(1)
Average: O(log n)
Worst: O(log n)
Space Complexity:
O(1) — Binary Search is an in-place algorithm.
Code:
python
Copy code
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Return -1 if target is not found
Explanation:
The list is halved after each comparison, making it an efficient search algorithm for large datasets.
The algorithm repeatedly compares the target to the middle element of the list, narrowing down the search range until the target is found or the range becomes empty.
3. Tree Traversal Algorithms
3.1 Depth-First Search (DFS)
Description:
DFS is an algorithm for traversing or searching tree-like structures. It explores as far down a branch as possible before backtracking.

Time Complexity:
O(n) — where n is the number of nodes in the tree.
Space Complexity:
O(h) — where h is the height of the tree (for recursive stack).
Code:
python
Copy code
def dfs(tree, node):
    if node is None:
        return
    print(node.data)
    dfs(tree, node.left)  # Visit left subtree
    dfs(tree, node.right)  # Visit right subtree
Explanation:
The DFS algorithm starts from the root node and explores as deep as possible along each branch.
The algorithm backtracks when it hits a leaf node and explores the next branch.
3.2 Breadth-First Search (BFS)
Description:
BFS is an algorithm for traversing or searching tree-like structures, where it explores all the nodes at the present depth level before moving on to the nodes at the next depth level.

Time Complexity:
O(n) — where n is the number of nodes in the tree.
Space Complexity:
O(n) — since all nodes at the current level may need to be stored in a queue.
Code:
python
Copy code
from collections import deque

def bfs(tree, root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
Explanation:
BFS explores nodes level by level, starting from the root node.
It uses a queue to store nodes, processing each node's children before moving on to the next level.
Conclusion
This document provides detailed descriptions and code examples for the fundamental algorithms implemented in this project. Each algorithm is explained with its time and space complexity to give insights into their efficiency. These implementations can be further expanded and optimized for more advanced use cases.