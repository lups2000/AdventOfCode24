def searchWord(matrix, r, c, wordToSearch):
    # Possible directions: 8 surrounding cells
    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
    
    count = 0

    for dr, dc in directions:
        path = []
        nr, nc = r, c
        valid_path = True
        
        for letter in wordToSearch:

            if (0 <= nr < len(matrix) and 
                0 <= nc < len(matrix[0]) and 
                matrix[nr][nc] == letter):
                path.append((nr, nc))
                nr += dr
                nc += dc
            else:
                valid_path = False
                break
        
        if valid_path and len(path) == len(wordToSearch):
            count += 1
    
    return count



with open("input.txt", "r") as fileToRead:
    matrix = []
    for line in fileToRead.readlines():
        line = list(line.strip())
        matrix.append(line)
    
    wordToSearch = "XMAS"

    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == wordToSearch[0]: 
                res += searchWord(matrix, i, j, wordToSearch)
    
    print(res)