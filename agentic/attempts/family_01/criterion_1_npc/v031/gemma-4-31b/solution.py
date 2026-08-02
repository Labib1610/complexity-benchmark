import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [0] * n
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr]) - 1
        v = int(input_data[ptr + 1]) - 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        ptr += 2

    # We need the lexicographically smallest assignment.
    # This means we try assigning band 1, then 2, then 3 for vertex 0, 1, ..., n-1.
    # Since n is small (up to 40), we can use backtracking with pruning.
    # To optimize, we can use bitmasks for available colors.
    
    res = [0] * n
    
    def backtrack(u):
        if u == n:
            return True
        
        # Determine which colors are used by neighbors of u that have been assigned
        used_colors = 0
        # Check neighbors v < u
        # We can pre-calculate the mask of neighbors v < u to speed up
        # But since n=40, a simple loop over neighbors is okay if pruned well.
        # Actually, let's use a bitmask of neighbors that are already assigned.
        
        # Find which colors are taken by neighbors of u
        forbidden = 0
        for v in range(u):
            if (adj[u] >> v) & 1:
                forbidden |= (1 << res[v])
        
        # Try colors 1, 2, 3 in order
        for color in (1, 2, 3):
            if not (forbidden & (1 << color)):
                res[u] = color
                
                # Heuristic: Check if any remaining unassigned vertex has no available colors
                # This is essentially a basic form of constraint propagation.
                possible = True
                for v in range(u + 1, n):
                    # For vertex v, find colors used by its neighbors already assigned
                    v_forbidden = 0
                    for w in range(u + 1):
                        if (adj[v] >> w) & 1:
                            v_forbidden |= (1 << res[w])
                    
                    # If v has no colors left (out of 1, 2, 3), this path is invalid
                    if (v_forbidden & (1 << 1)) and (v_forbidden & (1 << 2)) and (v_forbidden & (1 << 3)):
                        possible = False
                        break
                
                if possible:
                    if backtrack(u + 1):
                        return True
        
        return False

    # The simple backtracking above might be slow for N=40.
    # Let's use a more efficient approach: Backtracking with MRV (Minimum Remaining Values)
    # However, the problem asks for the lexicographically smallest sequence.
    # Lexicographical order means we MUST decide the color of vertex 0, then 1, etc.
    # We cannot use MRV for the order of assignment.
    # But we can use the "possible" check (Forward Checking) to prune.

    # To make it faster, we pre-calculate neighbors for each node.
    adj_list = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if (adj[u] >> v) & 1:
                adj_list[u].append(v)

    def backtrack_fast(u):
        if u == n:
            return True
        
        forbidden = 0
        for v in adj_list[u]:
            if v < u:
                forbidden |= (1 << res[v])
        
        for color in (1, 2, 3):
            if not (forbidden & (1 << color)):
                res[u] = color
                
                # Forward Checking
                possible = True
                for v in range(u + 1, n):
                    v_forbidden = 0
                    # Only check neighbors of v that are already assigned
                    for w in adj_list[v]:
                        if w <= u:
                            v_forbidden |= (1 << res[w])
                    
                    if (v_forbidden & 14) == 14: # 14 is binary 1110 (bits 1, 2, 3 set)
                        possible = False
                        break
                
                if possible:
                    if backtrack_fast(u + 1):
                        return True
        return False

    if backtrack_fast(0):
        print("YES")
        print(*(res))
    else:
        print("NO")

solve()