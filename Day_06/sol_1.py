import sys
sys.setrecursionlimit(10**6)  # Increase the recursion limit

def find_start_position(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "^":
                return (r,c)
            
def dfs(grid, curr_r, curr_c, current_dir, visited) -> int:
    if curr_r < 0 or curr_c < 0 or curr_r >= len(grid) or curr_c >= len(grid[0]):
        return len(visited)
    
    visited.add((curr_r, curr_c))
    
    DIRECTIONS = {
        "UP": (-1, 0),
        "RIGHT": (0, 1),
        "DOWN": (1, 0),
        "LEFT": (0, -1),
    }
    TURN_RIGHT = {
        "UP": "RIGHT",
        "RIGHT": "DOWN",
        "DOWN": "LEFT",
        "LEFT": "UP",
    }

    dr, dc = DIRECTIONS[current_dir]
    next_r, next_c = curr_r + dr, curr_c + dc

    if (0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]) and grid[next_r][next_c] == "#"):
        current_dir = TURN_RIGHT[current_dir]
    else:
        curr_r, curr_c = next_r, next_c

    return dfs(grid, curr_r, curr_c, current_dir, visited)


with open("./input.txt", "r") as fileToRead:
    
    grid = []
    for line in fileToRead.readlines():
        line = line.strip()
        grid.append(list(line))

    start_r, start_c = find_start_position(grid)
    current_dir = "UP"
    
    print(dfs(grid, start_r, start_c, current_dir ,set()))