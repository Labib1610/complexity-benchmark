import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    relays = []
    idx = 2
    for _ in range(t):
        a = int(data[idx]); b = int(data[idx+1]); c = int(data[idx+2])
        idx += 3
        relays.append((a, b, c))
    
    full_mask = (1 << k) - 1
    
    # Group relays by (a, b) to speed up the inner loop.
    # For each (a, b), we store list of c values.
    from collections import defaultdict
    groups = defaultdict(list)
    for (a, b, c) in relays:
        groups[(a, b)].append(c)
    
    # We need to select exactly one relay for each value of a in 1..k,
    # one for each value of b in 1..k, and one for each value of c in 1..k.
    # This is equivalent to finding a perfect matching in a 3-partite 3-uniform hypergraph.
    # We use backtracking over a-values, maintaining used_b and used_c masks.
    
    # Precompute bit masks
    # a, b, c are 1-indexed; bit position i corresponds to value i+1.
    
    # Sort a-values by number of available (b,c) pairs (heuristic: most constrained first)
    a_values = list(range(1, k+1))
    
    # For each a, collect list of (b, c) pairs available
    a_to_pairs = [[] for _ in range(k+1)]
    for (a, b, c) in relays:
        a_to_pairs[a].append((b, c))
    
    # Sort pairs for each a by how constrained b is (heuristic)
    # Count how many times each b appears
    b_count = [0] * (k+1)
    for (a, b, c) in relays:
        b_count[b] += 1
    
    for a in range(1, k+1):
        a_to_pairs[a].sort(key=lambda bc: (b_count[bc[0]], bc[0], bc[1]))
    
    # Sort a_values by number of available pairs (ascending = most constrained first)
    a_values.sort(key=lambda a: len(a_to_pairs[a]))
    
    # Backtracking
    used_b = 0
    used_c = 0
    chosen = [None] * (k+1)  # chosen[a] = (b, c)
    
    def backtrack(pos):
        nonlocal used_b, used_c
        if pos == k:
            return True
        a = a_values[pos]
        for (b, c) in a_to_pairs[a]:
            bbit = 1 << (b-1)
            cbit = 1 << (c-1)
            if (used_b & bbit) == 0 and (used_c & cbit) == 0:
                used_b |= bbit
                used_c |= cbit
                chosen[a] = (b, c)
                if backtrack(pos + 1):
                    return True
                used_b ^= bbit
                used_c ^= cbit
                chosen[a] = None
        return False
    
    if backtrack(0):
        print("YES")
        for a in range(1, k+1):
            b, c = chosen[a]
            print(f"{a} {b} {c}")
    else:
        print("NO")

solve()