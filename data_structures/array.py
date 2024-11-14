class Array:
    def __init__(self, capacity):
        # Initialize the array with a fixed capacity
        self.capacity = capacity
        self.size = 0
        self.elements = [None] * capacity  # Allocate memory for the array

    def insert(self, index, value):
        if self.size >= self.capacity:
            raise Exception("Array is full")
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        # Shift elements to the right to make space
        for i in range(self.size, index, -1):
            self.elements[i] = self.elements[i - 1]
        
        self.elements[index] = value
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.elements[index]

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        # Shift elements to the left to fill the gap
        for i in range(index, self.size - 1):
            self.elements[i] = self.elements[i + 1]
        
        self.elements[self.size - 1] = None  # Clear the last element
        self.size -= 1

    def display(self):
        print("Array contents:", [self.elements[i] for i in range(self.size)])

# Create an array of capacity 5
arr = Array(5)

# Insert elements
arr.insert(0, 10)
arr.insert(1, 20)
arr.insert(2, 30)
arr.display()  # Should show [10, 20, 30]

# Get element by index
print("Element at index 1:", arr.get(1))  # Should print 20

# Delete an element
arr.delete(1)
arr.display()  # Should show [10, 30]

# Insert at the beginning
arr.insert(0, 5)
arr.display()  # Should show [5, 10, 30]
