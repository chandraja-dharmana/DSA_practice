#Search for an element in the tree    #     
#         10
    #    /  \
    #   5    15
    #  / \
    # 2   7


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


# Search for a value
def inorder(node, tgt_val):

    if node is None:
        return False

    # Search left
    if inorder(node.left, tgt_val):
        return True

    # Check current node
    if node.data == tgt_val:
        print(f"{tgt_val} found")
        return True

    # Search right 
    return inorder(node.right, tgt_val)


vals = [5, 15, 9, 12]

for val in vals:
    ret_val = inorder(root, val)

    print(f"return value for {val} is {ret_val}")

    if not ret_val:
        print(f"{val} not found")