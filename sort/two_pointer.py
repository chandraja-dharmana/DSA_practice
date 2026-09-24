arr = [1, 2, 3, 4, 5]
k = 7
len_arr=len(arr)
l=0
r=0
max_len=0
sum_arr=0
max_l=0
max_r=0

for r in range(len_arr):
    sum_arr=sum_arr+arr[r]
    while(sum_arr>k):
        sum_arr=sum_arr-arr[l]
        l+=1
    if (sum_arr<=k):
        if (r-l+1)>max_len:
            max_l=l
            max_r=r
        max_len=max(max_len,r-l+1)

print(max_len)
print(arr[max_l:max_r+1])


# while (r<len_arr):
#     sum_arr=sum_arr+arr[r]
#     while(sum_arr>k):
#         sum_arr=sum_arr-arr[l]
#         l+=1
#     if (sum_arr<=k):
#         if (r-l+1)>max_len:
#             max_l=l
#             max_r=r
#         max_len=max(max_len,r-l+1)
#     r+=1

# print(max_len)
# print(arr[max_l:max_r+1])


# #verbose with all print statements
# while (r<len_arr):
#     print("arr[r]",arr[r])
#     sum_arr=sum_arr+arr[r]
#     print("sum_arr",sum_arr)
#     while(sum_arr>k):
#         print("arr[l]",arr[l])
#         sum_arr=sum_arr-arr[l]
#         print("sum_arr",sum_arr)
#         l+=1
#     if (sum_arr<=k):
#         if (r-l+1)>max_len:
#             max_l=l
#             max_r=r
#             print("max_l",max_l)
#             print("max_r",max_r)
#         max_len=max(max_len,r-l+1)
#         print("max_len",max_len)
#         print("l",l)
#         print("r",r)

#     r+=1

# print(max_len)
# print(arr[max_l:max_r+1])