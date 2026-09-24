#print number of subarrays along with the subarray

arr= [9,4,0,20,3,10,5]
len_arr=len(arr)
arr_val=33

sum1=0
sum_arr=[]
for i in range(len_arr):
    sum1+=arr[i]
    sum_arr.append(sum1)

print(sum_arr)

pos_map1={} #prefix sum - occurence_position
max_length=0

for i in range(len_arr):
    ps=sum_arr[i]-arr_val
    if ps==0: #subarray starts from index 0
        max_length=i+1

    if sum_arr[i] in pos_map1: # previous prefix sum exists
        len1 = i - pos_map1[sum_arr[i]]
        max_length = max(len1, max_length)
    else:
        pos_map1[sum_arr[i]]=i
    # if ps in pos_map1: # previous prefix sum exists
    #     count+=pos_map1[ps]
                
print(max_length)
print("pos map:",pos_map1)