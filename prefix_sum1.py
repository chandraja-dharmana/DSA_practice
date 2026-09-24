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

hash_map1={} #prefix sum - frequency
count=0

for i in range(len_arr):
    ps=sum_arr[i]-arr_val
    if not ps: #subarray starts from index 0
        count+=1
    if sum_arr[i] in hash_map1:
        hash_map1[sum_arr[i]]+=1
    else:
        hash_map1[sum_arr[i]]=1
    if ps in hash_map1: # previous prefix sum exists
        count+=hash_map1[ps]
                

print("count:",count)
print("hash map:",hash_map1)