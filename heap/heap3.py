import heapq

arr = [7, 2, 9, 4, 1, 5]
k = 3

heapq.heapify(arr)
print(arr)

small3 = []

for _ in range(k):
    small3.append(heapq.heappop(arr))

print(small3)