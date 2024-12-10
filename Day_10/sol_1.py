
def find_zeros(grid) -> list:
    zero_positions = []
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                zero_positions.append((r,c))
    
    return zero_positions

def dfs(grid, row, col, curr_number ,visited, nine_visited):
    rows, cols = len(grid), len(grid[0])

    if min(row, col) < 0 or row >= rows or col >= cols or (row, col) in visited or grid[row][col] != curr_number or (row, col) in nine_visited:
        return 0
    
    if grid[row][col] == 9:
        nine_visited.add((row, col))
        return 1
    
    visited.add((row, col))

    count = 0
    count += dfs(grid, row + 1, col, curr_number + 1, visited, nine_visited)
    count += dfs(grid, row - 1, col, curr_number + 1, visited, nine_visited)
    count += dfs(grid, row, col + 1, curr_number + 1, visited, nine_visited)
    count += dfs(grid, row, col - 1, curr_number + 1, visited, nine_visited)

    visited.remove((row, col))

    return count


with open("./input.txt", "r") as fileToRead:
    grid = []
    for line in fileToRead.readlines():
        grid.append([int(c) for c in list(line.strip())])
    
    zero_positions = find_zeros(grid)
    
    result = 0
    for r, c in zero_positions:
        result += dfs(grid, r, c, 0, set(), set())
    
    print(result)

    