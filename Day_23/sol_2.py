
def bron_kerbosch(graph, r, p, x, cliques):
    if not p and not x:
        cliques.append(r)
        return
    for node in list(p):
        bron_kerbosch(
            graph,
            r | {node},
            p & set(graph[node]),
            x & set(graph[node]),
            cliques
        )
        p.remove(node)
        x.add(node)

def find_largest_clique(graph):
    cliques = []
    bron_kerbosch(graph, set(), set(graph.keys()), set(), cliques)
    largest_clique = max(cliques, key=len)
    return largest_clique

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

    largest_clique = find_largest_clique(my_graph)
    password = ",".join(sorted(largest_clique))
    print(password)
