import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    triples = []
    idx = 2
    for _ in range(t):
        a = int(data[idx]); b = int(data[idx+1]); c = int(data[idx+2])
        idx += 3
        triples.append((a-1, b-1, c-1))
    
    # Build adjacency: for each (p1, p2), list of p3 values
    adj = {}
    for (a, b, c) in triples:
        key = (a, b)
        if key in adj:
            adj[key].append(c)
        else:
            adj[key] = [c]
    
    # We need a perfect matching in a 3-partite 3-uniform hypergraph.
    # Use inclusion-based DP over subsets of P2 and P3, matching P1 in order.
    # State: subset of P2 used, subset of P3 used. Value: chosen p2 for current p1 (or -1 if none).
    # We process p1 from 0 to k-1.
    
    full = (1 << k) - 1
    # dp[mask2][mask3] = previous p2 choice (or -1)
    # We'll use dict for sparse representation, but k<=22 so 2^22 is too big for full table.
    # However, total states are limited because mask2 and mask3 have same popcount = p1 index.
    # Use dict keyed by (mask2, mask3).
    
    # Initialize: before processing any p1, mask2=0, mask3=0
    # We'll store for each state the p2 chosen to reach it (for backtracking).
    
    # To save memory, use dict: key=(mask2, mask3), value=p2_chosen
    # But we need to reconstruct path, so store parent info.
    
    # Let's use arrays of dicts: for each level (number of p1 processed), a dict.
    # Actually we can do iterative DP with dict.
    
    # current: dict mapping (mask2, mask3) -> p2 chosen for this step
    # parent: dict mapping (mask2, mask3) -> (prev_mask2, prev_mask3)
    
    # Start
    from collections import deque
    
    # We'll do BFS/DP layer by layer
    # level 0: state (0,0)
    # For each p1 in 0..k-1, we extend.
    
    # Use dict for current states
    cur = {(0, 0): None}  # (mask2, mask3) -> (p2, p3) chosen to reach here, or None for start
    parent = {}  # (mask2, mask3, level) -> (prev_mask2, prev_mask3)
    # Actually we can store parent as we go.
    
    # We need to reconstruct, so store for each state at level i the previous state and choice.
    # Let's store: state_info[(mask2, mask3)] = (p2, p3, prev_mask2, prev_mask3)
    # But since we process layer by layer, we can keep a list of dicts.
    
    layers = []  # each layer is dict: (mask2, mask3) -> (p2, p3, prev_mask2, prev_mask3)
    layers.append({(0, 0): (None, None, None, None)})
    
    for i in range(k):
        prev_layer = layers[-1]
        cur_layer = {}
        for (mask2, mask3), _ in prev_layer.items():
            # For p1 = i, try all (p2, p3) such that (i, p2, p3) is a triple
            key = (i, None)  # we need to iterate over all p2 where (i, p2) exists
            # Instead, iterate over triples with p1=i
            # But we pre-built adj keyed by (p1, p2). Let's iterate over p2.
            # We can precompute for each p1 a list of (p2, p3).
            pass
        # We need efficient iteration. Let's precompute for each p1 the list of (p2, p3).
        # Rebuild:
        break
    
    # Precompute for each p1 the list of (p2, p3)
    by_p1 = [[] for _ in range(k)]
    for (a, b, c) in triples:
        by_p1[a].append((b, c))
    
    # Now DP
    layers = [{(0, 0): (None, None, None, None)}]
    found = False
    final_state = None
    
    for i in range(k):
        prev_layer = layers[-1]
        cur_layer = {}
        for (mask2, mask3) in prev_layer:
            for (p2, p3) in by_p1[i]:
                if (mask2 >> p2) & 1:
                    continue
                if (mask3 >> p3) & 1:
                    continue
                new_mask2 = mask2 | (1 << p2)
                new_mask3 = mask3 | (1 << p3)
                if (new_mask2, new_mask3) not in cur_layer:
                    cur_layer[(new_mask2, new_mask3)] = (p2, p3, mask2, mask3)
        layers.append(cur_layer)
        if not cur_layer:
            break
    
    # Check if we reached full masks
    last_layer = layers[-1]
    target = (full, full)
    if target in last_layer:
        # Reconstruct
        path = []
        cur_m2, cur_m3 = full, full
        for i in range(k, 0, -1):
            p2, p3, prev_m2, prev_m3 = layers[i][(cur_m2, cur_m3)]
            path.append((i-1, p2, p3))
            cur_m2, cur_m3 = prev_m2, prev_m3
        path.reverse()
        
        out = ["YES"]
        for (a, b, c) in path:
            out.append(f"{a+1} {b+1} {c+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

solve()