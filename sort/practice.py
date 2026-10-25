arr=[7,3,8,1,24,9,2,10]
arr_len=len(arr)

#########################################################################

# # #bubble sort

# for j in range(arr_len-1,0,-1): # n-1 iterations
#     print("j:",j)
#     for i in range(j): 
#         print("i:",i)
#         if arr[i]<arr[i+1]: #descending order
#             arr[i],arr[i+1]=arr[i+1],arr[i]

# print(arr) #[24, 10, 9, 8, 7, 3, 2, 1]

#########################################################################

# #insertion sort


### Attempt 1 - This is wrong
# It is closer to “repeatedly take the max from the remaining part and 
# place it at the front.”

# for i in range(arr_len-1): # n-1 iterations
#     max_elem=max(arr[i:]) #descending order
#     max_ind=arr.index(max_elem)
#     arr[i], arr[max_ind]=arr[max_ind],arr[i]  

# print(arr)

# # Attempt 2 
# # This is wrong, same as above

# for i in range(arr_len-1): # n-1 iterations
#     for j in range(i,arr_len):
#         if arr[i]<arr[j]: #descending order
#             arr[i],arr[j]=arr[j],arr[i]

# print(arr)

# # Standard one
# arr = [5, 3, 4, 1, 2]

# n = len(arr)

# for i in range(1, n):
#     key = arr[i]
#     j = i - 1

#     while j >= 0 and arr[j] > key:
#         arr[j + 1] = arr[j]
#         j -= 1

#     arr[j + 1] = key

# print(arr)

#########################################################################

# #selection sort

# for i in range(arr_len-1): #n-1 iterations
#     for j in range(i,arr_len):
#         max_elem=arr[i] #descending order
#         if max_elem<arr[j]:
#             max_elem=arr[j]
#         max_ind=arr.index(max_elem)
#         arr[i], arr[max_ind]=arr[max_ind],arr[i]

# print(arr)

# #standard one
# for i in range(arr_len-1):
#     max_idx = i
#     for j in range(i+1, arr_len):
#         if arr[j] > arr[max_idx]:
#             max_idx = j
#     arr[i], arr[max_idx] = arr[max_idx], arr[i]

# # print(arr)

#########################################################################
