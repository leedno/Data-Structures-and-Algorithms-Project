# **Algorithms Implementation Documentation**

## **Overview**

This document explains the algorithms implemented in the project, including sorting algorithms, searching algorithms, and tree traversal algorithms. Each algorithm is implemented in Python, and their time and space complexities are discussed. The code snippets are explained to provide a better understanding of the underlying logic.

---

## **1. Sorting Algorithms**

### **1.1 Bubble Sort**

#### **Description**:
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

#### **Time Complexity**:
- Best: O(n) — when the array is already sorted.
- Average: O(n^2) — for random data.
- Worst: O(n^2) — for a list sorted in reverse order.

#### **Space Complexity**: 
- O(1) — Bubble Sort is an in-place sorting algorithm.

#### **Code**:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap if the element is greater
    return arr
