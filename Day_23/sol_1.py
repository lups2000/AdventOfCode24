def find_triangles(graph):
    triangles = set()
    for node in graph:
        for neighbor1 in graph[node]:
            for neighbor2 in graph[neighbor1]:
                if neighbor2 in graph[node] and node != neighbor1 and node != neighbor2 and neighbor1 != neighbor2:
                    triangles.add(frozenset([node, neighbor1, neighbor2]))
    return triangles

def count_triangles_with_t(triangles):
    count = 0
    for triangle in triangles:
        if any(node.startswith("t") for node in triangle):
            count += 1
    return count

with open("./input.txt", "r") as fileToRead:
    my_graph = {}
    for line in fileToRead.readlines():
        line = line.strip()
        first, second = line.split("-")
        if first not in my_graph:
            my_graph[first] = []
        if second not in my_graph:
            my_graph[second] = []
        my_graph[first].append(second)
        my_graph[second].append(first)

    triangles = find_triangles(my_graph)
    result = count_triangles_with_t(triangles)
    print(result)