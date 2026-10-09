import sys
from collections import defaultdict

def solve():
    input = sys.stdin.readline
    N_S, N_G, M = map(int, input().split())
    edges = []
    adj_s = [[] for _ in range(N_S + 1)]
    adj_g = [[] for _ in range(N_G + 1)]
    
    for i in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj_s[u].append((v, i))
        adj_g[v].append((u, i))
    
    # Compute D
    D = 0
    for u in range(1, N_S + 1):
        D = max(D, len(adj_s[u]))
    for v in range(1, N_G + 1):
        D = max(D, len(adj_g[v]))
    
    color = [0] * M
    # color_s[u][c] = edge index or -1
    color_s = [[-1] * (D + 1) for _ in range(N_S + 1)]
    color_g = [[-1] * (D + 1) for _ in range(N_G + 1)]
    
    for idx, (u, v) in enumerate(edges):
        # find free color for u
        c = 1
        while color_s[u][c] != -1 or color_g[v][c] != -1:
            c += 1
        # assign
        color[idx] = c
        color_s[u][c] = idx
        color_g[v][c] = idx
        
        # Recolor conflicts if any (shouldn't happen with proper search)
        # But we can implement the standard recoloring if needed.
    
    # The above greedy may fail if we don't do recoloring.
    # We'll implement the full algorithm with recoloring.
    
    # Reset and do proper algorithm
    color = [0] * M
    color_s = [[-1] * (D + 1) for _ in range(N_S + 1)]
    color_g = [[-1] * (D + 1) for _ in range(N_G + 1)]
    
    for idx, (u, v) in enumerate(edges):
        # find free color for u
        c = 1
        while color_s[u][c] != -1:
            c += 1
        # assign
        color[idx] = c
        color_s[u][c] = idx
        # now fix conflicts on ground side
        conflict = color_g[v][c]
        while conflict != -1:
            # find new color for conflict edge
            u2, v2 = edges[conflict]
            c2 = 1
            while color_s[u2][c2] != -1 or color_g[v2][c2] != -1:
                c2 += 1
            # recolor conflict
            color[conflict] = c2
            color_s[u2][c] = -1
            color_s[u2][c2] = conflict
            color_g[v2][c] = -1
            color_g[v2][c2] = conflict
            # now check if v has conflict with c2
            conflict = color_g[v][c2]
            c = c2
        color_g[v][c] = idx
    
    out = ['YES']
    out.append(' '.join(map(str, color)))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()