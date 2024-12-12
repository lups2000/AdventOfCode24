def is_safe_sequence(report, allow_skip=False):
    is_ascending = None
    skipped = False
    
    for i in range(1, len(report)):
        prev, curr = report[i-1], report[i]
        prev_prev = report[i-2] if i > 1 else None
        
        if is_ascending is None:
            is_ascending = prev < curr
        
        # Check if the difference between adjacent levels is within 1-3
        if not (1 <= abs(prev - curr) <= 3 and 
                ((prev < curr and is_ascending) or (prev > curr and not is_ascending))):
            
            if not allow_skip or skipped:
                return False
            
            skip_prev = (prev_prev is not None and 
                         1 <= abs(prev_prev - curr) <= 3 and 
                         ((prev_prev < curr and is_ascending) or 
                          (prev_prev > curr and not is_ascending)))
            
            skip_curr = (i+1 < len(report) and 
                         1 <= abs(prev - report[i+1]) <= 3 and 
                         ((prev < report[i+1] and is_ascending) or 
                          (prev > report[i+1] and not is_ascending)))
            
            if skip_prev or skip_curr:
                skipped = True
                continue
            else:
                return False
    
    return True


with open("./input.txt", "r") as fileToRead:
    safe_reports = 0
    for line in fileToRead:
        report = list(map(int, line.strip().split()))
        
        if is_safe_sequence(report):
            safe_reports += 1
        # If not safe, check if removing a single level makes it safe
        else:
            for j in range(len(report)):
                # Create a new report by removing one level
                modified_report = report[:j] + report[j+1:]
                if is_safe_sequence(modified_report):
                    safe_reports += 1
                    break
    
    print(safe_reports)