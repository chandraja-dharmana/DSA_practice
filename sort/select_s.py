a= [7, 2, 9, 4, 1]
len_arr = len(a)

for i in range(len_arr):
    print(f"i : {i}")
    min_ind=i
    print(f"before i loop min_val: {a[i]}")
    for j in range(i,len_arr-1):
        print(f"j : {j}")
        print(f"before j loop min_val: {a[i]}")
        print(f"a[j+1]: {a[j+1]}")
        if a[min_ind] > a[j+1]:
            min_ind=j+1 # going in one direction from left to right
        print(f"after min_val: {a[i]}")
    print(f"min_ind: {min_ind}")
    tmp = a[min_ind]
    a[min_ind]=a[i]
    a[i]=tmp
    print(a)
print(a)


# for i in range(len_arr):
#     print(f"i : {i}")
#     min_ind=i
#     min_val=a[i]
#     print(f"before i loop min_val: {min_val}")
#     for j in range(i,len_arr-1):
#         print(f"j : {j}")
#         print(f"before j loop min_val: {min_val}")
#         print(f"a[j+1]: {a[j+1]}")
#         if min_val > a[j+1]:
#             min_ind=j+1 # going in one direction from left to right
#             min_val=a[j+1]
#         print(f"after min_val: {min_val}")
#     print(f"min_ind: {min_ind}")
#     tmp = a[min_ind]
#     a[min_ind]=a[i]
#     a[i]=tmp
#     print(a)
# print(a)




################################################################################################
#####################     BELOW IS WRONG        #############################################


# # below is too elaborate
# # min() to get the minimum element in array
# # index() for min element's index
# for i in range(len_arr):
#     print(f"i : {i}")
#     min_val=a[i]
#     print(f"before i loop min_val: {min_val}")
#     for j in range(i,len_arr-1):
#         print(f"j : {j}")
#         print(f"before j loop min_val: {min_val}")
#         print(f"a[j+1]: {a[j+1]}")
#         if min_val > a[j+1]:
#             min_val=a[j+1]
#         print(f"after min_val: {min_val}")
#     for k in range(len_arr):
#         if a[k]==min_val:
#             min_ind = k
#             break
#     print(f"min_ind: {min_ind}")
#     tmp = a[min_ind]
#     a[min_ind]=a[i]
#     a[i]=tmp
#     print(a)
# print(a)


# #simpler one with min() and index())
# for i in range(len_arr):
#     print(i)
#     min_val = min(a[i:len_arr])
#     min_ind=a.index(min_val)
#     tmp = a[min_ind]
#     a[min_ind]=a[i]
#     a[i]=tmp
# print(a)
