from heapq import heapify, heappop

with open("./input.txt", "r") as fileToRead:
    list1 = []
    list2 = []
    for line in fileToRead.readlines():
        line = line.strip()
        a, b = line.split("   ")
        list1.append(int(a))
        list2.append(int(b))

    heapify(list1)
    heapify(list2)
    
    total_distance = 0

    while list1 and list2:
        a, b = heappop(list1) , heappop(list2)
        total_distance += (abs(a - b))
    
    print(total_distance)
