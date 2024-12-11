from functools import lru_cache

@lru_cache(None)
def recursive_helper(curr, blinks=0, limit=75) -> int:
    if blinks == limit:
        return 1
    
    if curr == "0":
        return recursive_helper("1", blinks + 1, limit)
    elif len(curr) % 2 == 0:
        mid = len(curr) // 2
        return recursive_helper(str(int(curr[:mid])), blinks + 1, limit) + recursive_helper(str(int(curr[mid:])) , blinks + 1, limit)
    else:
        return recursive_helper(str(int(curr) * 2024), blinks + 1, limit)


with open("./input.txt") as fileToRead:
    line = fileToRead.readline().strip()

    list_to_process = line.split(" ")

    res = 0
    
    for el in list_to_process:
        res += recursive_helper(el)
    print(res)