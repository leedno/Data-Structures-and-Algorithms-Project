class Queue:
    def __init__(self):
        self.items = []  # Initialize empty list to hold the queue elements

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove and return the front element
        raise IndexError("dequeue from empty queue")  # If the queue is empty, raise an error

    def peek(self):
        if not self.is_empty():
            return self.items[0]  # Return the front element without removing
        raise IndexError("peek from empty queue")

    def is_empty(self):
        return len(self.items) == 0  # Check if the queue is empty

    def size(self):
        return len(self.items)  # Return current size of the queue


# Testing queue
queue = Queue()

# Enqueue elements into the queue
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front element:", queue.peek())  # Should print: 10

print("Dequeued:", queue.dequeue())  # Should print: 10
print("Dequeued:", queue.dequeue())  # Should print: 20

print("Queue size:", queue.size())  # Should print: 1

print("Is queue empty?", queue.is_empty())  # Should print: False

print("Dequeued:", queue.dequeue())  # Should print: 30

print("Is queue empty?", queue.is_empty())  # Should print: True
