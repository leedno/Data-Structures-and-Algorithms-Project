from graphviz import Digraph

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Height of node (used for balancing)

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        if not root:
            return Node(value)

        if value < root.value:
            root.left = self._insert(root.left, value)
        else:
            root.right = self._insert(root.right, value)

        # Update the height of this node
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        # Get the balance factor of this node to check whether it became unbalanced
        balance = self._get_balance(root)

        # If this node becomes unbalanced, then there are 4 cases

        # Left Left Case
        if balance > 1 and value < root.left.value:
            return self._right_rotate(root)

        # Right Right Case
        if balance < -1 and value > root.right.value:
            return self._left_rotate(root)

        # Left Right Case
        if balance > 1 and value > root.left.value:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        # Right Left Case
        if balance < -1 and value < root.right.value:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_height(self, root):
        if not root:
            return 0
        return root.height

    def _get_balance(self, root):
        if not root:
            return 0
        return self._get_height(root.left) - self._get_height(root.right)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.value, end=" -> ")
            self.inorder_traversal(root.right)

    def display(self):
        print("Inorder Traversal:")
        self.inorder_traversal(self.root)
        print("\n")


if __name__ == "__main__":
    tree = AVLTree()

    # Insert values
    tree.insert(30)
    tree.insert(20)
    tree.insert(10)
    tree.insert(25)
    tree.insert(5)

    tree.display()