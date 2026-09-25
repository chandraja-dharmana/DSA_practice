import heapq

#heappush
arr=[]

heapq.heappush(arr, 5)
heapq.heappush(arr, 8)
heapq.heappush(arr, 1)
heapq.heappush(arr, 3)
heapq.heappush(arr, 9)
heapq.heappush(arr, 2)

#converts to a heap, default min heap
print(arr)

#heapify --> default min heap
arr = [5, 2, 8, 1, 9, 3]
heapq.heapify(arr)
print(arr)

#max heap
arr1 = list(map(lambda x: -x, arr))
heapq.heapify(arr1)
arr= list(map(lambda x: -x, arr1))
print(arr)

#
