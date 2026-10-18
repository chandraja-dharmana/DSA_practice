# Knuth-Morris-Pratt KMP String Matching Algorithm

arr=['a','b','a','b','c','a','b','c','a','b','a','b','a','b','d']

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
#result - [0, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 3, 4, 0]

