# Knuth-Morris-Pratt KMP String Matching Algorithm
# https://chatgpt.com/share/6ad496bd-b780-83ee-92d1-e3c8a82b93d7

arr=['a','b','a','b','d']

#don't use set - we need a specific pattern
len_arr=len(arr)
lps=[0]*len_arr

lps[0]=0
len_lps=0

for i in range(1,len_arr):
    while len_lps>0 and arr[i]!=arr[len_lps]:
        len_lps=lps[len_lps-1]
    if arr[i]==arr[len_lps]:
        len_lps+=1
    lps[i]=len_lps

print(lps)
#result - [0, 0, 1, 2, 0]

############################################################################3

# Find if subarr occurs in arr1

subarr =['a', 'b', 'a', 'b', 'd'] 
arr1 = ['a', 'b', 'a', 'b', 'c',
        'a', 'b', 'c', 'a', 'b', 'a', 'b', 'a', 'b', 'd']

# lps = [0, 0, 1, 2, 0]

j = 0
i = 0


while i < len(arr1):

    if subarr[j] == arr1[i]:
        j += 1
        i += 1

        if j == len(subarr):
            print("found")
            break

    else:
        if j == 0:
            i += 1
        else:
            j = lps[j - 1]

else:
    print("not found")

# used while ... else. 
# The else executes only if the loop finishes normally, without hitting break.