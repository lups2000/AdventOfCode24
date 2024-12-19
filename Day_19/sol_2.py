def calculate_res(patterns, designs):
    
    def count_form_design(design, cache):
        if design in cache:
            return cache[design]
        if design == "":
            return 1
        cnt = 0
        for p in patterns:
            if design.startswith(p):
                cnt += count_form_design(design[len(p):], cache)
        cache[design] = cnt
        return cache[design]
    
    cnt = 0
    for d in designs:
        cnt += count_form_design(d, {})
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