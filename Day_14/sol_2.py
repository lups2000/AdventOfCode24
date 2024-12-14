def print_grid(grid):
    for row in grid:
        for cell in row:
            if cell == 0:
                print(".", end=" ")
            else:
                print("X", end=" ")
        print()

def write_grid_to_file(grid, file, timestamp):
    file.write(f"Time: {timestamp} seconds\n")
    for row in grid:
        for cell in row:
            file.write(". " if cell == 0 else "X ")
        file.write("\n")
    file.write("\n")

def simulate_movements_all(grid, positions, speeds, filename):
    rows, cols = len(grid), len(grid[0])
    seconds = 10000

    with open(filename, "w") as file:
        for t in range(seconds):
            new_positions = []
            grid = [[0 for _ in range(cols)] for _ in range(rows)]
            for (pos_x, pos_y), (speed_x, speed_y) in zip(positions, speeds):
                pos_x = (pos_x + speed_x) % cols
                pos_y = (pos_y + speed_y) % rows
                grid[pos_y][pos_x] += 1
                new_positions.append((pos_x, pos_y))

            positions = new_positions        
            write_grid_to_file(grid, file, t)

    return grid

with open("./input.txt", "r") as fileToRead:
    rows = 103
    cols = 101
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    output_filename = "robot_simulation.txt"

    positions = []
    speeds = []

    for line in fileToRead.readlines():
        line = line.strip()
        position, speed = line.split(" ")
        pos_x, pos_y = map(int, position[2:].split(","))
        speed_x, speed_y = map(int, speed[2:].split(","))

        positions.append((pos_x, pos_y))
        speeds.append((speed_x, speed_y))

    simulate_movements_all(grid, positions, speeds, output_filename)
    # answer found visually :)