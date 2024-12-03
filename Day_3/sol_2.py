import re

with open("./input.txt", "r") as fileToRead:
    content = fileToRead.read().strip()

    pattern = r"mul\((-?\d+),(-?\d+)\)"
    matches = re.finditer(pattern, content, re.DOTALL)

    matches_intervals = [m for m in matches]
    
    disable_pattern = r"don't\(\).*?do\(\)"
    matches_disable = re.finditer(disable_pattern, content, re.DOTALL)
    disable_intervals = [m.span() for m in matches_disable]

    result = 0
    for i in range(len(matches_intervals)):
        curr_span = matches_intervals[i].span()
        for j in range(len(disable_intervals)):
            curr_disable_span = disable_intervals[j]
            # Check for overlap
            if not (curr_disable_span[1] <= curr_span[0] or curr_disable_span[0] >= curr_span[1]):
                # Skip if there's an overlap
                break
        else:
            a, b = matches_intervals[i].groups()
            result += int(a) * int(b)

    print(result)
