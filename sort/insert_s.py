# a=[5, 3, 4, 1, 2]
# arr_len = len(a)


# # below implementation is correct but not the most efficient
# # It doesn't break early from the inner loop when no more
# # swaps are needed (only wasted checks).
# for i in range(arr_len-1):
#     print(f"i: {i}")
#     if a[i]>a[i+1]:
#         for j in range(i+1,0,-1):
#             print(f"j: {j}")
#             if a[j-1]>a[j]:
#                 tmp = a[j-1]
#                 a[j-1]=a[j]
#                 a[j]=tmp
#     print(a)
# print(a)


#standard, most efficient
arr = [5, 3, 4, 1, 2]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print(arr)