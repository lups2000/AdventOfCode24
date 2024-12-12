import heapq

def helper(s) -> list:
    my_list = []

    isFree = False
    id = 0
    for i in range(len(s)):
        if isFree:
            for _ in range(int(s[i])):
                my_list.append(".")
            isFree = False
        else:
            for _ in range(int(s[i])):
                my_list.append(str(id))
            id += 1
            isFree = True
    return my_list

def calculate_free_spaces(my_list) -> list:
    free_spaces = []
    start = None
    length = 0
    for i in range(len(my_list)):
        if my_list[i] == ".":
            if not start:
                start = i
            length += 1
        else:
            if not start:
                continue
            free_spaces.append([start, length])
            start = None
            length = 0
    return free_spaces

def move_blocks_to_left(my_list):
    
    free_spaces = calculate_free_spaces(my_list)
    
    end = len(my_list) - 2
    curr = my_list[-1]
    size = 1
    while end >= 0:
        if my_list[end] == curr:
            size += 1
        else:
            if curr != ".":
                for i in range(len(free_spaces)):
                    if end <= free_spaces[i][0]:
                        break
                    if free_spaces[i][1] >= size:
                        for j in range(free_spaces[i][0], free_spaces[i][0] + size):
                            my_list[j] = curr
                        if free_spaces[i][1] - size > 0:
                            free_spaces[i] = [free_spaces[i][0] + size, free_spaces[i][1] - size]
                        else:
                            del free_spaces[i]
                        for j in range(end + 1, end + 1 + size):
                            my_list[j] = "."
                        break
            size = 1
            curr = my_list[end]

        end -= 1

with open("./input.txt", "r") as fileToRead:

    line = fileToRead.readline().strip()
    
    list_to_process = helper(line)
    move_blocks_to_left(list_to_process)
    
    result = 0

    for i in range(len(list_to_process)):
        if list_to_process[i] == ".":
            continue
        result += (i * int(list_to_process[i]))
    
    print(result)
    