import graphviz

# preorder traversal of a tree using recursion and iteration (stack) 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def preorder_recursive(root):
    if root:
        print(root.data, end=' ')
        preorder_recursive(root.left)
        preorder_recursive(root.right)
    
def preorder_iterative(root):
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        print(node.data, end=' ')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print('Preorder Recursive:')
preorder_recursive(root)
print('\nPreorder Iterative:')
preorder_iterative(root)
print()

# Output:
# Preorder Recursive:
# 1 2 4 5 3 6 7
# Preorder Iterative:
# 1 2 4 5 3 6 7


# Time Complexity: O(n)
# Space Complexity: O(n) for stack
# n is number of nodes in the tree
