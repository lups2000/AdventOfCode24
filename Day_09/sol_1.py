
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

def move_blocks_to_left(my_list):
    start = 0
    end = len(my_list) - 1

    while start < end:
        if my_list[start] != ".":
            start += 1
        elif my_list[end] == ".":
            end -= 1
        else:
            my_list[start] = my_list[end]
            my_list[end] = "."

with open("./input.txt", "r") as fileToRead:

    line = fileToRead.readline().strip()
    
    list_to_process = helper(line)

    move_blocks_to_left(list_to_process)
    
    result = 0

    for i in range(len(list_to_process)):
        if list_to_process[i] == ".":
            break
        result += (i * int(list_to_process[i]))
    
    print(result)