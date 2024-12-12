from collections import deque


def bfs(grid, r, c, visited):
    rows, cols = len(grid), len(grid[0])
    q = deque([(r,c)])
    curr = grid[r][c]
    area = 1
    perimeter = 4
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    while q:
        pop_r, pop_c = q.popleft()

        for dr, dc in directions:
            new_r, new_c = pop_r + dr, pop_c + dc
            if min(new_r, new_c) < 0 or new_r >= rows or new_c >= cols or (new_r, new_c) in visited or grid[new_r][new_c] != curr:
                continue
                
            area += 1
            perimeter += 4

            if new_r > 0 and grid[new_r-1][new_c] == curr:
                perimeter -= 2            
            if new_c > 0 and grid[new_r][new_c-1] == curr:
                perimeter -= 2

            visited.add((new_r, new_c))
            q.append((new_r, new_c))

    return area * perimeter

with open("./input.txt", "r") as fileToRead:
    grid = []
    for line in fileToRead.readlines():
        line = line.strip()
        grid.append(list(line))

    rows, cols = len(grid), len(grid[0])

    visited = set()
    result = 0
    for r in range(rows):
        for c in range(cols):
            if (r,c) not in visited:
                visited.add((r,c))
                result += bfs(grid, r, c, visited)
    
    print(result)