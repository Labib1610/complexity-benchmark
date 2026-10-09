import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    jobs = []
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        jobs.append((p1, p2))
    
    # Johnson's rule: partition into two groups
    group1 = []  # p1 <= p2, sort by p1 ascending
    group2 = []  # p1 > p2, sort by p2 descending
    
    for p1, p2 in jobs:
        if p1 <= p2:
            group1.append((p1, p2))
        else:
            group2.append((p1, p2))
    
    group1.sort(key=lambda x: x[0])
    group2.sort(key=lambda x: -x[2])
    
    order = group1 + group2
    
    time_m1 = 0
    time_m2 = 0
    
    for p1, p2 in order:
        time_m1 += p1
        time_m2 = max(time_m1, time_m2) + p2
    
    print(time_m2)

solve()