# Import nececcary classes
from binary_tree import BinaryTree  
from binary_tree import Node

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        if not self.root:
            self.root = Node(value)  # If tree is empty, insert the root node
        else:
            self._insert(self.root, value)  # Insert the value maintaining the BST property

    def _insert(self, current, value):
        if value < current.value:
            if not current.left:
                current.left = Node(value)  # Insert to the left if smaller
            else:
                self._insert(current.left, value)  # Recurse left
        else:
            if not current.right:
                current.right = Node(value)  # Insert to the right if larger
            else:
                self._insert(current.right, value)  # Recurse right

    def search(self, value):
        return self._search(self.root, value)  # Start searching from the root

    def _search(self, current, value):
        if current is None:
            return False  # Value not found
        if value == current.value:
            return True  # Value found
        elif value < current.value:
            return self._search(current.left, value)  # Search in the left subtree
        else:
            return self._search(current.right, value)  # Search in the right subtree

    def delete(self, value):
        self.root = self._delete(self.root, value)  # Start deleting from the root

    def _delete(self, current, value):
        if current is None:
            return current  # If tree is empty, nothing to delete

        if value < current.value:
            current.left = self._delete(current.left, value)  # Recurse left
        elif value > current.value:
            current.right = self._delete(current.right, value)  # Recurse right
        else:
            # Node with only one child or no child
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            # Node with two children: get the inorder successor (smallest in the right subtree)
            min_larger_node = self._min_value_node(current.right)
            current.value = min_larger_node.value  # Copy the inorder successor's value to current node
            current.right = self._delete(current.right, min_larger_node.value)  # Delete the inorder successor

        return current

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left  # Find the leftmost leaf node
        return current

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


# Testing the Binary Search Tree
bst = BinarySearchTree()

# Insert values into the BST
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(18)

# Display the tree traversals
bst.display()

# Search for values in the BST
print("\nSearching for 7:", bst.search(7))  # Should return True
print("Searching for 20:", bst.search(20))  # Should return False

# Delete a value and show the tree again
bst.delete(7)
print("\nAfter deleting 7:")
bst.display()

# Delete a node with two children
bst.delete(5)
print("\nAfter deleting 5 (node with two children):")
bst.display()