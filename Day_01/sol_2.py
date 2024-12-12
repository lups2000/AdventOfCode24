
with open("./input.txt", "r") as fileToRead:
    list1 = []
    freqs_2 = {}
    for line in fileToRead.readlines():
        line = line.strip()
        a, b = line.split("   ")
        list1.append(a)
        if b not in freqs_2:
            freqs_2[b] = 1
        else:
            freqs_2[b] += 1
    
    similarity_score = 0

    for el in list1:
        if el in freqs_2:
            similarity_score += (int(el) * freqs_2[el])

    print(similarity_score)
        

    
    
    