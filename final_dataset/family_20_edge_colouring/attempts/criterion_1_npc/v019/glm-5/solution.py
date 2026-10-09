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
    edges = []
    for i in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Check degree constraint
    for i in range(n):
        if len(adj[i]) != 3:
            print("NO")
            return
    
    edge_color = [0] * m
    used_at_node = [0] * n  # bitmask of colors used at each node
    
    def dfs(u, p_eid, p_color):
        # u is current node, arrived via edge p_eid with color p_color
        # Find the two other edges at u
        e1_idx = -1
        e2_idx = -1
        for v, eid in adj[u]:
            if eid != p_eid:
                if e1_idx == -1:
                    e1_idx = eid
                else:
                    e2_idx = eid
        
        # Determine colors for e1 and e2
        # They must be the two colors != p_color
        c1 = p_color % 3 + 1
        c2 = c1 % 3 + 1
        
        # Try to assign c1 to e1 and c2 to e2
        # Check if valid
        u1, v1 = edges[e1_idx]
        u2, v2 = edges[e2_idx]
        nu1 = u1 if v1 == u else v1
        nu2 = u2 if v2 == u else v2
        
        # Check if c1 is available at nu1 and c2 at nu2
        if not (used_at_node[nu1] & (1 << c1)) and not (used_at_node[nu2] & (1 << c2)):
            edge_color[e1_idx] = c1
            edge_color[e2_idx] = c2
            used_at_node[nu1] |= (1 << c1)
            used_at_node[nu2] |= (1 << c2)
            
            # Recurse
            if dfs(nu1, e1_idx, c1) and dfs(nu2, e2_idx, c2):
                return True
            
            # Backtrack
            used_at_node[nu1] ^= (1 << c1)
            used_at_node[nu2] ^= (1 << c2)
        
        # Try swapping: c2 to e1, c1 to e2
        if not (used_at_node[nu1] & (1 << c2)) and not (used_at_node[nu2] & (1 << c1)):
            edge_color[e1_idx] = c2
            edge_color[e2_idx] = c1
            used_at_node[nu1] |= (1 << c2)
            used_at_node[nu2] |= (1 << c1)
            
            if dfs(nu1, e1_idx, c2) and dfs(nu2, e2_idx, c1):
                return True
            
            used_at_node[nu1] ^= (1 << c2)
            used_at_node[nu2] ^= (1 << c1)
        
        return False
    
    # Start from node 0
    # Pick first edge, assign color 1
    u0, v0 = edges[0]
    edge_color[0] = 1
    used_at_node[u0] |= 2
    used_at_node[v0] |= 2
    
    if dfs(u0, 0, 1) and dfs(v0, 0, 1):
        print("YES")
        print(' '.join(map(str, edge_color)))
    else:
        print("NO")

solve()