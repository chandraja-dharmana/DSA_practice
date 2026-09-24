path = []
n = 2
result = []

def bt_dfs(path):
    # Q1: complete answer?
    if len(path) == n:
        result.append("".join(path))
        return

    # Q2: what choices do I have?
    for char in ["a", "b"]:
        path.append(char)      # make the choice
        bt_dfs(path)           # explore deeper
        path.pop()             # undo the choice

bt_dfs(path)

print(path)
print(result)
