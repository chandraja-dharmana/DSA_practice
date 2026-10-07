#Subsets: Given arr = [1, 2], generate all possible subsets.
#order doesn't matter ----> combination
#non-repeating

arr = [1, 2, 3]

res=set()
comb=[]

def bt(num1, len_comb):

    if len(comb)==len_comb:
        #sort and set() 112, 211, 121 --> only one 112
        num2=sorted(num1) # do not use num1.sort( )
        tmp=''.join(map(str,num2))
        tmp1=int(tmp)
        res.add(tmp1)
        return

    #comb=num1 both have the same value

    for i in arr:
        if i not in comb: #remove only this line for non-repeating
            comb.append(i)
            bt(comb, len_comb)
            comb.pop()


for j in range(1, len(arr)+1):
    bt(arr,j)

final_res=[]
#all subsets as lists
for k in res:
    tmp2=list(map(int,str(k)))
    final_res.append(tmp2)

final_res.append([])
print("result:", final_res)
print("number of combinations: ", len(final_res))


# repeating
# order does not matter
# 10 combinations for 3 digit
# 111, 112, 113, 122, 123, 133, 222, 223, 233, 333

# result: ['11', '12', '13', '22', '23', '33']
# number of combinations:  6 for 2 digit

# result: [[1], [2], [3], [1, 3, 3], [1, 1], [1, 2], [1, 3],
#          [2, 2], [2, 3], [3, 3], [3, 3, 3], [2, 2, 2], [2, 2, 3],
#     [2, 3, 3], [1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 2], [1, 2, 3], []]
# number of combinations:  20

#-----------------------------------------#

# non-repeat
# result: [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3], []]
# number of combinations:  8

# ####same thing above with print statements
# arr = [1, 2, 3]

# res=set()
# comb=[]

# def bt(num1, len_comb):

#     if len(comb)==len_comb:
#         #sort and set() 112, 211, 121 --> only one 112
#         num2=sorted(num1) # do not use num1.sort( )
#         tmp=''.join(map(str,num2))
#         tmp1=int(tmp)
#         res.add(tmp1)
#         #print(res)
#         return

#     #comb=num1 both have the same value

#     for i in arr:
#         #if i not in comb: #remove only this line for non-repeating
#         print("i: ",i)
#         comb.append(i)
#         print("comb: ",comb)
#         bt(comb, len_comb)
#         print("comb after return: ",comb)
#         comb.pop()
#         print("comb after pop: ",comb)


# for j in range(1, len(arr)+1):
#     bt(arr,j)

# final_res=[]
# #all subsets as lists
# for k in res:
#     tmp2=list(map(int,str(k)))
#     final_res.append(tmp2)

# final_res.append([])
# print("result:", final_res)
# print("number of combinations: ", len(final_res))