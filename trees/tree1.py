    #     10
    #    /  \
    #   5    15
    #  / \
    # 2   7

#in-order traversal 2 5 7 10 15

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create the nodes
root = Node(10)
root.left = Node(5)
root.right = Node(15)

root.left.left = Node(2)
root.left.right = Node(7)


# In-order traversal
def inorder(node):
    if node is not None:
        # This is the important part
        inorder(node.left) #Left
        print(node.data, end=" ") #Root
        inorder(node.right) #Right


inorder(root)