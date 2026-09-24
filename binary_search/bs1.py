# Problem 1: Search for an Element
# Given a sorted array, find whether a given number exists using binary search.

arr = [2, 4, 6, 8, 10, 12, 14]
tgt1=12

# WHILE

def arr_sub(arr, tgt1):
    
    elem_not_present=True
    while elem_not_present:

        len_arr=len(arr)
        middle_elem_ind = len_arr//2

        midd_elem = arr[middle_elem_ind]

        # [2, 4, 6, 8, 10, 12] arr[3] = 8
        # [2, 4, 6, 8, 10, 12, 14]  arr[3] = 8


        if midd_elem > tgt1 and len_arr>1 :
            arr=arr[0:middle_elem_ind]
            elem_not_present=True
        elif midd_elem < tgt1 and len_arr>1 :
            arr=arr[middle_elem_ind:len_arr]
            elem_not_present=True
        elif midd_elem == tgt1:
            print("element found")
            elem_not_present=False
            break
        elif len_arr==1 and midd_elem!=tgt1:
            elem_not_present=False
            print("element not found")
            break
        print(arr)
            

arr_sub(arr, tgt1)





