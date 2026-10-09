import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    triples = []
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        triples.append((x, y, z))
    
    if k == 0:
        print("YES")
        return
    
    # Group triples by x
    by_x = [[] for _ in range(k)]
    for idx, (x, y, z) in enumerate(triples):
        by_x[x].append((y, z, idx))
    
    # Precompute masks for each x: set of (y,z) pairs
    # We'll use DP over x from 0 to k-1
    # State: used_y (bitmask), used_z (bitmask)
    # We need to assign each x exactly one triple
    
    # To optimize, we process x in order and prune
    # Since k <= 22, masks up to 2^22 ~ 4M, but we can't store all states
    # We'll use BFS/DFS with memoization on (x, used_y, used_z)
    # But state space is too large. Instead, we use meet-in-the-middle or branch and bound.
    
    # Let's try iterative DP with dictionary, but prune aggressively
    # Actually, since each x must be assigned, and we have k steps, we can do DP layer by layer
    # But the number of states could be large. Let's try with pruning: only keep reachable states.
    
    # However, worst case could be exponential. Given k<=22, maybe it's acceptable with pruning.
    # Let's implement a recursive backtracking with heuristics: order x by number of options (MRV)
    
    # First, check if any x has no options
    for i in range(k):
        if not by_x[i]:
            print("NO")
            return
    
    # Order x by number of available triples (ascending) for MRV heuristic
    order = sorted(range(k), key=lambda i: len(by_x[i]))
    
    # We'll do backtracking
    used_y = 0
    used_z = 0
    assignment = [None] * k  # for each x, store (y, z, idx)
    
    # Precompute for each x in order, the list of (y, z, idx)
    options = [by_x[i] for i in order]
    
    # Recursive function
    sys.setrecursionlimit(10000)
    
    def backtrack(pos, used_y, used_z):
        if pos == k:
            return True
        for y, z, idx in options[pos]:
            yb = 1 << y
            zb = 1 << z
            if not (used_y & yb) and not (used_z & zb):
                assignment[order[pos]] = (y, z, idx)
                if backtrack(pos + 1, used_y | yb, used_z | zb):
                    return True
        return False
    
    if backtrack(0, 0, 0):
        print("YES")
        out = []
        for i in range(k):
            y, z, idx = assignment[i]
            x = i
            out.append(f"{x+1} {y+1} {z+1}")
        print("\n".join(out))
    else:
        print("NO")

solve()