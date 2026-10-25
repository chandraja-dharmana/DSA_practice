arr = [5, 2, 8, 1, 3]
arr_len=len(arr)

# #bubble sort


# for j in range(arr_len-1,0,-1): # n-1 iterations
#     print("j:",j)
#     for i in range(j): 
#         print("i:",i)
#         if arr[i]<arr[i+1]: #descending order
#             arr[i],arr[i+1]=arr[i+1],arr[i]

# print(arr) #[24, 10, 9, 8, 7, 3, 2, 1]

#### RECURSIVE
# def rec_bubble(arr,j):

#     if j<=0:
#         return
    
#     for i in range(j):
#         if arr[i]<arr[i+1]: #descending order
#             arr[i],arr[i+1]=arr[i+1],arr[i]

#     rec_bubble(arr,j-1)

# rec_bubble(arr,arr_len-1)
# print(arr)


#########################################################################

# #insertion sort


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

#arr = [5, 2, 8, 1, 3]

# #### RECURSIVE
def rec_insert(arr,i):

    if i > len(arr)-1:
        return
    
    key=arr[i]
    j=i-1
    while j >= 0 and arr[j] > key: #ascending
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key
    rec_insert(arr,i+1)

rec_insert(arr,1)
print(arr)


####    NO RECURSIVE SEELCTION SORT  #### 