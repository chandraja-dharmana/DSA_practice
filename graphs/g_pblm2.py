#Count Nodes: Given a graph A-B-C, start from A and count how many nodes are reachable.

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


start_point='A'
visited = set()
visited.add(start_point) #This makes sure A itself counts as 1

def dfs(node):

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            dfs(neighbor)

print("starting point: ",start_point)
dfs(start_point)
print("number of nodes:", len(visited))



# ##same as above with print statements

# graph = {
#     "A": ["B", "C"],
#     "B": ["A", "D"],
#     "C": ["A", "D"],
#     "D": ["B", "C"]
# }


# start_point='A'
# visited = set()
# visited.add(start_point)

# def dfs(node):
#     print("visited: ", visited)

#     for neighbor in graph[node]:
#         print("neighbour: ", neighbor)
#         if neighbor not in visited:
#             visited.add(neighbor)
#             print("visited: ", visited)
#             if dfs(neighbor):
#                 return True

#     return False

# ret = dfs(start_point)
# print(ret)
# print("visited: ", visited)
# print("number of nodes:", len(visited))
