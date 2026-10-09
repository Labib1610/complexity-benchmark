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
    
    # Johnson's rule for 2-machine flow shop
    jobs.sort(key=lambda x: min(x[0], x[1]))
    
    m1_time = 0
    m2_time = 0
    for p1, p2 in jobs:
        m1_time += p1
        if m1_time > m2_time:
            m2_time = m1_time + p2
        else:
            m2_time += p2
    
    print(m2_time)

solve()