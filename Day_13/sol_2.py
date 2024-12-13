def helper(a1, a2, b1, b2, p1, p2):
    num_X2 = p2 - (a2 / a1 * p1)
    den_X2 = b2 - (b1 * a2 / a1)
    X2 = num_X2 / den_X2

    X1 = (p1 - b1 * X2) / a1

    temp_X1 = round(X1)
    temp_X2 = round(X2)
    
    if (temp_X1 * a1 + temp_X2 * b1 == p1 and 
        temp_X1 * a2 + temp_X2 * b2 == p2):
        return int(temp_X1), int(temp_X2)
    else:
        return None, None

def check_result(num_button_A, num_button_B):
    if not num_button_A or not num_B:
        return False
    return num_button_A >= 0 and num_button_B >= 0

with open("./input.txt", "r") as fileToRead:
    result = 0
    a1 = a2 = b1 = b2 = p1 = p2 = 0
    offset = 10000000000000

    for line in fileToRead.readlines():
        line = line.strip()
        
        if line.startswith("Button A"):
            coordinates_A = line[12:].split(", Y+")
            a1, a2 = map(int, coordinates_A)
        elif line.startswith("Button B"):
            coordinates_B = line[12:].split(", Y+")
            b1, b2 = map(int, coordinates_B)
        elif line.startswith("Prize"):
            coordinates_Prize = line[9:].split(", Y=")
            p1, p2 = map(int, coordinates_Prize)
            p1 = p1 + offset
            p2 = p2 + offset
        else:
            if a1 and a2 and b1 and b2 and p1 and p2:
                num_A, num_B = helper(a1, a2, b1, b2, p1, p2)
                if check_result(num_A, num_B):
                    result += (3 * num_A + num_B)
    
    if a1 and a2 and b1 and b2 and p1 and p2:
        num_A, num_B = helper(a1, a2, b1, b2, p1, p2)
        if check_result(num_A, num_B):
            result += (3 * num_A + num_B)

    print(result)
