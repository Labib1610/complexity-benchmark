import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    parts = []
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        parts.append((p1, p2))
    
    # Johnson's rule for two-machine flow shop
    # Group 1: p1 < p2, sort by p1 ascending
    # Group 2: p1 >= p2, sort by p2 descending
    group1 = []
    group2 = []
    for p1, p2 in parts:
        if p1 < p2:
            group1.append((p1, p2))
        else:
            group2.append((p1, p2))
    
    group1.sort(key=lambda x: x[0])
    group2.sort(key=lambda x: -x[1])
    
    order = group1 + group2
    
    # Simulate to find makespan
    time_milling = 0
    time_polishing = 0
    for p1, p2 in order:
        time_milling += p1
        # Polishing starts at max(time_milling, time_polishing)
        time_polishing = max(time_milling, time_polishing) + p2
    
    print(time_polishing)

if __name__ == "__main__":
    solve()