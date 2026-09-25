import heapq

arr = [7, 2, 9, 4, 1, 5]
k = 3

heapq.heapify(arr)
print(arr)

small3 = []

for _ in range(k):
    small3.append(heapq.heappop(arr))

print(small3)

#nlargest()
arr = [7, 2, 9, 4, 1, 5]
heapq.heapify(arr)
ele = heapq.nlargest(2, arr) 
print(ele) #[9, 7]

#nsmallest()
arr = [7, 2, 9, 4, 1, 5]
heapq.heapify(arr)
ele = heapq.nsmallest(3, arr)
print(ele) #[1, 2, 4]