def calculate_res(patterns, designs):
    
    def can_form_design(design, cache):
        if design in cache:
            return cache[design]
        if design == "":
            return True
        for p in patterns:
            if design.startswith(p):
                if can_form_design(design[len(p):], cache):
                    cache[design] = True
                    return True
        cache[design] = False
        return False
    
    cnt = 0
    for d in designs:
        if can_form_design(d, {}):
            cnt += 1
    return cnt


with open("./input.txt", "r") as fileToRead:
    patterns = []
    designs = []
    my_input = fileToRead.read().split("\n")

    for p in my_input[0].split(", "):
        patterns.append(p)
    
    for d in my_input[2:]:
        designs.append(d)

    print(calculate_res(patterns, designs))