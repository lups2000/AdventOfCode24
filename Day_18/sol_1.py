from collections import deque

def print_grid(grid):
    for row in grid:
        print(" ".join(row))

def simulate_bytes_fall(grid, bytes):
    for x, y in bytes:
        grid[y][x] = "#"
    return grid

def bfs(grid, start_r, start_c):
    rows, cols = len(grid), len(grid[0])
    q = deque([(start_r, start_c)])
    visited = set()
    visited.add((start_r, start_c))
    directions = [(1,0),(0,-1),(-1,0),(0,1)]
    length = 0
    while q:
        for _ in range(len(q)):
            pr, pc = q.popleft()
            
            for dr, dc in directions:
                nr, nc = pr + dr, pc + dc
                if min(nr, nc) < 0 or nr >= rows or nc >= cols or grid[nr][nc] == "#" or (nr, nc) in visited:
                    continue
                if nr == rows - 1 and nc == cols - 1:
                    return 1 + length
                
                visited.add((nr, nc))
                q.append((nr, nc))
        
        length += 1


with open("./input.txt", "r") as fileToRead:
    bytes = []
    grid = [["."] * 71 for _ in range(71)]
    for line in fileToRead.readlines():
        line = [int(el) for el in line.strip().split(",")]
        bytes.append(line)

    grid = simulate_bytes_fall(grid, bytes[:1025])
    print_grid(grid)
    print(bfs(grid, 0, 0))