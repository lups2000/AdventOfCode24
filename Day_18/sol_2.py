from collections import deque

def print_grid(grid):
    for row in grid:
        print(" ".join(row))

def simulate_bytes_fall(grid, bytes):
    for x, y in bytes:
        grid[y][x] = "#"
    return grid

def bfs(grid):
    rows, cols = len(grid), len(grid[0])
    q = deque([(0, 0)])
    visited = set()
    visited.add((0, 0))
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
    return None

def binary_search(bytes, start, end):
    grid = [["."] * 71 for _ in range(71)]
    last_simulated_index = -1  # Track how many bytes have been simulated

    while start <= end:
        mid = (start + end) // 2

        if mid > last_simulated_index:
            simulate_bytes_fall(grid, bytes[last_simulated_index + 1:mid + 1])
        elif mid < last_simulated_index:
            grid = [["."] * 71 for _ in range(71)] # reset grid
            simulate_bytes_fall(grid, bytes[:mid + 1])

        last_simulated_index = mid

        if bfs(grid):
            start = mid + 1
        else:
            end = mid - 1

    return start


with open("./input.txt", "r") as fileToRead:
    bytes = []
    grid = [["."] * 71 for _ in range(71)]
    for line in fileToRead.readlines():
        line = [int(el) for el in line.strip().split(",")]
        bytes.append(line)


    bad_index = binary_search(bytes ,1024, len(bytes) - 1)
    print(bytes[bad_index])