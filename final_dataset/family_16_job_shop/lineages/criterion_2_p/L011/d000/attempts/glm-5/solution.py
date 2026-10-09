import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    items = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx]); p2 = int(data[idx+1])
        items.append((p1, p2))
        idx += 2
    
    # Johnson's rule for two-machine flow shop
    # Partition into two sets and sort accordingly
    set1 = []  # p1 <= p2, sort by p1 ascending
    set2 = []  # p1 > p2, sort by p2 descending
    
    for p1, p2 in items:
        if p1 <= p2:
            set1.append((p1, p2))
        else:
            set2.append((p1, p2))
    
    set1.sort(key=lambda x: x[0])
    set2.sort(key=lambda x: x[1], reverse=True)
    
    order = set1 + set2
    
    # Simulate
    current_time_primary = 0
    current_time_secondary = 0
    for p1, p2 in order:
        current_time_primary += p1
        if current_time_secondary < current_time_primary:
            current_time_secondary = current_time_primary
        current_time_secondary += p2
    
    print(current_time_secondary)

solve()