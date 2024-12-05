with open("./input.txt", "r") as fileToRead:
    my_graph = {}
    result = 0
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

            if isGood:
                result += int(list_to_process[len(list_to_process) // 2])
    
    print(result)
              
