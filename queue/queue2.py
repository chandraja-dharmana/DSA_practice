# So your solution demonstrates both accessing the front
# and removing elements from a queue.
from collections import deque

b=deque()
b.append(10)
b.append(20)
b.append(30)
b.append(40)
b.append(50)
print(b)

for i in range(len(b)):
    print(b.popleft())