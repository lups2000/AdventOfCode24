
def mix(num, secret):
    return num ^ secret

def prune(secret):
    return secret % 16777216

def simulate_step(secret, cycles):
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
    return secret

with open("./input.txt", "r") as fileToRead:
    res = 0
    for line in fileToRead.readlines():
        secret = int(line.strip())
        res += simulate_step(secret, 2000)
    
    print(res)
    