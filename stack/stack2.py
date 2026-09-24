#Valid Parentheses
# #assuming in1 contains only "(" or ")", no other characters

def is_valid_parentheses(s):

    in1=list(s)
    while in1:
        pair_found = False
        for j in range(len(in1) - 1, 0, -1):
            if in1[j] == ")" and in1[j - 1] == "(":
                in1.pop(j)
                in1.pop(j - 1)
                pair_found = True
                break
        if not pair_found:
            break

    return in1 == []

# test cases
cases = [
    "()()",            # True
    "(()",             # False
    "((())())",        # True
    "(()))",           # False
    "(()(()))",        # True
    "((())(()))",      # True
    "())((())",        # False
    "(((())))()(()())",  # True
    "((())())(()",     # False
    "())(())",         # False
]

for value in cases:
    print(value, "->", is_valid_parentheses(value))


# #working only for true cases, not false
# while in1!=[]: 
#     for j in range(len(in1)-1,0,-1):
#         if in1[j] ==")" and in1[j-1]=="(":
#             in1.pop(j)
#             in1.pop(j-1)
#             break


# in1=list(in1_str)
# in_pair=[]
# in_nopair=[]

# while in1!=[]:
#     print("outside for in1: ",in1)
#     print("len(in1): ",len(in1))
#     for j in range(len(in1)-1,0,-1):
#         print("j: ",j)
#         print("j-1: ",j-1)
#         print("in1[j]: ",in1[j])
#         print("in1[j-1]: ",in1[j-1])
#         if in1[j] ==")" and in1[j-1]=="(":
#             print("j: ",j)
#             print("j-1: ",j-1)
#             print("in1[j]: ",in1[j])
#             print("in1[j-1]: ",in1[j-1])
#             in1.pop(j)
#             in1.pop(j-1)
#             print("in1: ",in1)
#             break


# ##below is wrong
# open_ct = in1.count("(")
# close_ct = in1.count(")")
# print("open count: ",open_ct)
# print("close count: ",close_ct)

# if open_ct == close_ct:
#     print(True)
# else:
#     print(False)





