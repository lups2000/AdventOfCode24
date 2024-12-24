
from collections import defaultdict


def mix(num, secret):
    return num ^ secret

def prune(secret):
    return secret % 16777216

def simulate_step(secret, cycles):
    sequence = [(secret % 10)]
    for _ in range(cycles):
        temp = secret * 64
        secret = mix(temp, secret)
        secret = prune(secret)

        temp = secret // 32
        secret = mix(temp, secret)
        secret = prune(secret)

        temp = secret * 2048
        secret = mix(temp, secret)
        secret = prune(secret)
        sequence.append((secret % 10))
    return sequence

with open("./input.txt", "r") as fileToRead:
    my_map = defaultdict(int)
    for line in fileToRead.readlines():
        secret = int(line.strip())
        sequence = simulate_step(secret, 2000)
        seen = set()

        for i in range(len(sequence) - 4):
            a, b, c, d, e = sequence[i:i+5]
            seq = (b - a, c - b, d - c, e - d)
            if seq not in seen:
                seen.add(seq)
                my_map[seq] += e
    print(max(my_map.values()))