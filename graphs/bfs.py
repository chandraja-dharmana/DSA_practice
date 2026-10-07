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
#target = "F"


visited = set()
queue = ["A"]

visited.add("A")

while queue:
    node = queue.pop(0)

    if node == target:
        print("Found")
        break

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
else:
    print("Not Found")


# ### same thing above with print statements
# graph = {
#     "A": ["B", "C"],
#     "B": ["A", "D"],
#     "C": ["A", "D"],
#     "D": ["B", "C"]
# }

# #starting from 'A'

# target = "D"
# #target = "F"


# visited = set()
# queue = ["A"]

# visited.add("A")

# while queue:
#     node = queue.pop(0)
#     print("node:",node)

#     if node == target:
#         print("Found")
#         break

#     print("graph[node]:", graph[node])
#     for neighbor in graph[node]:
#         print("neighbour:", neighbor)
#         if neighbor not in visited:
#             visited.add(neighbor)
#             print("visited:", visited)
#             queue.append(neighbor)
#             print("queue:", queue)
# else:
#     print("Not Found")