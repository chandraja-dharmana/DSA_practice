# A ---- B
# |      |
# C ---- D
# there is no difference between ------ and ______ 
# undirected

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

#starting from 'A'

target = "D"
target = "F"


visited = set()

def dfs(node):
    if node == target:
        return True

    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(neighbor):
                return True

    return False


if dfs("A"):
    print("Found")
else:
    print("Not Found")