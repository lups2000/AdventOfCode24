def searchXMAS(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if matrix[r][c] == "A":
                if (
                    (
                        r - 1 >= 0 and c - 1 >= 0 and matrix[r - 1][c - 1] == "M" and
                        r + 1 < rows and c + 1 < cols and matrix[r + 1][c + 1] == "S" and
                        r - 1 >= 0 and c + 1 < cols and matrix[r - 1][c + 1] == "S" and
                        r + 1 < rows and c - 1 >= 0 and matrix[r + 1][c - 1] == "M"
                    ) or 
                    (
                        r - 1 >= 0 and c - 1 >= 0 and matrix[r - 1][c - 1] == "S" and
                        r + 1 < rows and c + 1 < cols and matrix[r + 1][c + 1] == "M" and
                        r - 1 >= 0 and c + 1 < cols and matrix[r - 1][c + 1] == "M" and
                        r + 1 < rows and c - 1 >= 0 and matrix[r + 1][c - 1] == "S"
                    ) or
                    (
                        r - 1 >= 0 and c - 1 >= 0 and matrix[r - 1][c - 1] == "M" and
                        r + 1 < rows and c + 1 < cols and matrix[r + 1][c + 1] == "S" and
                        r - 1 >= 0 and c + 1 < cols and matrix[r - 1][c + 1] == "M" and
                        r + 1 < rows and c - 1 >= 0 and matrix[r + 1][c - 1] == "S"
                    ) or
                    (
                        r - 1 >= 0 and c - 1 >= 0 and matrix[r - 1][c - 1] == "S" and
                        r + 1 < rows and c + 1 < cols and matrix[r + 1][c + 1] == "M" and
                        r - 1 >= 0 and c + 1 < cols and matrix[r - 1][c + 1] == "S" and
                        r + 1 < rows and c - 1 >= 0 and matrix[r + 1][c - 1] == "M"
                    )
                ):
                    count += 1

    return count


with open("./input.txt", "r") as fileToRead:
    matrix = [list(line.strip()) for line in fileToRead]

    result = searchXMAS(matrix)
    print(result)
