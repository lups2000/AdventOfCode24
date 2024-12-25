
def print_grid(grid):
    for row in grid:
        print("".join(row))

def grid_to_pin(grid, locks, keys):
    rows, cols = len(grid), len(grid[0])
    my_map = {i: 0 for i in range(5)}
    for r in range(rows):
        for c in range(cols):
            if r != 0 and r != rows - 1 and grid[r][c] == "#":
                my_map[c] += 1
    if "".join(grid[0]) == "#####":
        locks.append(my_map.values())
    else:
        keys.append(my_map.values())

def analyse_combs(locks, keys):
    cnt = 0
    for l in locks:
        for k in keys:
            if all(a + b <= 5 for a, b in zip(l, k)):
                cnt += 1
    return cnt

with open("./input.txt", "r") as fileToRead:
    locks = []
    keys = []
    grid = []
    for line in fileToRead.read().split("\n"):
        if line == "":
            grid_to_pin(grid, locks, keys)
            grid = []
        else:
            grid.append(list(line))
    grid_to_pin(grid, locks, keys)
    print(analyse_combs(locks, keys))