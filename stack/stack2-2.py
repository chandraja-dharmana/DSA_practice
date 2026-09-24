# Valid Parentheses
# assuming string contains only "(" or ")", no other characters


# def is_valid_parentheses(s):
#     stack = []

#     for ch in s:
#         if ch == "(":
#             stack.append(ch)
#         elif ch == ")":
#             if stack and stack[-1] == "(":
#                 stack.pop()
#             else:
#                 return False

#     return len(stack) == 0


# # test cases
# cases = [
#     "()()",            # True
#     "(()",             # False
#     "((())())",        # True
#     "(()))",           # False
#     "(()(()))",        # True
#     "((())(()))",      # True
#     "())((())",        # False
#     "(((())))()(()())",  # True
#     "((())())(()",     # False
#     "())(())",         # False
# ]

# for value in cases:
#     print(value, "->", is_valid_parentheses(value))



def is_valid_parentheses(s):
    stack = []

    for ch in s:
        if ch == "(":
            stack.append(ch)
            print("stack: ",stack)
        elif ch == ")":
            print("stack: ",stack)
            if stack and stack[-1] == "(":
                stack.pop()
                print("stack: ",stack)
            else:
                return False

    return len(stack) == 0


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
