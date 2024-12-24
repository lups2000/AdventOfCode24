from collections import deque

def perform_operation(my_map, wire1, wire2, operation, output):
    if operation == "AND":
        my_map[output] = my_map[wire1] & my_map[wire2]
    elif operation == "OR":
        my_map[output] = my_map[wire1] | my_map[wire2]
    else:
        my_map[output] = my_map[wire1] ^ my_map[wire2]

def extract_z_bits(my_map):
    res = 0
    cnt = 0
    for k, v in sorted(my_map.items()):
        if k.startswith("z"):
            res += (2 ** cnt) * v
            cnt += 1
    return res

with open("./input.txt", "r") as fileToRead:
    my_map = {}
    q = deque()

    for el in fileToRead.read().split("\n"):
        if el == "": continue
        if "->" not in el:
            wire, state = el.split(": ")
            my_map[wire] = int(state)
        else:
            first_part, second_part = el.split(" -> ")
            wire1, operation, wire2 = first_part.split(" ")
            q.append((wire1, wire2, operation, second_part))
    
    while q:
        wire1, wire2, operation, output = q.popleft()

        if wire1 not in my_map or wire2 not in my_map:
            q.append((wire1, wire2, operation, output))
        else:
            perform_operation(my_map, wire1, wire2, operation, output)

    print(extract_z_bits(my_map))
