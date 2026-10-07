#possible permutations without repetitions

arr = [1, 2, 3]

res=[]
perm=[]

def bt(num1):

    if len(perm)==len(arr):
        tmp=''.join(map(str,num1))
        res.append(tmp)
        return
    
    for i in arr:
        if i not in perm:
            perm.append(i)
            bt(perm)
            perm.pop()


bt(arr)
print("result:", res)
print("number of permutations: ", len(res))



# #same thing above with print statements
# arr = [1, 2, 3]

# res=[]
# perm=[]

# def bt(num1):

#     if len(perm)==len(arr):
#         tmp=''.join(map(str,num1))
#         print("tmp:",tmp)
#         res.append(tmp)
#         return
    
#     print("arr:",arr)
#     for i in arr:
#         print("i:",i)
#         print("perm:",perm)
#         if i not in perm:
#             perm.append(i)
#             bt(perm)
#             perm.pop()


# bt(arr)
# print("result:", res)
# print("number of permutations: ", len(res))
