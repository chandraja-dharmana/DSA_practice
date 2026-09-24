# a=[40,20,50,10,30]

# max_elem=a[0]
# for i in range(len(a)-1):
#     if max_elem<a[i+1]:
#         max_elem=a[i+1]

# a.remove(max_elem)

# second_max=-1 # assume array doesn't contain int numbers
# for i in range(len(a)-1):
#     if (second_max<a[i+1] and a[i+1]!=max_elem):
#         second_max=a[i+1]
# print(second_max)


# # if not removing the max element
# # if second_max<a[i+1] and a[i+1]!=max_elem:

# # [ 1 2 4 5 7 7 ] second largest element is not 7, it is 5
# # [ 7 7 7 7 7 7 ] no second largest element
# # [ 1 7 7 7 7 7 ] worst case O(n)
# ===========================================================

#optimal one

arr = [10, 5, 8, 20, 15]

largest = float('-inf')
second_largest = float('-inf')

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)