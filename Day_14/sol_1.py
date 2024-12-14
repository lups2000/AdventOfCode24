
def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def simulate_movements(grid, pos_x, pos_y, speed_x, speed_y):
    rows, cols = len(grid), len(grid[0])
    seconds = 100
    for _ in range(seconds):
        grid[pos_y][pos_x] -= 1
        pos_x = (pos_x + speed_x) % cols
        pos_y = (pos_y + speed_y) % rows
        grid[pos_y][pos_x] += 1

def calculate_scores(grid):
    rows, cols = len(grid), len(grid[0])
    mid_rows = rows // 2
    mid_cols = cols // 2
    first_quadrant = 0
    second_quadrant = 0
    third_quadrant = 0
    fourth_quadrant = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                if r < mid_rows and c < mid_cols:
                    first_quadrant += grid[r][c]
                elif r < mid_rows and c > mid_cols:
                    second_quadrant += grid[r][c]
                elif r > mid_rows and c > mid_cols:
                    third_quadrant += grid[r][c]
                elif r > mid_rows and c < mid_cols:
                    fourth_quadrant += grid[r][c]
    
    return first_quadrant * second_quadrant * third_quadrant * fourth_quadrant


with open("./input.txt", "r") as fileToRead:
    rows = 103
    cols = 101
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for line in fileToRead.readlines():
        line = line.strip()
        position, speed = line.split(" ")
        pos_x, pos_y = map(int, position[2:].split(","))
        speed_x, speed_y = map(int,speed[2:].split(","))

        grid[pos_y][pos_x] += 1
        simulate_movements(grid, pos_x, pos_y, speed_x, speed_y)
    
    print_grid(grid)
    print(calculate_scores(grid))