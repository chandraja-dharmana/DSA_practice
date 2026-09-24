#https://chatgpt.com/share/6aaac1f3-7b90-83e8-b3ea-b276d5b9f789

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        # If linked list is empty
        if self.head is None:
            self.head = new_node
            return

        # Start from the first node
        current = self.head

        # Go to the last node
        while current.next:
            current = current.next

        # This below is an important line
        # Connect the last node to the new node
        current.next = new_node

    def print_list(self):
        current = self.head

        while current:
            print(current.data, end=" ")
            current = current.next

# Create linked list
ll = LinkedList()

# Add elements
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

# Print
ll.print_list()