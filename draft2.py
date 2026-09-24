# str_list=["abc","def","ghi"]
# print(str(str_list))
# #output : ['abc', 'def', 'ghi']

# num_lis=[1,2,3]
# print(str(num_lis))
# #output : [1, 2, 3]
# a="".join(str(num_lis))
# print(a)
# #output : [1, 2, 3]


# num_lis=["1","2","3"]
# a="".join(num_lis)
# print(a)
# #output : 123

nums = [1, 2, 3, 4]

result = map(str, nums)
a="".join(list(result))
print(a)