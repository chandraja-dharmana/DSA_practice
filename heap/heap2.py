#K Smallest: Given arr = [7, 2, 9, 4, 1, 5] and k = 3, find the 3 smallest elements using a heap.
import heapq

arr = [7, 2, 9, 4, 1, 5] 

# # Convert array into a Min Heap
# heapq.heapify(arr)

# print(arr) #[1, 2, 5, 4, 7, 9]
# #simple pop won't work -> fetch 5 instead of 4

small3=[]
cnt=0
# 3 small elements
while cnt<3:
    heapq.heapify(arr)
    small3.append(heapq.heappop(arr))
    cnt+=1

print(small3)
