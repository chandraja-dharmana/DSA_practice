# this will work if we need onlt length of the longest subarray
# it won't work if we need the actual subarray

arr = [2, 5, 1, 10, 10]
k = 14
len_arr=len(arr)
l=0
r=0
max_len=0
sum_arr=0
max_l=0
max_r=0

for r in range(len_arr):
    sum_arr=sum_arr+arr[r]
    if(sum_arr>k):
        sum_arr=sum_arr-arr[l]
        l+=1
    if (sum_arr<=k):
        if (r-l+1)>max_len:
            max_l=l
            max_r=r
        max_len=max(max_len,r-l+1)

print(max_len)
print(arr[max_l:max_r+1])
