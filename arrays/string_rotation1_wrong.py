s2 = "abcd"
len_arr=len(s2)

#s3 = "cdab"
s3 = "acbd"
sr=list(s2)
sl=list(s2)
num_comb_left=num_comb_right=len_arr
comb_right = []
comb_left = []
all_comb=[]

for i in range(num_comb_right):
    tmp = sr[-1]
    for i in range(1,len_arr):
        sr[-i] = sr[-i-1]

    sr[-len_arr] =  tmp
    br="".join(sr)
    comb_right.append(br)

print(comb_right)


for i in range(num_comb_left):
    tmp = sl[0]
    for i in range(1,len_arr):
        sl[i-1] = sl[i]

    sl[len_arr-1] =  tmp
    bl="".join(sl)
    comb_left.append(bl)

print(comb_left)

all_comb=comb_right+comb_left

if s3 in all_comb:
    print("is a rotation")
else:
    print("is not a rotation")



# right
# tmp = s1[-1]
# s1[-1] = s1[-2]
# s1[-2] = s1[-3]
# s1[-3] = s1[-4]
# s1[-4] =  tmp

# left
# tmp=s[0]
# s[0]=s[1]
# s[1]=s[2]
# s[2]=s[3]
# s[3]=tmp




