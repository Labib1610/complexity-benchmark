import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    j = int(input_data[0])
    cakes = []
    idx = 1
    for _ in range(j):
        p1 = int(input_data[idx]); p2 = int(input_data[idx+1])
        cakes.append((p1, p2))
        idx += 2
    
    # Sort by Johnson's rule: cakes with p1 <= p2 first, sorted by p1 ascending;
    # then cakes with p1 > p2, sorted by p2 descending.
    group1 = [c for c in cakes if c[0] <= c[1]]
    group2 = [c for c in cakes if c[0] > c[1]]
    group1.sort(key=lambda x: x[0])
    group2.sort(key=lambda x: x[1], reverse=True)
    order = group1 + group2
    
    oven_end = 0
    frosting_end = 0
    for p1, p2 in order:
        oven_end += p1
        # Frosting starts when both the cake is done in oven and the frosting machine is free
        start = max(oven_end, frosting_end)
        frosting_end = start + p2
    
    print(frosting_end)

solve()