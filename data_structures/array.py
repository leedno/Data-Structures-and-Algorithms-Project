class Array:
    def __init__(self, capacity):

        self.capacity = capacity
        self.size = 0
        self.elements = [None] * capacity 

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
        if index < 0 or index >= self.size:
            raise IndexError("index out of bounds")
        return self.elements[index]

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of bounds")
        
        for i in range(index, self.size - 1):
            self.elements[i] = self.elements[i + 1]
        
        self.elements[self.size - 1] = None
        self.size -= 1

    def display(self):
        print("array contents:", [self.elements[i] for i in range(self.size)])
arr = Array(5)

arr.insert(0, 10)
arr.insert(1, 20)
arr.insert(2, 30)
arr.display()  
print("element at index 1:", arr.get(1)) 

arr.delete(1)
arr.display()  
arr.insert(0, 5)
arr.display()
