import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    brackets = []
    idx = 1
    for _ in range(j):
        d1 = int(data[idx]); d2 = int(data[idx+1])
        brackets.append((d1, d2))
        idx += 2
    
    # Partition into two groups:
    # Group A: d1 <= d2 (non-decreasing internal spans)
    # Group B: d1 > d2 (decreasing internal spans)
    groupA = []
    groupB = []
    for d1, d2 in brackets:
        if d1 <= d2:
            groupA.append((d1, d2))
        else:
            groupB.append((d1, d2))
    
    # Group A sorted by d1 ascending (ties broken by d2 ascending)
    groupA.sort(key=lambda x: (x[0], x[1]))
    # Group B sorted by d2 descending (ties broken by d1 descending)
    groupB.sort(key=lambda x: (-x[1], -x[0]))
    
    # Concatenate: Group A first, then Group B
    sequence = groupA + groupB
    
    # Simulate the layout
    # alpha_end tracks the end of the last Alpha footprint
    # beta_start tracks the earliest start the current Beta footprint can have
    # (must be >= its own Alpha end, and >= previous Beta end)
    alpha_end = 0
    beta_end = 0
    
    for d1, d2 in sequence:
        # Alpha footprint starts at alpha_end (earliest possible)
        alpha_start = alpha_end
        alpha_end_new = alpha_start + d1
        
        # Beta footprint must start >= alpha_end_new (internal dependency)
        # and >= beta_end (Beta track ordering)
        beta_start = alpha_end_new
        if beta_end > beta_start:
            beta_start = beta_end
        beta_end = beta_start + d2
        
        alpha_end = alpha_end_new
    
    print(beta_end)

solve()