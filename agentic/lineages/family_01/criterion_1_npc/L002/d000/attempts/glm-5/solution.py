import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [0] * (n + 1)
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    # forbidden[u] = bitmask of modules that cannot share the same state as u
    forbidden = [0] * (n + 1)
    for u in range(1, n + 1):
        forbidden[u] = adj[u]
    
    # We need to assign states 1,2,3 such that adjacent modules differ.
    # This is 3-coloring. Find lexicographically smallest.
    
    # Greedy with backtracking might be needed, but n <= 40.
    # Let's try a smarter approach: since it's 3-coloring, we can use the structure.
    # Actually, let's just do backtracking with pruning.
    
    color = [0] * (n + 1)  # 0 = unassigned, 1/2/3 = colors
    
    def backtrack(u):
        if u > n:
            return True
        # Determine available colors
        used = 0
        v = adj[u]
        while v:
            low = v & (-v)
            idx_v = low.bit_length() - 1
            if color[idx_v]:
                used |= 1 << color[idx_v]
            v ^= low
        for c in range(1, 4):
            if not (used & (1 << c)):
                color[u] = c
                if backtrack(u + 1):
                    return True
                color[u] = 0
        return False
    
    if backtrack(1):
        print("YES")
        print(" ".join(str(color[i]) for i in range(1, n + 1)))
    else:
        print("NO")

solve()