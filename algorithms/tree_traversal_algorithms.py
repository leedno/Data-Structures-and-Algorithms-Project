class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Preorder Traversal (Root, Left, Right)
def preorder_traversal(root):
    if root:
        print(root.value, end=" ")  
        preorder_traversal(root.left)  
        preorder_traversal(root.right) 

# Inorder Traversal (Left, Root, Right)
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

# Postorder Traversal (Left, Right, Root)
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

# Level-order Traversal (Breadth-first, using a queue)
from collections import deque
def levelorder_traversal(root):
    if not root:
        return
    
    queue = deque([root])  # Initialize queue with root
    
    while queue:
        node = queue.popleft()  # Remove node from queue
        print(node.value, end=" ")  # Visit node
        
        if node.left:
            queue.append(node.left)  # Add left child to queue
        if node.right:
            queue.append(node.right)  # Add right child to queue

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    # Preorder Traversal
    print("Preorder Traversal:")
    preorder_traversal(root)
    print("\n")

    # Inorder Traversal
    print("Inorder Traversal:")
    inorder_traversal(root)
    print("\n")

    # Postorder Traversal
    print("Postorder Traversal:")
    postorder_traversal(root)
    print("\n")

    # Level-order Traversal
    print("Level-order Traversal:")
    levelorder_traversal(root)
    print("\n")
