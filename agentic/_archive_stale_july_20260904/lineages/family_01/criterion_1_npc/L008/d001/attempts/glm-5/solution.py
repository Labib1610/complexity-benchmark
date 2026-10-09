import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Check if graph is bipartite
    color = [-1] * n
    is_bipartite = True
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            stack = [i]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
                        break
                if not is_bipartite:
                    break
        if not is_bipartite:
            break
    
    if not is_bipartite:
        print("NO")
        return
    
    # Find connected components
    visited = [False] * n
    components = []
    for i in range(n):
        if not visited[i]:
            comp = []
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            components.append(comp)
    
    # DP: for each component, track which color gets sealant 1
    # dp[i] = set of possible (mask1, mask2) pairs after processing first i components
    # mask1 = parts with sealant 1, mask2 = parts with sealant 2
    # We use a set of tuples (mask1, mask2)
    
    dp = { (0, 0) }
    
    for comp in components:
        new_dp = set()
        # Determine which vertices in comp have color 0 and color 1
        c0 = [v for v in comp if color[v] == 0]
        c1 = [v for v in comp if color[v] == 1]
        
        for mask1, mask2 in dp:
            # Option A: color 0 gets sealant 1, color 1 gets sealant 2
            new_mask1 = mask1
            new_mask2 = mask2
            for v in c0:
                new_mask1 |= (1 << v)
            for v in c1:
                new_mask2 |= (1 << v)
            new_dp.add((new_mask1, new_mask2))
            
            # Option B: color 0 gets sealant 1, color 1 gets sealant 3
            new_mask1 = mask1
            new_mask2 = mask2
            for v in c0:
                new_mask1 |= (1 << v)
            new_dp.add((new_mask1, new_mask2))
            
            # Option C: color 0 gets sealant 2, color 1 gets sealant 1
            new_mask1 = mask1
            new_mask2 = mask2
            for v in c1:
                new_mask1 |= (1 << v)
            for v in c0:
                new_mask2 |= (1 << v)
            new_dp.add((new_mask1, new_mask2))
            
            # Option D: color 0 gets sealant 2, color 1 gets sealant 3
            new_mask1 = mask1
            new_mask2 = mask2
            for v in c0:
                new_mask2 |= (1 << v)
            new_dp.add((new_mask1, new_mask2))
            
            # Option E: color 0 gets sealant 3, color 1 gets sealant 1
            new_mask1 = mask1
            new_mask2 = mask2
            for v in c1:
                new_mask1 |= (1 << v)
            new_dp.add((new_mask1, new_mask2))
            
            # Option F: color 0 gets sealant 3, color 1 gets sealant 2
            new_mask1 = mask1
            new_mask2 = mask2
            for v in c1:
                new_mask2 |= (1 << v)
            new_dp.add((new_mask1, new_mask2))
        
        dp = new_dp
    
    if not dp:
        print("NO")
        return
    
    # Find lexicographically smallest assignment
    # We need to find the assignment that minimizes s[0], then s[1], etc.
    # s[i] = 1 if i in mask1, 2 if i in mask2, 3 otherwise
    
    best = None
    for mask1, mask2 in dp:
        s = []
        for i in range(n):
            if mask1 & (1 << i):
                s.append(1)
            elif mask2 & (1 << i):
                s.append(2)
            else:
                s.append(3)
        if best is None or s < best:
            best = s
    
    print("YES")
    print(' '.join(map(str, best)))

solve()