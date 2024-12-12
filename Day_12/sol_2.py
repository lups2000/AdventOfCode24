from enum import Enum
from typing import List, Set
from collections import deque

class Direction(Enum):
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)

    def ccw(self):
        #counter-clockwise
        rotations = [Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.EAST]
        return rotations[(rotations.index(self) - 1) % 4]

    def cw(self):
        #clockwise
        rotations = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
        return rotations[(rotations.index(self) - 1) % 4]

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def go(self, direction: Direction):
        return Point(self.x + direction.value[0], self.y + direction.value[1])

    def adjacents(self, diagonal: bool = True):
        adjacent_dirs = list(Direction) if diagonal else [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
        return [self.go(d) for d in adjacent_dirs]

class Grid:
    def __init__(self, grid_data: List[List[str]]):
        self.grid = grid_data
        self.height = len(grid_data)
        self.width = len(grid_data[0]) if self.height > 0 else 0

    def __contains__(self, point: Point):
        return (0 <= point.x < self.width and 0 <= point.y < self.height)

    def __getitem__(self, point: Point):
        return self.grid[point.y][point.x]

def total_fence_price(grid: Grid) -> int:
    score = 0
    seen: Set[Point] = set()

    for y in range(grid.height):
        for x in range(grid.width):
            p = Point(x, y)
            if p not in seen:
                queue = deque([p])
                region_points: Set[Point] = set()
                area = 0
                num_sides = 0

                while queue:
                    q = queue.popleft()
                    
                    if q not in grid or grid[q] != grid[p] or q in region_points:
                        continue

                    area += 1

                    for dir in Direction:
                        forward = q.go(dir)
                        left = q.go(dir.ccw())
                        right = q.go(dir.cw())

                        if forward in region_points:
                            num_sides -= 1
                            for side in [left, right]:
                                if side not in region_points and side.go(dir) in region_points:
                                    num_sides += 1
                        else:
                            num_sides += 1
                            for side in [left, right]:
                                if side in region_points and side.go(dir) not in region_points:
                                    num_sides -= 1

                    region_points.add(q)
                    queue.extend(adj for adj in q.adjacents(False) if adj not in region_points)

                seen.update(region_points)
                score += area * num_sides

    return score

with open("./input.txt", "r") as fileToRead:
    grid = []
    for line in fileToRead.readlines():
        line = line.strip()
        grid.append(list(line))

    grid = Grid(grid)
    print(total_fence_price(grid))