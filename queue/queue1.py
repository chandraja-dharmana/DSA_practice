a=[1,2,3,4]

# Yes — for basic enqueue(adding at the back), 
# both list and deque are effectively O(1) amortized.

# ENQUEUE - add at the back
a.append(5)
print(a)
# [1, 2, 3, 4, 5]

# FRONT - see the first element
print(a[0])
# 1

from collections import deque
b=deque(a)
b.popleft() #same as b.popleft(0)

# # DON'T USE THIS
# # DEQUEUE - remove from the front
# b=a.pop(0)
# print(b)
# print(a)

# pop(0) works for learning the queue concept, but it is O(n) 
# because Python has to shift the remaining elements.
# Later, you'll learn deque, where removing from the front is O(1).