
class Node:
    def __init__(self, value):
        self.value = value  # Store the data
        self.next = None    # Points to the next one

class LinkedList:
    def __init__(self):
        self.head = None  # The head is initially None (empty list)

    def insert(self, value):
        new_node = Node(value)  # Create a new node
        if not self.head:
            self.head = new_node  # If list is empty, new node becomes head
        else:
            current = self.head
            while current.next:  # go to the end of the list
                current = current.next
            current.next = new_node  # Add the new node at the end

    def delete(self, value):
        if not self.head:
            print("List is empty")
            return

        # If the value is at the head node
        if self.head.value == value:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.value == value:  # Node to delete found
                current.next = current.next.next  # Skip the node
                return
            current = current.next

        print("Value not found")

    def display(self):
        if not self.head:
            print("List is empty")
            return

        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")



ll = LinkedList()

# Insert values
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()  # Should print: 10 -> 20 -> 30 -> None

# Delete a value
ll.delete(20)
ll.display()  # Should print: 10 -> 30 -> None

# Trying to delete value that is not in the list  
ll.delete(40)  # Should print: Value not found