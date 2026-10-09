import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().split()
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
    
    assignment = [0] * n
    
    def dfs(u):
        for v in adj[u]:
            if assignment[v] == 0:
                assignment[v] = 3 - assignment[u]
                if not dfs(v):
                    return False
            elif assignment[v] == assignment[u]:
                return False
        return True
    
    # Process each connected component
    for i in range(n):
        if assignment[i] == 0:
            assignment[i] = 1
            if not dfs(i):
                print("NO")
                return
    
    # Build conflict graph for vertices with assignment 1
    # These vertices must be assigned to enclosures 1 or 2
    # Original assignment 1 -> try 1 or 2
    # Original assignment 2 -> must be 3
    
    # Vertices that need to be assigned to 1 or 2
    group = [i for i in range(n) if assignment[i] == 1]
    idx = {v: i for i, v in enumerate(group)}
    k = len(group)
    
    if k == 0:
        # All vertices are in group 2, assign to enclosure 3
        result = [3] * n
        print("YES")
        print(' '.join(map(str, result)))
        return
    
    # Build conflict graph among group vertices
    conflict_adj = [[] for _ in range(k)]
    for u in group:
        for v in adj[u]:
            if v in idx:
                conflict_adj[idx[u]].append(idx[v])
    
    # Check if conflict graph is bipartite
    color = [-1] * k
    valid = True
    
    def dfs_color(u, c):
        nonlocal valid
        color[u] = c
        for v_idx in conflict_adj[u]:
            if color[v_idx] == -1:
                dfs_color(v_idx, 1 - c)
            elif color[v_idx] == c:
                valid = False
    
    for i in range(k):
        if color[i] == -1:
            dfs_color(i, 0)
    
    if not valid:
        print("NO")
        return
    
    # Construct final assignment
    result = [0] * n
    for i in range(n):
        if assignment[i] == 2:
            result[i] = 3
        else:
            # group vertex: color 0 -> enclosure 1, color 1 -> enclosure 2
            result[i] = color[idx[i]] + 1
    
    print("YES")
    print(' '.join(map(str, result)))

solve()