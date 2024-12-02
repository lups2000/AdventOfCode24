with open("./input.txt", "r") as fileToRead:
    safe_reports = 0

    for line in fileToRead:
        report = list(map(int, line.strip().split(" ")))
        is_ascending = None
        found = True

        for i in range(1, len(report)):
            prev, curr = report[i-1], report[i]
            
            if is_ascending is None:
                is_ascending = prev < curr
            
            if not (1 <= abs(prev - curr) <= 3 and ((prev < curr and is_ascending) or (prev > curr and not is_ascending))):
                found = False
                break

        if found:
            safe_reports += 1

    print(safe_reports)
