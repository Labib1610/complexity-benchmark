import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    N_in, N_out, M = map(int, input().split())
    edges = []
    adj_in = [[] for _ in range(N_in + 1)]
    adj_out = [[] for _ in range(N_out + 1)]
    
    for idx in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj_in[u].append((v, idx))
        adj_out[v].append((u, idx))
    
    D = 0
    for u in range(1, N_in + 1):
        D = max(D, len(adj_in[u]))
    for v in range(1, N_out + 1):
        D = max(D, len(adj_out[v]))
    
    color_in = [0] * (N_in + 1)  # last used color for each ingress
    color_out = [0] * (N_out + 1)  # last used color for each egress
    edge_color = [0] * M
    
    # We'll color edges one by one using augmenting path method
    for u, v in edges:
        # find free color for u
        used_u = set()
        for (_, idx) in adj_in[u]:
            if edge_color[idx] != 0:
                used_u.add(edge_color[idx])
        cu = 1
        while cu in used_u:
            cu += 1
        
        # find free color for v
        used_v = set()
        for (_, idx) in adj_out[v]:
            if edge_color[idx] != 0:
                used_v.add(edge_color[idx])
        cv = 1
        while cv in used_v:
            cv += 1
        
        if cu == cv:
            edge_color[edges.index((u, v))] = cu
            continue
        
        # Need to recolor along an alternating path
        # We'll implement the standard algorithm:
        # Start with edge (u,v) colored cu, then find path starting from v with color cu
        # and ending at some vertex missing cu, flipping colors along the path.
        
        # We'll do BFS/DFS to find augmenting path
        # color cu is for u, cv is for v
        # We want to assign cu to (u,v) and shift colors along path
        
        # Build path: start from v, looking for edge colored cu
        # We'll use iterative approach
        
        # We'll store parent pointers for path reconstruction
        parent = {}
        visited = set()
        q = deque()
        q.append(('out', v, cu))
        visited.add(('out', v))
        found = None
        
        while q and found is None:
            typ, node, col = q.popleft()
            if typ == 'out':
                # look for edges from this egress with color col
                for (u2, idx) in adj_out[node]:
                    if edge_color[idx] == col:
                        if ('in', u2) not in visited:
                            visited.add(('in', u2))
                            parent[('in', u2)] = (typ, node, col, idx)
                            # check if u2 has free color col
                            used_u2 = set()
                            for (_, idx2) in adj_in[u2]:
                                if edge_color[idx2] != 0:
                                    used_u2.add(edge_color[idx2])
                            if col not in used_u2:
                                found = ('in', u2, col)
                                break
                            q.append(('in', u2, col))
            else:
                # typ == 'in'
                for (v2, idx) in adj_in[node]:
                    if edge_color[idx] == col:
                        if ('out', v2) not in visited:
                            visited.add(('out', v2))
                            parent[('out', v2)] = (typ, node, col, idx)
                            # check if v2 has free color col
                            used_v2 = set()
                            for (_, idx2) in adj_out[v2]:
                                if edge_color[idx2] != 0:
                                    used_v2.add(edge_color[idx2])
                            if col not in used_v2:
                                found = ('out', v2, col)
                                break
                            q.append(('out', v2, col))
        
        if found is None:
            # Should not happen in bipartite graph with D colors
            # But fallback: assign cv
            edge_color[edges.index((u, v))] = cv
            continue
        
        # Reconstruct path and flip colors
        # found is (typ, node, col)
        # We'll walk back via parent
        path_edges = []
        cur = found
        while cur in parent:
            typ, node, col, idx = parent[cur]
            path_edges.append((idx, col))
            cur = (typ, node)
        
        # Now flip colors along path
        for idx, col in path_edges:
            # find the other color for this edge
            uu, vv = edges[idx]
            # find current color
            cur_col = edge_color[idx]
            # find the other color used by uu or vv
            used_uu = set()
            for (_, idx2) in adj_in[uu]:
                if edge_color[idx2] != 0:
                    used_uu.add(edge_color[idx2])
            used_vv = set()
            for (_, idx2) in adj_out[vv]:
                if edge_color[idx2] != 0:
                    used_vv.add(edge_color[idx2])
            # find a color not used by both
            new_col = 1
            while new_col in used_uu or new_col in used_vv:
                new_col += 1
            edge_color[idx] = new_col
        
        # Now assign cu to the original edge
        edge_color[edges.index((u, v))] = cu
    
    print("YES")
    print(" ".join(str(c) for c in edge_color))

if __name__ == "__main__":
    solve()