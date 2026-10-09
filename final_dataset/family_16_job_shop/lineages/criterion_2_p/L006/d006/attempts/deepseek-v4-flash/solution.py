import sys

def solve():
    data = sys.stdin.buffer.read().split()
    j = int(data[0])
    stages = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx += 2
        stages.append((p1, p2))
    
    # Sort by p2 descending, then p1 descending
    stages.sort(key=lambda x: (-x[1], -x[0]))
    
    V = 0
    sum_p1 = 0
    for p1, p2 in stages:
        sum_p1 += p1
        V = max(p2, V - p1 + p2)
    
    print(sum_p1 + V)

if __name__ == "__main__":
    solve()