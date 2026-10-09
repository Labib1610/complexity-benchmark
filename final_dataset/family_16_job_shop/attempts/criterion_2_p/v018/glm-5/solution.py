import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    
    # Separate requests into two groups based on comparison of p1 and p2
    group1 = []  # p1 <= p2
    group2 = []  # p1 > p2
    
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 <= p2:
            group1.append((p1, p2))
        else:
            group2.append((p1, p2))
    
    # Sort group1 by p1 (ascending)
    group1.sort(key=lambda x: x[0])
    # Sort group2 by p2 (descending)
    group2.sort(key=lambda x: -x[2])
    
    # Combine groups
    requests = group1 + group2
    
    # Simulate the process
    time_p1 = 0
    time_p2 = 0
    
    for p1, p2 in requests:
        time_p1 += p1
        # Secondary unit starts at max(time_p2, time_p1) and finishes at that time + p2
        time_p2 = max(time_p2, time_p1) + p2
    
    print(time_p2)

solve()