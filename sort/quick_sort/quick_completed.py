arr=[4,6,2,5,7,9,1,3]

# using one pointer P from left to right
# descending order
# pivot as the first element


def quicksort(arr,low,high):

    len_arr=high-low
    if len_arr<2:
        return
    
    p=arr[low] # first element as pivot
    c=low+1
    l=low+1
    h=high

    # if l>=h:  #This also works
    #     return 
    
    for i in range(l,h):
        if arr[i]>p:
            arr[i],arr[c]=arr[c],arr[i]
            c+=1

    arr[low],arr[c-1]=arr[c-1],arr[low]
    
    quicksort(arr,low,c)
    quicksort(arr,c,h)

quicksort(arr,0,len(arr))
print(arr)



#################################################################################
# #SAME AS ABOVE WITH PRINT STATEMENTS

# arr=[4,6,2,5,7,9,1,3]

# # using one pointer P from left to right
# # descending order
# # pivot as the first element


# def quicksort(arr,low,high):

#     len_arr=high-low
#     if len_arr<2:
#         return
    
#     p=arr[low] # first element as pivot
#     print("pivot value:",p)
#     c=low+1
#     l=low+1
#     h=high
#     print(f"l: {l}, h: {h}")

#     # if l>=h:  #This also works
#     #     return 
    
#     for i in range(l,h):
#         if arr[i]>p:
#             print(f"i:{i}\tarr[i]:{arr[i]}")
#             print(f"c:{c}\tarr[c]:{arr[c]}")
#             arr[i],arr[c]=arr[c],arr[i]
#             print("inside if arr:",arr)
#             c+=1

#     arr[low],arr[c-1]=arr[c-1],arr[low]

#     print("outside if arr:",arr)
   
#     print(f"low: {low}, c: {c}")
#     left_arr=arr[low:c]
#     print("left arr:",left_arr)
    
#     print(f"c: {c}, h: {h}")
#     right_arr=arr[c:h]
#     print("right arr:",right_arr)
    
#     quicksort(arr,low,c)
#     quicksort(arr,c,h)

# quicksort(arr,0,len(arr))
# print(arr)

#################################################################################

#THIS IS WRONG
# arr=[4,6,2,5,7,9,1,3]

# # using one pointer P from left to right
# # descending order
# # pivot as the first element


# def quicksort(arr,low,high):

#     if len(arr)<2:
#         return
    
#     p=arr[low] # first element as pivot
#     print("pivot value:",p)
#     c=low+1
#     l=low+1
#     h=high
#     print(f"l: {l}, h: {h}")
    
#     for i in range(l,h):
#         if arr[i]>p:
#             print(f"i:{i}\tarr[i]:{arr[i]}")
#             print(f"c:{c}\tarr[c]:{arr[c]}")
#             arr[i],arr[c]=arr[c],arr[i]
#             print("inside if arr:",arr)
#             c+=1

#     arr[low],arr[c-1]=arr[c-1],arr[low]



#     print("outside if arr:",arr)
#     print(f"low: {low}, c: {c}")
#     left_arr=arr[low:c]
#     print(f"c: {c}, h: {h}")
#     right_arr=arr[c:h]
#     print("right arr:",right_arr)
#     print("left arr:",left_arr)
#     quicksort(left_arr,low,c)
#     quicksort(right_arr,c,h)

# quicksort(arr,0,len(arr))
# print(arr)