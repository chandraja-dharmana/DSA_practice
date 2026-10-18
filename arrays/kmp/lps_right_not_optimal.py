# Knuth-Morris-Pratt KMP String Matching Algorithm

arr=['a','b','a','b','c','a','b','c','a','b','a','b','a','b','d']

#don't use set - we need a specific pattern
len_arr=len(arr)
lps=[0]*len_arr

lps[0]=0
len_lps=0

for i in range(1,len_arr):
    while len_lps>=0:
        if arr[i]==arr[len_lps]: # match
            len_lps+=1
            lps[i]=len_lps
            break
        elif arr[i]!=arr[len_lps]: # mismatch
            if len_lps==0:
                lps[i]=0
                break
            elif len_lps>0:
                len_lps=lps[len_lps-1]


print(lps)
#result - [0, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 3, 4, 0]

