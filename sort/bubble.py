a=[8, 5, 3, 7, 2]
len_arr = len(a)

# #the one below goes from the end toward the start
# for i in range(len_arr-1,0,-1):
#     print(f"i : {i}")
#     for j in range(i):
#         print(f"j: {j}")
#         if a[j] > a[j+1]:
#             print(f"before {a[j]}")
#             print(f"before {a[j+1]}")
#             tmp= a[j]
#             a[j]= a[j+1]
#             a[j+1]=tmp
#             print(f"after {a[j]}")
#             print(f"after {a[j+1]}")
#     print(a)
# print(a)


## the one below goes from the start towards the end
## textbook format
for i in range(len_arr):
    print(f"i : {i}")
    for j in range(0, len_arr - i - 1):
        print(f"j: {j}")
        if a[j] > a[j+1]:
            print(f"before {a[j]}")
            print(f"before {a[j+1]}")
            tmp= a[j]
            a[j]= a[j+1]
            a[j+1]=tmp
            print(f"after {a[j]}")
            print(f"after {a[j+1]}")
    print(a)
print(a)