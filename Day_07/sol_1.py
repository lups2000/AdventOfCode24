operations = ("+", "*")

def helper(curr_res, target, list_to_process):

    if curr_res > target:
        return False

    if curr_res == target and not list_to_process:
        return True
    
    if not list_to_process:
        return False
    
    first = int(list_to_process[0])

    for op in operations:
        if op == "+":
            if helper(curr_res + first, target, list_to_process[1:]):
                return True
        elif op == "*":
            if helper(curr_res * first, target, list_to_process[1:]):
                return True
    
    return False
    


with open("./input.txt", "r") as fileToRead:

    total = 0

    for line in fileToRead.readlines():
        line = line.strip()
        result, list_to_process = line.split(": ")
        result = int(result)
        list_to_process = list_to_process.split(" ")
        
        initial_value = int(list_to_process[0])
        list_to_process = list_to_process[1:]
        
        if helper(initial_value, result, list_to_process):
            total += result
    
    print(total)


