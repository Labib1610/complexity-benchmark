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
    
    color = [0] * n
    
    def is_possible():
        for i in range(n):
            if color[i] == 0:
                if not dfs(i, 1):
                    return False
        return True
    
    def dfs(u, c):
        color[u] = c
        for v in adj[u]:
            if color[v] == 0:
                if not dfs(v, 4 - c):
                    return False
            elif color[v] == c:
                return False
        return True
    
    if not is_possible():
        print("NO")
        return
    
    # Build complement graph
    complement_adj = [[] for _ in range(n)]
    for u in range(n):
        neighbors = set(adj[u])
        for v in range(n):
            if v != u and v not in neighbors:
                complement_adj[u].append(v)
    
    # Find connected components in complement graph
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
                for v in complement_adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            components.append(comp)
    
    # DP: dp[mask] = True if mask is achievable
    # mask encodes which components are in set S (agents with color 3)
    num_comp = len(components)
    dp = [False] * (1 << num_comp)
    dp[0] = True
    parent = [-1] * (1 << num_comp)
    
    for mask in range(1 << num_comp):
        if not dp[mask]:
            continue
        for i in range(num_comp):
            if not (mask & (1 << i)):
                # Check if component i is bipartite
                is_bip = True
                for u in components[i]:
                    for v in adj[u]:
                        if v in components[i]:
                            is_bip = False
                            break
                    if not is_bip:
                        break
                if is_bip:
                    new_mask = mask | (1 << i)
                    if not dp[new_mask]:
                        dp[new_mask] = True
                        parent[new_mask] = i
    
    # Find a valid mask
    valid_mask = -1
    for mask in range(1 << num_comp):
        if dp[mask]:
            # Check if remaining components form bipartite graph
            remaining = []
            for i in range(num_comp):
                if not (mask & (1 << i)):
                    remaining.append(i)
            
            # Build subgraph of remaining components
            rem_nodes = set()
            for i in remaining:
                for u in components[i]:
                    rem_nodes.add(u)
            
            # Check bipartite
            temp_color = [0] * n
            ok = True
            for u in rem_nodes:
                if temp_color[u] == 0:
                    if not dfs_bip(u, 1, temp_color, rem_nodes, adj):
                        ok = False
                        break
            if ok:
                valid_mask = mask
                break
    
    if valid_mask == -1:
        print("NO")
        return
    
    # Assign colors
    result = [0] * n
    
    # Assign color 3 to components in valid_mask
    for i in range(num_comp):
        if valid_mask & (1 << i):
            for u in components[i]:
                result[u] = 3
    
    # Assign colors 1 and 2 to remaining nodes
    rem_nodes = set()
    for i in range(num_comp):
        if not (valid_mask & (1 << i)):
            for u in components[i]:
                rem_nodes.add(u)
    
    temp_color = [0] * n
    for u in rem_nodes:
        if temp_color[u] == 0:
            dfs_bip(u, 1, temp_color, rem_nodes, adj)
    
    for u in rem_nodes:
        result[u] = temp_color[u]
    
    print("YES")
    print(' '.join(map(str, result)))

def dfs_bip(u, c, color, nodes, adj):
    color[u] = c
    for v in adj[u]:
        if v in nodes:
            if color[v] == 0:
                if not dfs_bip(v, 3 - c, color, nodes, adj):
                    return False
            elif color[v] == c:
                return False
    return True

solve()