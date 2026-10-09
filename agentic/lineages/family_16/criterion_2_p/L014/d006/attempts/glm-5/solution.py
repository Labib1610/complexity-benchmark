import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    j = int(input_data[0])
    items = []
    idx = 1
    for _ in range(j):
        p1 = int(input_data[idx])
        p2 = int(input_data[idx+1])
        items.append((p1, p2))
        idx += 2
    
    # Sort by (p1-p2, p1 if p1<=p2 else -p1)
    items.sort(key=lambda x: (x[0]-x[1], x[0] if x[0] <= x[1] else -x[0]))
    
    T = sum(p2 for p1, p2 in items)
    
    max_sync = 0
    prefix_p1 = 0
    prefix_p2 = 0  # prefix_p2[k-1] = sum of p2 for first k-1 items
    
    for p1, p2 in items:
        prefix_p1 += p1
        # sync at this position = prefix_p1 + (T - prefix_p2)
        sync = prefix_p1 + T - prefix_p2
        if sync > max_sync:
            max_sync = sync
        prefix_p2 += p2
    
    print(max_sync)

solve()