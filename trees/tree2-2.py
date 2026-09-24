# This is wrong
# https://chatgpt.com/share/6aaaebb4-5a18-83e8-873d-b55c3b89fa78

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
def inorder(node, tgt_val):
   if node is not None:
       # This is the important part
       inorder(node.left, tgt_val) #Left
       if node.data == tgt_val:
           print(f"{tgt_val} found")
           return True
       inorder(node.right, tgt_val) #Right
       #return inorder(node.right, tgt_val) # works only for 15 

vals = [5,15,9,12]
for val in vals:
   ret_val = inorder(root, val)
   print(f"return value for {val} is {ret_val}")
   if not ret_val:
       print(f"{val} not found")