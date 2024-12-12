from collections import deque

def topological_sort(my_list):
        sub_graph = {el: [] for el in my_list}
        in_degree = {el: 0 for el in my_list}

        for x in my_list:
            if x in my_graph:
                for y in my_graph[x]:
                    if y in sub_graph:
                        sub_graph[x].append(y)
                        in_degree[y] += 1

        queue = deque([el for el in my_list if in_degree[el] == 0])
        sorted_order = []

        while queue:
            popped = queue.popleft()
            sorted_order.append(popped)
            for neighbor in sub_graph[popped]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted_order

with open("./input.txt", "r") as fileToRead:
    my_graph = {}
    result = 0
    incorrect_lists = []
    for line in fileToRead.readlines():
        line = line.strip()
        if "|" in line:
            x, y = line.split("|")
            if x not in my_graph:
                my_graph[x] = []
            if y not in my_graph:
                my_graph[y] = []
            my_graph[x].append(y)
        elif line != "":
            list_to_process = line.split(",")
            isGood = True
            for i in range(1, len(list_to_process)):
                curr = list_to_process[i]
                prev = list_to_process[i-1]

                if curr not in my_graph[prev] or prev not in my_graph:
                    isGood = False
                    break

            if not isGood:
                incorrect_lists.append(list_to_process)
    
    for l in incorrect_lists:
        sorted_update = topological_sort(l)
        result += int(sorted_update[len(sorted_update) // 2])

    print(result)
                

    
    
              
