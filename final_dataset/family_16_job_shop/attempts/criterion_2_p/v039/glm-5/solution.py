import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    orders = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx]); p2 = int(data[idx+1])
        orders.append((p1, p2))
        idx += 2
    
    # Johnson's rule for two-machine flow shop
    # Group 1: p1 <= p2, sort by p1 ascending
    # Group 2: p1 > p2, sort by p2 descending
    group1 = []
    group2 = []
    for p1, p2 in orders:
        if p1 <= p2:
            group1.append((p1, p2))
        else:
            group2.append((p1, p2))
    
    group1.sort(key=lambda x: x[0])
    group2.sort(key=lambda x: x[1], reverse=True)
    
    sequence = group1 + group2
    
    t1 = 0  # time on machine 1 (oven)
    t2 = 0  # time on machine 2 (icing)
    for p1, p2 in sequence:
        t1 += p1
        if t2 < t1:
            t2 = t1 + p2
        else:
            t2 = t2 + p2
    
    print(t2)

solve()