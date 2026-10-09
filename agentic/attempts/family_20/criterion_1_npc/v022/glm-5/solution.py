import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for i in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Check for bridges using DFS
    disc = [0] * (n + 1)
    low = [0] * (n + 1)
    timer = [1]
    has_bridge = [False]
    
    def dfs(u, pe):
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        for v, e in adj[u]:
            if e == pe:
                continue
            if disc[v] == 0:
                dfs(v, e)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    has_bridge[0] = True
            else:
                low[u] = min(low[u], disc[v])
    
    for i in range(1, n + 1):
        if disc[i] == 0:
            dfs(i, -1)
    
    if has_bridge[0]:
        print("NO")
        return
    
    # Find proper 3-edge-coloring using Kempe chains
    color = [0] * m
    edge_idx = defaultdict(dict)
    for i, (u, v) in enumerate(edges):
        edge_idx[u][v] = i
        edge_idx[v][u] = i
    
    def get_color(u, v):
        return color[edge_idx[u][v]]
    
    def set_color(u, v, c):
        color[edge_idx[u][v]] = c
    
    def used_colors(u):
        return {color[e] for _, e in adj[u]}
    
    def find_alt_path(u, c1, c2, exclude_edge):
        """Find alternating c1-c2 path from u, return list of (vertex, edge) or None"""
        path = []
        visited = {u}
        cur = u
        while True:
            found = None
            for v, e in adj[cur]:
                if e == exclude_edge:
                    continue
                if color[e] == c1 and v not in visited:
                    found = (v, e)
                    break
            if found is None:
                break
            v, e = found
            path.append((v, e))
            visited.add(v)
            cur = v
            c1, c2 = c2, c1
        return path
    
    for i, (u, v) in enumerate(edges):
        used_u = used_colors(u)
        used_v = used_colors(v)
        avail_u = {1, 2, 3} - used_u
        avail_v = {1, 2, 3} - used_v
        common = avail_u & avail_v
        
        if common:
            c = min(common)
            color[i] = c
        else:
            # Need Kempe chain manipulation
            c_u = min(avail_u)
            c_v = min(avail_v)
            
            # Find alternating path from u using colors c_v, c_u
            path = find_alt_path(u, c_v, c_u, i)
            
            if path and path[-1][0] != v:
                # Swap colors along path
                for _, e in path:
                    if color[e] == c_v:
                        color[e] = c_u
                    else:
                        color[e] = c_v
                color[i] = c_v
            else:
                # Try the other direction
                path = find_alt_path(v, c_u, c_v, i)
                if path and path[-1][0] != u:
                    for _, e in path:
                        if color[e] == c_u:
                            color[e] = c_v
                        else:
                            color[e] = c_u
                    color[i] = c_u
                else:
                    # Try all color combinations
                    done = False
                    for c1 in [1, 2, 3]:
                        for c2 in [1, 2, 3]:
                            if c1 == c2:
                                continue
                            if c1 not in avail_u or c2 not in avail_v:
                                continue
                            path = find_alt_path(u, c2, c1, i)
                            if path and path[-1][0] != v:
                                for _, e in path:
                                    if color[e] == c2:
                                        color[e] = c1
                                    else:
                                        color[e] = c2
                                color[i] = c2
                                done = True
                                break
                        if done:
                            break
                    if not done:
                        color[i] = c_u  # fallback
    
    # Verify coloring
    for u in range(1, n + 1):
        cols = [color[e] for _, e in adj[u]]
        if len(set(cols)) != 3:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, color)))

solve()