# #Number of operations = len(a) * len(b) 
# #12*6 = 72
# a=[1,2,1,4,5,2,3,3,6,1,4,3]
# b=list(set(a)) #[1, 2, 3, 4, 5, 6]
# ctr=[0]*len(b)
# ctr_dict={}
# for i in range(len(a)):
#     for j in range(len(b)):
#         if b[j]==a[i]:
#              ctr[j]+=1
#         if i==len(a)-1:
#             ctr_dict[b[j]]=ctr[j]

# print(ctr_dict) 
# ctr = [3, 2, 3, 2, 1, 1]


