#Find Smallest: Given arr = [5, 2, 8, 1, 9, 3], use a Min Heap to find the smallest element.

import heapq

arr = [5, 2, 8, 1, 9, 3]
# Convert array into a Min Heap
heapq.heapify(arr)

print(arr)

# Access the smallest element
smallest = arr[0]

print(smallest)

# Important: A heap array does not have to be sorted.
# [1, 2, 3, 5, 9, 8] is a Min Heap, even though 8 comes after 9.
#        1
#       / \
#      2   3
#     / \ /
#    5  9 8