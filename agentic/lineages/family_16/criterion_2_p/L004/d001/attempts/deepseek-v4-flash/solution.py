import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    rituals = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx +=  ​2
        rituals.append((p1, p2))
    
    # Sort by sum of p1 and p2 in descending order
    rituals.sort(key=lambda x: x[0] + x[1], reverse=True)
    
    prefix = 0
    total_channel = sum(p2 for _, p2 in rituals)
    max_strain = 0
    for p1, p2 in rituals:
        prefix += p1
        total_channel -= p2
        strain = prefix + total_channel
        if strain > max_strain:
            max_strain = strain
    
    print(max_strain)



if __name__ == "__main__":
    solve()