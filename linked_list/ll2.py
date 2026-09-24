# Problem 2: Search in a Linked List
# Given a linked list and a target value, determine whether the target exists.

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

    # def find_tgt(self, tgt_val):

    #     # Start from the first node
    #     current = self.head

    #     found=False

    #     while current:
    #         if current.data == tgt_val:
    #             print(f"{tgt_val} found")
    #             found=True
    #             break
    #         current = current.next

    #     if not found:
    #         print(f"{tgt_val} not found")

    def find_tgt(self, tgt_val):

       current = self.head

       while current:
           if current.data == tgt_val:
               print("Found")
               return


           current = current.next

       print("Not Found")


# Create linked list
ll = LinkedList()

# Add elements
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

#find a particular value
ll.find_tgt(20)
ll.find_tgt(100)





