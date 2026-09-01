import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
    
    # Precompute which nodes are independent (no edges between them)
    # For each subset of nodes, check if it's an independent set
    # We use this to determine valid color classes
    
    # For each node, precompute its neighbors
    neighbors = adj
    
    # Try to find a valid 3-coloring using backtracking with pruning
    # We want lexicographically smallest assignment
    
    color = [0] * (n + 1)  # 0 = uncolored, 1/2/3 = colors
    
    def is_safe(node, c):
        # Check if color c is safe for node
        # A color is safe if no neighbor has the same color
        mask = neighbors[node]
        i = 1
        while mask:
            if mask & 1:
                if color[i] == c:
                    return False
            mask >>= 1
            i += 1
        return True
    
    def get_used_colors(node):
        # Get set of colors used by neighbors
        used = set()
        mask = neighbors[node]
        i = 1
        while mask:
            if mask & 1:
                if color[i] != 0:
                    used.add(color[i])
            mask >>= 1
            i += 1
        return used
    
    def backtrack(node):
        if node > n:
            return True
        
        for c in range(1, 4):
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0
        
        return False
    
    if backtrack(1):
        print("YES")
        print(" ".join(map(str, color[1:])))
    else:
        print("NO")

solve()