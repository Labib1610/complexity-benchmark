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
        jobs.append((p1, p2))
        idx += 2
    
    # Johnson's rule for two-machine flow shop
    # Split into two sets: p1 < p2 (set1) and p1 >= p2 (set2)
    set1 = []
    set2 = []
    for p1, p2 in jobs:
        if p1 < p2:
            set1.append((p1, p2))
        else:
            set2.append((p1, p2))
    
    # set1 sorted by p1 ascending
    set1.sort(key=lambda x: x[0])
    # set2 sorted by p2 descending
    set2.sort(key=lambda x: -x[1])
    
    order = set1 + set2
    
    t1 = 0
    t2 = 0
    for p1, p2 in order:
        t1 += p1
        if t2 < t1:
            t2 = t1 + p2
        else:
            t2 += p2
    
    print(t2)

solve()