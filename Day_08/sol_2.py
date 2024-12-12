def check_in_bound(rows, cols, new_r, new_c):
    if min(new_r, new_c) < 0 or new_r >= rows or new_c >= cols:
        return False
    return True

def place_antinodes(frequencies, grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    for i in range(len(frequencies)):
        for j in range(i+1, len(frequencies)):
            if frequencies[i][0] == frequencies[j][0]: # same frequency
                r1, c1 = frequencies[i][1], frequencies[i][2]
                r2, c2 = frequencies[j][1], frequencies[j][2]

                visited.add((r1,c1))
                visited.add((r2,c2))

                x_dist = abs(r1 - r2)
                y_dist = abs(c1 - c2)

                if r1 >= r2 and c1 >= c2:
                    while check_in_bound(rows, cols, r1 + x_dist, c1 + y_dist):
                        visited.add((r1 + x_dist, c1 + y_dist))
                        r1 = r1 + x_dist
                        c1 = c1 + y_dist
                    while check_in_bound(rows, cols, r2 - x_dist, c2 - y_dist):
                        visited.add((r2 - x_dist, c2 - y_dist))
                        r2 = r2 - x_dist
                        c2 = c2 - y_dist
                elif r1 < r2 and c1 < c2:
                    while check_in_bound(rows, cols, r1 - x_dist, c1 - y_dist):
                        visited.add((r1 - x_dist, c1 - y_dist))
                        r1 = r1 - x_dist
                        c1 = c1 - y_dist
                    while check_in_bound(rows, cols, r2 + x_dist, c2 + y_dist):
                        visited.add((r2 + x_dist, c2 + y_dist))
                        r2 = r2 + x_dist
                        c2 = c2 + y_dist
                elif r1 >= r2 and c1 < c2:
                    while check_in_bound(rows, cols, r1 + x_dist, c1 - y_dist):
                        visited.add((r1 + x_dist, c1 - y_dist))
                        r1 = r1 + x_dist
                        c1 = c1 - y_dist
                    while check_in_bound(rows, cols, r2 - x_dist, c2 + y_dist):
                        visited.add((r2 - x_dist, c2 + y_dist))
                        r2 = r2 - x_dist
                        c2 = c2 + y_dist
                else:
                    while check_in_bound(rows, cols, r1 - x_dist, c1 + y_dist):
                        visited.add((r1 - x_dist, c1 + y_dist))
                        r1 = r1 - x_dist
                        c1 = c1 + y_dist
                    while check_in_bound(rows, cols, r2 + x_dist, c2 - y_dist):
                        visited.add((r2 + x_dist, c2 - y_dist))
                        r2 = r2 + x_dist
                        c2 = c2 - y_dist
    return len(visited)

with open("./input.txt", "r") as fileToRead:

    grid = []
    for line in fileToRead.readlines():
        line = line.strip()
        grid.append(list(line))
    
    rows = len(grid)
    cols = len(grid[0])
    frequencies = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != ".":
                frequencies.append((grid[r][c], r, c))

    print(place_antinodes(frequencies, grid))

                
