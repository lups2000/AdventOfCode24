
def helper(my_list):
    support = []
    for i in range(len(my_list)):
        if my_list[i] == "0":
            support.append("1")
        elif len(my_list[i]) % 2 == 0:
            mid = len(my_list[i]) // 2
            first, second = int(my_list[i][:mid]), int(my_list[i][mid:])
            support.append(str(first))
            support.append(str(second))
        else:
            support.append(str(int(my_list[i]) * 2024))

    return support 


with open("./input.txt") as fileToRead:
    line = fileToRead.readline().strip()

    list_to_process = line.split(" ")
    
    for i in range(25):
        list_to_process = helper(list_to_process)
    
    print(len(list_to_process))