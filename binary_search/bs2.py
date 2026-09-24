# Problem 2: Find the Position
# Given a sorted array and a target, return the index of the target.

### ALL WRONG ################

arr = [2, 4, 6, 8, 10, 12, 14]
tgt1=10
i=0
greater=False
smaller=False
elem_ind=[]
op=[]

# RECURSION

def arr_sub(arr, tgt1):
    global i, tgt_ind, op
    global greater, smaller
    print("iteration: ", i)
    print("array: ", arr)

    len_arr=len(arr)
    middle_elem_ind = len_arr//2
    elem_ind.append(middle_elem_ind)
    len_ind=len(elem_ind)
    print("elem_ind: ", elem_ind)
    if i==0:
        tgt_ind = middle_elem_ind
        print("tgt index: ", tgt_ind)

    midd_elem = arr[middle_elem_ind]

    if midd_elem == tgt1:
        print("element: ", midd_elem)
        print("element found")
        if len_ind==1:
            print("tgt index: ", tgt_ind)
        if len_ind>1:
            print("op: ", op)
            if '-' in op and smaller:
                tgt_ind+=1
            for i in range(len(op)):
                if op[i] == '+':
                    tgt_ind += elem_ind[i + 1]
                elif op[i] == '-':
                    tgt_ind -= elem_ind[i + 1]

            print("tgt index: ", tgt_ind)
    elif len_arr==1 and midd_elem != tgt1:
        print("element not found")
    else:
        if midd_elem > tgt1 and len_arr>2:
            smaller=True
            print("smaller")
            op.append('-')
            arr=arr[0:middle_elem_ind+1]
        elif midd_elem > tgt1 and len_arr==2: #edge case
            print("element: ", arr[0])
            print("element found")
            print("tgt index: ", 0)
        elif midd_elem < tgt1 and len_arr>1:
            greater=True
            print("greater")
            op.append('+')
            arr=arr[middle_elem_ind:len_arr]

        i+=1
        if not (midd_elem > tgt1 and len_arr==2):
            arr_sub(arr, tgt1)

arr_sub(arr, tgt1)


# test_cases = {
#     "example1": {
#         "arr": [3, 7, 12, 18, 25, 31, 39, 46, 52, 61, 68, 74, 81, 90, 97],
#         "target": 7,
#         "output": "Found"
#     },

#     "example2": {
#         "arr": [5, 11, 17, 23, 29, 34, 41, 48, 56, 63, 71, 78, 85, 92, 99],
#         "target": 92,
#         "output": "Found"
#     },

#     "example3": {
#         "arr": [10, 20, 30, 40, 50, 60, 70, 80, 90],
#         "target": 55,
#         "output": "Not Found"
#     },

#     "example4": {
#         "arr": [4, 9, 15, 22, 28, 35, 41, 48, 53],
#         "target": 28,
#         "output": "Found"
#     },

#     "example5": {
#         "arr": [-50, -42, -35, -27, -18, -10, -3, 5, 12, 21, 30],
#         "target": -27,
#         "output": "Found"
#     },

#     "example6": {
#         "arr": [-80, -65, -51, -44, -32, -21, -9, 4, 16, 29, 45],
#         "target": -50,
#         "output": "Not Found"
#     },

#     "example7": {
#         "arr": [-100, -75, -60, -42, -25, -11, 0, 8, 19, 34, 57, 81, 120],
#         "target": 34,
#         "output": "Found"
#     },

#     "example8": {
#         "arr": [42],
#         "target": 42,
#         "output": "Found"
#     },

#     "example9": {
#         "arr": [42],
#         "target": 17,
#         "output": "Not Found"
#     },

#     "example10": {
#         "arr": [12, 24, 36, 48, 60, 72, 84, 96],
#         "target": 100,
#         "output": "Not Found"
#     },

#     "example11": {
#         "arr": [2, 5, 9, 14, 21, 29, 38, 48, 59, 71, 84, 98, 113, 129, 146, 164, 183, 203],
#         "target": 129,
#         "output": "Found"
#     },

#     "example12": {
#         "arr": [1, 4, 8, 13, 19, 26, 34, 43, 53, 64, 76, 89, 103, 118, 134, 151, 169, 188],
#         "target": 100,
#         "output": "Not Found"
#     },

#     "example13": {
#         "arr": [2, 4, 4, 4, 7, 9, 12, 12, 15, 18, 21],
#         "target": 12,
#         "output": "Found"
#     },

#     "example14": {
#         "arr": [1, 3, 3, 3, 6, 8, 8, 11, 14, 14, 20],
#         "target": 10,
#         "output": "Not Found"
#     },

#     "example15": {
#         "arr": [-120, -95, -73, -51, -30, -12, 0, 17, 29, 44, 63, 81, 102, 127, 155, 190, 225],
#         "target": 102,
#         "output": "Found"
#     }
# }

# for i in range(15):
#     eg = "example"+str(i+1)
#     print(eg)
#     arr = test_cases[eg]["arr"]
#     target = test_cases[eg]["target"]
#     arr_sub(arr, target)