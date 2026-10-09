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
    
    # Johnson's rule for 2-machine flow shop
    # Split into two groups:
    # Group 1: p1 <= p2, sort by p1 ascending
    # Group 2: p1 > p2, sort by p2 descending
    group1 = []
    group2 = []
    for p1, p2 in jobs:
        if p1 <= p2:
            group1.append((p1, p2))
        else:
            group2.append((p1, p2))
    
    group1.sort(key=lambda x: x[0])
    group2.sort(key=lambda x: x[1], reverse=True)
    
    order = group1 + group2
    
    time1 = 0
    time2 = 0
    for p1, p2 in order:
        if time1 > time2:
            # machine 2 is free at time2, but machine 1 finishes this job at time1 + p1
            start2 = time1 + p1
        else:
            start2 = time2 + p1
        # Actually correct calculation:
        # finish1 = time1 + p1
        # start2 = max(finish1, time2)
        # finish2 = start2 + p2
        finish1 = time1 + p1
        start2 = finish1 if finish1 > time2 else time2
        finish2 = start2 + p2
        time1 = finish1
        time2 = finish2
    
    print(time2)

solve()