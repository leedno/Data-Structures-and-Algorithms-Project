class Array:
    def __init__(self, capacity):
        # Initialize array
        self.capacity = capacity
        self.size = 0
        self.elements = [None] * capacity  # Create empty array

    def insert(self, index, value):
        if self.size >= self.capacity:
            raise Exception("array is full")
        if index < 0 or index > self.size:
            raise IndexError("index out of bounds")
        
        for i in range(self.size, index, -1):
            self.elements[i] = self.elements[i - 1]
        
        self.elements[index] = value
        self.size += 1

    def get(self, index):
        # Return the element at the given index
        if index < 0 or index >= self.size:
            raise IndexError("index out of bounds")
        return self.elements[index]

    def delete(self, index):
        # Remove element at the given index and shift others
        if index < 0 or index >= self.size:
            raise IndexError("index out of bounds")
        
        for i in range(index, self.size - 1):
            self.elements[i] = self.elements[i + 1]
        
        self.elements[self.size - 1] = None
        self.size -= 1

    def display(self):
        print("array contents:", [self.elements[i] for i in range(self.size)])

# Testing Array class
arr = Array(5)

arr.insert(0, 10)  # Insert 10
arr.insert(1, 20)  # Insert 20
arr.insert(2, 30)  # Insert 30
arr.display()  # Show the array

print("element at index 1:", arr.get(1))

arr.delete(1)  # Remove element at index 1
arr.display()  # Show the updated array
arr.insert(0, 5)  # Insert 5 at the beginning
arr.display()  # Final display
