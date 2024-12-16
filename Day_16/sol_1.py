from heapq import heappush, heappop

directions = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1)
}
clockwise = {"N": "E", "E": "S", "S": "W", "W": "N"}
anti_clockwise = {"N": "W", "W": "S", "S": "E", "E": "N"}

def dijkstra(grid, start, curr_dir):
    rows, cols = len(grid), len(grid[0])
    min_heap = [(0, start[0], start[1], curr_dir)]  # (cost, row, col, direction)
    visited = set()

    while min_heap:
        current_cost, r, c, dir = heappop(min_heap)

        if (r, c, dir) in visited:
            continue

        if grid[r][c] == "E":
            return current_cost

        visited.add((r, c, dir))    

        # moving straight
        dr, dc = directions[dir]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
            heappush(min_heap, (current_cost + 1, nr, nc, dir))

        # turning clockwise
        new_dir = clockwise[dir]
        dr, dc = directions[new_dir]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
            heappush(min_heap, (current_cost + 1001, nr, nc, new_dir))

        # turning anti-clockwise
        new_dir = anti_clockwise[dir]
        dr, dc = directions[new_dir]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
            heappush(min_heap, (current_cost + 1001, nr, nc, new_dir))

    return -1

with open("./input.txt") as file:
    grid = [list(line.strip()) for line in file]
    rows, cols = len(grid), len(grid[0])
    start = None
    initial_dir = "E"

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                start = (r, c)
                break

    print(dijkstra(grid, start, initial_dir))
