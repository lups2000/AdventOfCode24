import re

with open("./input.txt", "r") as fileToRead:
    pattern = r"mul\((-?\d+),(-?\d+)\)"
    content = fileToRead.read().strip()
    matches = re.findall(pattern, content)
    
    result = 0
    for a,b in matches:
        result += (int(a) * int(b))
    
    print(result)
    