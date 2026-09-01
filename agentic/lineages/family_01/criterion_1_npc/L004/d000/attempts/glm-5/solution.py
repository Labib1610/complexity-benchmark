import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    full = (1 << n) - 1
    # Precompute independent sets via DP
    ind = [False] * (1 << n)
    ind[0] = True
    for mask in range(1, 1 << n):
        low = mask & (-mask)
        v = low.bit_length() - 1
        if ind[mask ^ low] and (adj[v] & mask) == 0:
            ind[mask] = True
    
    # Precompute all maximal independent sets
    mis = []
    stack = [(0, 0)]
    while stack:
        mask, cand = stack.pop()
        if cand == full:
            mis.append(mask)
            continue
        # Find lowest unset bit in cand
        free = full ^ cand
        low = free & (-free)
        v = low.bit_length() - 1
        # Option 1: include v
        new_cand1 = cand | adj[v] | low
        stack.append((mask | low, new_cand1))
        # Option 2: exclude v
        new_cand2 = cand | low
        stack.append((mask, new_cand2))
    
    # For each MIS, find the complement and check if it's independent
    for mask in mis:
        comp = full ^ mask
        if ind[comp]:
            # Found a valid 3-coloring
            # mask = color 1, comp split into color 2 and color 3
            # We need lexicographically smallest: minimize color1 set, then color2 set
            # Since mask is a maximal independent set, we iterate to find the one
            # with smallest mask (lexicographically smallest color1 assignment)
            # But we need to check all valid MIS and pick the best coloring
            # Let's collect all valid (mask, comp) pairs and find the best coloring
            pass
    
    # Redo: collect all valid colorings and find lexicographically smallest
    best = None
    for mask in mis:
        comp = full ^ mask
        if ind[comp]:
            # comp is independent, split into two colors
            # To get lexicographically smallest, assign color 2 greedily
            color = [0] * n
            for i in range(n):
                if mask & (1 << i):
                    color[i] = 1
            # For remaining vertices (comp), assign color 2 or 3 greedily
            # To minimize lexicographically, try color 2 first for each vertex
            remaining = comp
            # We need to split comp into two independent sets
            # Greedy: for each vertex in order, try color 2, else color 3
            c2 = 0
            c3 = 0
            for i in range(n):
                if remaining & (1 << i):
                    # Try color 2
                    if (c2 & adj[i]) == 0:
                        c2 |= (1 << i)
                        color[i] = 2
                    else:
                        c3 |= (1 << i)
                        color[i] = 3
            # Verify
            if c2 & c3 == 0 and (c2 | c3) == remaining:
                if (c2 & adj[i] for i in range(n) if c2 & (1 << i)) and (c3 & adj[i] for i in range(n) if c3 & (1 << i)):
                    pass
                # Check validity
                valid = True
                for i in range(n):
                    if color[i] == 2 and (c2 & adj[i]):
                        valid = False
                        break
                    if color[i] == 3 and (c3 & adj[i]):
                        valid = False
                        break
                if valid:
                    if best is None or color < best:
                        best = color[:]
    
    if best is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, best)))

solve()