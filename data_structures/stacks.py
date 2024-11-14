class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty list to hold the stack elements

    def push(self, value):
        self.items.append(value)  # Add value to the top of the stack

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Remove and return the top element
        raise IndexError("pop from empty stack")  # If the stack is empty, raise an error

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Return the top element without removing it
        raise IndexError("peek from empty stack")  # If the stack is empty, raise an error

    def is_empty(self):
        return len(self.items) == 0  # Check if the stack is empty

    def size(self):
        return len(self.items)  # Return the current size of the stack


# Testing the Stack
stack = Stack()

# Push elements to the stack
stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.peek())  # Should print: 30

print("Popped:", stack.pop())  # Should print: 30
print("Popped:", stack.pop())  # Should print: 20

print("Stack size:", stack.size())  # Should print: 1

print("Is stack empty?", stack.is_empty())  # Should print: False

print("Popped:", stack.pop())  # Should print: 10

print("Is stack empty?", stack.is_empty())  # Should print: True
