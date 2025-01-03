from collections import deque

def print_grid(grid):
    for row in grid:
        print(" ".join(row))

def read_input(file):
    lines = file.read().splitlines()
    grid = []
    isGrid = True
    moves = []
    for line in lines:
        if line == "":
            isGrid = False
        elif isGrid:
            grid.append(list(line))
        else:
            moves.append(list(line))
    return grid, moves

def extend_grid(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [["." for _ in range(2 * cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#":  # Obstacle
                new_grid[r][2 * c] = "#"
                new_grid[r][2 * c + 1] = "#"
            elif grid[r][c] == ".":  # Empty space
                new_grid[r][2 * c] = "."
                new_grid[r][2 * c + 1] = "."
            elif grid[r][c] == "@":  # Player
                new_grid[r][2 * c] = "@"
                new_grid[r][2 * c + 1] = "."
            elif grid[r][c] == "O":  # Object to move
                new_grid[r][2 * c] = "["
                new_grid[r][2 * c + 1] = "]"

    return new_grid

def check_availability(grid, next_r, next_c, direction):
    rows, cols = len(grid), len(grid[0])
    new_r, new_c = next_r, next_c

    if direction == (0,1) or direction == (0,-1):
        while 0 <= new_r < rows and 0 <= new_c < cols:
            if grid[new_r][new_c] == ".":
                grid[next_r - direction[0]][next_c - direction[1]] = "."
                while new_r != next_r or new_c != next_c:
                    grid[new_r][new_c] = grid[new_r - direction[0]][new_c - direction[1]]
                    new_r -= direction[0]
                    new_c -= direction[1]
                grid[new_r][new_c] = "@"
                return True
            elif grid[new_r][new_c] == "#":  # Obstacle encountered
                break
            new_r += direction[0]
            new_c += direction[1]
    else:
        q = deque([(next_r, next_c)])
        if grid[next_r][next_c] == "]":
            q.append((next_r, next_c - 1))
        else:
            q.append((next_r, next_c + 1))
        visited = set()
        ok = True
        while q:
            rr, cc = q.popleft()
            if (rr, cc) in visited:
                continue
            visited.add((rr, cc))
            rrr, ccc = rr + direction[0], cc + direction[1]
            if grid[rrr][ccc] == "#":
                ok = False
                break
            if grid[rrr][ccc] == "[":
                q.append((rrr,ccc))
                q.append((rrr, ccc + 1))
            if grid[rrr][ccc] == "]":
                q.append((rrr,ccc))
                q.append((rrr, ccc - 1))
        if not ok:
            return False
        while visited:
            for rr, cc in sorted(visited):
                rrr, ccc = rr + direction[0], cc + direction[1]
                if (rrr, ccc) not in visited:
                    grid[rrr][ccc] = grid[rr][cc]
                    grid[rr][cc] = "."
                    visited.remove((rr,cc))
        return True

    return False

def execute_moves(grid, sequence, start_pos):
    directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    rows, cols = len(grid), len(grid[0])
    for s in sequence:
        new_r = start_pos[0] + directions[s][0]
        new_c = start_pos[1] + directions[s][1]
        if new_r == 0 or new_r == rows - 1 or new_c == 0 or new_c == cols - 1 or grid[new_r][new_c] == "#":
            continue
        elif grid[new_r][new_c] == ".":
            grid[start_pos[0]][start_pos[1]] = "."
            grid[new_r][new_c] = "@"
            start_pos = [new_r, new_c]
        else: # next position is blocked by a "O" aka “[]"
            if not check_availability(grid, new_r, new_c, directions[s]):
                continue
            grid[start_pos[0]][start_pos[1]] = "."
            grid[new_r][new_c] = "@"
            start_pos = [new_r, new_c]

    return start_pos

def calculate_result(grid):
    rows, cols = len(grid), len(grid[0])
    result = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "[":
                result += (100 * r + c)
    return result

with open("./input.txt", "r") as fileToRead:
    
    grid, moves = read_input(fileToRead)

    grid = extend_grid(grid)
    rows, cols = len(grid), len(grid[0])

    start_pos = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                start_pos = [r,c]
                break
    
    for move_seq in moves:
        start_pos = execute_moves(grid, move_seq, start_pos)
    print(calculate_result(grid))