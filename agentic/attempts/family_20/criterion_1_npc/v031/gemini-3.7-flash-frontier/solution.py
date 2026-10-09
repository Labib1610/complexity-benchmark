import sys
import random
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges = []
    idx = 2
    for i in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        edges.append((u, v))
        idx += 2
        
    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i))
        adj[v].append((u, i))
        
    # Check for bridges using Tarjan's algorithm
    tin = [-1] * n
    low = [-1] * n
    timer = 0
    has_bridge = False
    
    def dfs_bridge(u, p_edge):
        nonlocal timer, has_bridge
        tin[u] = low[u] = timer
        timer += 1
        for to, e_idx in adj[u]:
            if e_idx == p_edge:
                continue
            if tin[to] != -1:
                low[u] = min(low[u], tin[to])
            else:
                dfs_bridge(to, e_idx)
                low[u] = min(low[u], low[to])
                if low[to] > tin[u]:
                    has_bridge = True

    for i in range(n):
        if tin[i] == -1:
            dfs_bridge(i, -1)
            
    if has_bridge:
        print("NO")
        return

    # Randomized Kempe-chain coloring
    # Try up to max_restarts times
    max_restarts = 5
    max_steps = 150000

    for restart in range(max_restarts):
        edge_color = [-1] * m
        # vertex_color_edge[u][c] = edge_index with color c incident to u
        vertex_color_edge = [[-1] * 4 for _ in range(n)]
        
        uncolored = deque(range(m))
        # Shuffle initial order
        uncolored_list = list(range(m))
        random.shuffle(uncolored_list)
        uncolored = deque(uncolored_list)
        
        step = 0
        success = True
        
        while uncolored:
            step += 1
            if step > max_steps:
                success = False
                break
                
            e = uncolored.popleft()
            if edge_color[e] != -1:
                continue
                
            u, v = edges[e]
            
            # Find missing colors at u and v
            m_u = [c for c in (1, 2, 3) if vertex_color_edge[u][c] == -1]
            m_v = [c for c in (1, 2, 3) if vertex_color_edge[v][c] == -1]
            
            # Check for common missing color
            common = set(m_u) & set(m_v)
            if common:
                c = random.choice(list(common))
                edge_color[e] = c
                vertex_color_edge[u][c] = e
                vertex_color_edge[v][c] = e
                continue
                
            # Try Kempe chains
            pairs = [(c1, c2) for c1 in m_u for c2 in m_v]
            random.shuffle(pairs)
            
            augmented = False
            for c1, c2 in pairs:
                # Path starts at u with color c2, alternating c2, c1, c2, ...
                curr = u
                path_edges = []
                needed_color = c2
                while True:
                    e_next = vertex_color_edge[curr][needed_color]
                    if e_next == -1:
                        break
                    path_edges.append(e_next)
                    nxt = edges[e_next][0] if edges[e_next][1] == curr else edges[e_next][1]
                    curr = nxt
                    needed_color = c1 if needed_color == c2 else c2
                
                if curr != v:
                    # Kempe chain does not reach v, swap colors on this path
                    for pe in path_edges:
                        old_c = edge_color[pe]
                        new_c = c1 if old_c == c2 else c2
                        pu, pv = edges[pe]
                        vertex_color_edge[pu][old_c] = -1
                        vertex_color_edge[pv][old_c] = -1
                        edge_color[pe] = new_c
                    for pe in path_edges:
                        new_c = edge_color[pe]
                        pu, pv = edges[pe]
                        vertex_color_edge[pu][new_c] = pe
                        vertex_color_edge[pv][new_c] = pe
                    
                    # Now c2 is missing at both u and v
                    edge_color[e] = c2
                    vertex_color_edge[u][c2] = e
                    vertex_color_edge[v][c2] = e
                    augmented = True
                    break
                    
            if not augmented:
                # Forced conflict: pick random color c
                c = random.choice((1, 2, 3))
                e_u = vertex_color_edge[u][c]
                if e_u != -1:
                    edge_color[e_u] = -1
                    uu, uv = edges[e_u]
                    vertex_color_edge[uu][c] = -1
                    vertex_color_edge[uv][c] = -1
                    uncolored.append(e_u)
                
                e_v = vertex_color_edge[v][c]
                if e_v != -1:
                    edge_color[e_v] = -1
                    vu, vv = edges[e_v]
                    vertex_color_edge[vu][c] = -1
                    vertex_color_edge[vv][c] = -1
                    uncolored.append(e_v)
                
                edge_color[e] = c
                vertex_color_edge[u][c] = e
                vertex_color_edge[v][c] = e

        if success and all(edge_color[i] != -1 for i in range(m)):
            print("YES")
            print(*(edge_color[i] for i in range(m)))
            return

    print("NO")

if __name__ == '__main__':
    solve()