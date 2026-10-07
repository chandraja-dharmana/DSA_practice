#possible permutations with repetitions

arr = [1, 2, 3]

res=[]
perm=[]

def bt(num1):

    if len(perm)==len(arr)-1:
        tmp=''.join(map(str,num1))
        res.append(tmp)
        return

    for i in arr:
        perm.append(i)
        bt(perm)
        perm.pop()


bt(arr)
print("result:", res)
print("number of permutations: ", len(res))


# result: ['111', '112', '113', '121', '122', '123', '131', '132',
#          '133', '211', '212', '213', '221', '222', '223', '231',
#          '232', '233', '311', '312', '313', '321', '322', '323', '331', '332', '333']
# number of permutations:  27


# ###same thing as above with print statements

# arr = [1, 2, 3]

# res=[]
# comb=[]

# def bt(num1):

#     if len(comb)==len(arr):
#         tmp=''.join(map(str,num1))
#         print("tmp:",tmp)
#         res.append(tmp)
#         print("res:",res)
#         return

#     for i in arr:
#         print("i:",i)
#         comb.append(i)
#         print("comb:",comb)
#         bt(comb)
#         comb.pop()
#         print("comb after pop:",comb)


# bt(arr)
# print("result:", res)
# print("number of combinations: ", len(res))