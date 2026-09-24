# Problem 1: Search for an Element
# Given a sorted array, find whether a given number exists using binary search.

arr = [2, 4, 6, 8, 10, 12, 14]
tgt1=2
i=0

# RECURSION

def arr_sub(arr, tgt1):
    global i

    print("iteration: ", i)
    print("array: ", arr)

    len_arr=len(arr)
    middle_elem_ind = len_arr//2

    midd_elem = arr[middle_elem_ind]
    print("outside midd_elem: ", midd_elem)

    if midd_elem == tgt1:
        print("element: ", midd_elem)
        print("element found")
    elif len_arr==1 and midd_elem != tgt1:
        print("element not found")
    else:
        if midd_elem > tgt1 and len_arr>1 :
            arr=arr[0:middle_elem_ind]
        elif midd_elem < tgt1 and len_arr>1 :
            arr=arr[middle_elem_ind:len_arr]

        i+=1
        arr_sub(arr, tgt1)

#arr_sub(arr, tgt1)


test_cases = {
    "example1": {
        "arr": [3, 7, 12, 18, 25, 31, 39, 46, 52, 61, 68, 74, 81, 90, 97],
        "target": 7,
        "output": "Found"
    },

    "example2": {
        "arr": [5, 11, 17, 23, 29, 34, 41, 48, 56, 63, 71, 78, 85, 92, 99],
        "target": 92,
        "output": "Found"
    },

    "example3": {
        "arr": [10, 20, 30, 40, 50, 60, 70, 80, 90],
        "target": 55,
        "output": "Not Found"
    },

    "example4": {
        "arr": [4, 9, 15, 22, 28, 35, 41, 48, 53],
        "target": 28,
        "output": "Found"
    },

    "example5": {
        "arr": [-50, -42, -35, -27, -18, -10, -3, 5, 12, 21, 30],
        "target": -27,
        "output": "Found"
    },

    "example6": {
        "arr": [-80, -65, -51, -44, -32, -21, -9, 4, 16, 29, 45],
        "target": -50,
        "output": "Not Found"
    },

    "example7": {
        "arr": [-100, -75, -60, -42, -25, -11, 0, 8, 19, 34, 57, 81, 120],
        "target": 34,
        "output": "Found"
    },

    "example8": {
        "arr": [42],
        "target": 42,
        "output": "Found"
    },

    "example9": {
        "arr": [42],
        "target": 17,
        "output": "Not Found"
    },

    "example10": {
        "arr": [12, 24, 36, 48, 60, 72, 84, 96],
        "target": 100,
        "output": "Not Found"
    },

    "example11": {
        "arr": [2, 5, 9, 14, 21, 29, 38, 48, 59, 71, 84, 98, 113, 129, 146, 164, 183, 203],
        "target": 129,
        "output": "Found"
    },

    "example12": {
        "arr": [1, 4, 8, 13, 19, 26, 34, 43, 53, 64, 76, 89, 103, 118, 134, 151, 169, 188],
        "target": 100,
        "output": "Not Found"
    },

    "example13": {
        "arr": [2, 4, 4, 4, 7, 9, 12, 12, 15, 18, 21],
        "target": 12,
        "output": "Found"
    },

    "example14": {
        "arr": [1, 3, 3, 3, 6, 8, 8, 11, 14, 14, 20],
        "target": 10,
        "output": "Not Found"
    },

    "example15": {
        "arr": [-120, -95, -73, -51, -30, -12, 0, 17, 29, 44, 63, 81, 102, 127, 155, 190, 225],
        "target": 102,
        "output": "Found"
    }
}

for i in range(15):
    eg = "example"+str(i+1)
    print(eg)
    arr = test_cases[eg]["arr"]
    target = test_cases[eg]["target"]
    arr_sub(arr, target)





# arr = [2, 4, 6, 8, 10, 12, 14]
# tgt1=6
# i=0
# elem_ind = []
# greater=[]
# smaller=[]
# greater.append(False)
# smaller.append(False)
# comp=[]

# def arr_sub(arr, tgt1):
#     global i
#     global tgt_ind
#     global greater
#     global smaller
#     print("iteration: ", i)
#     print("array: ",arr)

#     len_arr=len(arr)
#     if len_arr%2==0:
#         middle_elem_ind = len_arr//2
#     else:
#         middle_elem_ind = len_arr//2

#     elem_ind.append(middle_elem_ind)
#     # if i==0:
#     #     tgt_ind = middle_elem_ind
#     print("outside middle_elem_ind: ", middle_elem_ind)
#     #print("target index: ",tgt_ind)

#     midd_elem = arr[middle_elem_ind]
#     print("outside midd_elem: ", midd_elem)
#     print("outside elem_ind: ", elem_ind)

#     if midd_elem == tgt1:
#         print("element found")
#         if i>0:
#             if greater[-1]:
#                 print("greater")
#                 tgt_ind=tgt_ind+elem_ind[-1]
#             if smaller[-1]:
#                 print("smaller")
#                 tgt_ind=tgt_ind-elem_ind[-1]
#         print("target index: ",tgt_ind)
#     elif len_arr==1 and midd_elem != tgt1:
#         print("element not found")
#     else:
#         if midd_elem > tgt1 and len_arr>1 :
#             smaller.append(True)
#             print("smaller")
#             arr=arr[0:middle_elem_ind]
#             if i==0:
#                 tgt_ind=middle_elem_ind
#             elif i>0:
#                 if greater[-2]==True and greater[-1]==False:
#                     print("----add----")
#                     tgt_ind=tgt_ind+elem_ind[-1]
#                 if greater[-2]==False and greater[-1]==False:
#                     print("----subtract-----")
#                     tgt_ind=tgt_ind-elem_ind[-1]
#             print("inside 1st target index: ",tgt_ind)
#         elif midd_elem < tgt1 and len_arr>1 :
#             greater.append(True)
#             print("greater")
#             arr=arr[middle_elem_ind:len_arr]
#             if i==0:
#                 tgt_ind=middle_elem_ind
#             elif i>0:
#                 if greater[-2]==True and greater[-1]==False:
#                     print("----subtract-----")
#                     tgt_ind=tgt_ind-elem_ind[-1]
#                 if greater[-2]==True and greater[-1]==True:
#                     print("----add----")
#                     tgt_ind=tgt_ind+elem_ind[-1]

#             print("inside 2nd target index: ",tgt_ind)
#         i+=1
#         arr_sub(arr, tgt1)

# arr_sub(arr, tgt1)





