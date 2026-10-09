import sys
import random

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    
    idx = 2
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
        
    # Check for bridges using Tarjan's bridge-finding algorithm
    # A cubic graph with a bridge cannot be 3-edge-colorable
    visited = [False] * (n + 1)
    tin = [0] * (n + 1)
    low = [0] * (n + 1)
    timer = 0
    has_bridge = False
    
    def dfs_bridge(v, p_edge):
        nonlocal timer, has_bridge
        visited[v] = True
        timer += 1
        tin[v] = low[v] = timer
        for to, edge_idx in adj[v]:
            if edge_idx == p_edge:
                continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs_bridge(to, edge_idx)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    has_bridge = True

    for i in range(1, n + 1):
        if not visited[i]:
            dfs_bridge(i, -1)
            
    if has_bridge:
        print("NO")
        return

    # Edge colors: 0 means uncolored, 1, 2, 3 are the colors
    edge_color = [0] * m
    # vertex_color_edge[v][c] gives the edge index incident to v with color c (1-indexed color)
    v_col_edge = [[-1] * 4 for _ in range(n + 1)]
    
    def set_color(e_idx, c):
        old_c = edge_color[e_idx]
        u, v = edges[e_idx]
        if old_c > 0:
            v_col_edge[u][old_c] = -1
            v_col_edge[v][old_c] = -1
        edge_color[e_idx] = c
        if c > 0:
            v_col_edge[u][c] = e_idx
            v_col_edge[v][c] = e_idx

    uncolored = list(range(m))
    random.shuffle(uncolored)
    
    max_steps = 300000
    step = 0
    
    while uncolored and step < max_steps:
        step += 1
        e_idx = uncolored.pop()
        if edge_color[e_idx] > 0:
            continue
        
        u, v = edges[e_idx]
        
        # Find free colors at u and v
        free_u = [c for c in (1, 2, 3) if v_col_edge[u][c] == -1]
        free_v = [c for c in (1, 2, 3) if v_col_edge[v][c] == -1]
        
        # If there's a common free color
        common = set(free_u) & set(free_v)
        if common:
            c = random.choice(list(common))
            set_color(e_idx, c)
            continue
        
        cu = random.choice(free_u)
        cv = random.choice(free_v)
        
        # Trace alternating (cu, cv) path starting from u
        path = []
        curr = u
        curr_c = cv # Since cu is free at u, the edge incident to u must have color cv
        
        while True:
            nxt_e = v_col_edge[curr][curr_c]
            if nxt_e == -1:
                break
            path.append((nxt_e, curr_c))
            nu, nv = edges[nxt_e]
            curr = nu if curr != nu else nv
            curr_c = cu if curr_c == cv else cv
            
        if curr != v:
            # Kempe chain does not reach v, we can flip colors on path
            for p_edge, p_col in path:
                other_c = cu if p_col == cv else cv
                set_color(p_edge, other_c)
            # Now cv is free at both u and v
            set_color(e_idx, cv)
        else:
            # Kempe chain reaches v; randomly uncolor an incident edge to resolve conflict
            if random.random() < 0.5:
                # pick a colored edge at u
                used_u = [c for c in (1, 2, 3) if v_col_edge[u][c] != -1]
                c_uncol = random.choice(used_u)
                e_to_uncol = v_col_edge[u][c_uncol]
                set_color(e_to_uncol, 0)
                uncolored.append(e_to_uncol)
                set_color(e_idx, c_uncol)
            else:
                used_v = [c for c in (1, 2, 3) if v_col_edge[v][c] != -1]
                c_uncol = random.choice(used_v)
                e_to_uncol = v_col_edge[v][c_uncol]
                set_color(e_to_uncol, 0)
                uncolored.append(e_to_uncol)
                set_color(e_idx, c_uncol)

    if any(c == 0 for c in edge_color):
        print("NO")
    else:
        print("YES")
        print(*(edge_color))

if __name__ == '__main__':
    solve()