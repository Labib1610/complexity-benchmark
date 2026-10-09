import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    jobs = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx]); p2 = int(data[idx+1])
        idx += 2
        jobs.append((p1, p2))
    
    # Johnson's rule for two-machine flow shop
    jobs.sort(key=lambda x: (min(x[0], x[1]), x[0] - x[1]))
    
    time1 = 0
    time2 = 0
    for p1, p2 in jobs:
        if time1 + p1 > time2:
            time2 = time1 + p1
        time1 += p1
        time2 += p2
    
    print(time2)

solve()