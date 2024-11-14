class Node:
    def __init__(self, value):
        self.value = value  # Store data
        self.left = None    # Left child
        self.right = None   # Right child

class BinaryTree:
    def __init__(self):
        self.root = None  # Initially, the tree is empty

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node  # if the tree is empty, new node becomes the root
        else:
            self._insert(self.root, new_node)  # otherwise, find the correct position

    def _insert(self, current, new_node):
        if new_node.value < current.value:
            if current.left is None:
                current.left = new_node  # Insert to the left
            else:
                self._insert(current.left, new_node)  # Recursive insert
        else:
            if current.right is None:
                current.right = new_node  # Insert to the right
            else:
                self._insert(current.right, new_node)  # Recursiv insert

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)  # Traverse left
            print(node.value, end=" -> ")  # Visit the node
            self.in_order_traversal(node.right)  # Traverse right

    def pre_order_traversal(self, node):
        if node:
            print(node.value, end=" -> ")  # Visit node
            self.pre_order_traversal(node.left)  # Traverse left
            self.pre_order_traversal(node.right)  # Traverse right

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)  # Traverse left
            self.post_order_traversal(node.right)  # Traverse right
            print(node.value, end=" -> ")  # Visit the node

    def display(self):
        if self.root:
            print("In-order traversal:")
            self.in_order_traversal(self.root)
            print("\nPre-order traversal:")
            self.pre_order_traversal(self.root)
            print("\nPost-order traversal:")
            self.post_order_traversal(self.root)
        else:
            print("The tree is empty")


bt = BinaryTree()

bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(3)
bt.insert(7)
bt.insert(12)
bt.insert(18)

# Display tree traversals
bt.display() 
