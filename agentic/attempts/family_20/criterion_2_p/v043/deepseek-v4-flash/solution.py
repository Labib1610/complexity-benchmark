import sys
from collections import deque

input = sys.stdin.readline

def solve():
    Nin, Nout, M = map(int, input().split())
    edges = []
    adj_in = [[] for _ in range(Nin)]
    adj_out = [[] for _ in range(Nout)]
    
    for i in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj_in[u].append((v, i))
        adj_out[v].append((u, i))
    
    D = 0
    for i in range(Nin):
        D = max(D, len(adj_in[i]))
    for i in range(Nout):
        D = max(D, len(adj_out[i]))
    
    color = [0] * M
    # color_in[u][c] = edge index or -1
    color_in = [[-1] * (D + 1) for _ in range(Nin)]
    color_out = [[-1] * (D + 1) for _ in range(Nout)]
    
    for idx, (u, v) in enumerate(edges):
        # find free color for u
        c = 1
        while color_in[u][c] != -1:
            c += 1
        # assign
        color[idx] = c
        color_in[u][c] = idx
        color_out[v][c] = idx
        
        # resolve conflicts on v
        while True:
            conflict_idx = color_out[v][c]
            if conflict_idx == -1 or conflict_idx == idx:
                break
            # find new color for conflict edge
            u2, v2 = edges[conflict_idx]
            # remove from old color
            color_in[u2][c] = -1
            color_out[v2][c] = -1
            # find free color for u2
            c2 = 1
            while color_in[u2][c2] != -1:
                c2 += 1
            color[conflict_idx] = c2
            color_in[u2][c2] = conflict_idx
            color_out[v2][c2] = conflict_idx
            # now conflict moves to v2 with color c2
            v = v2
            c = c2
    
    print("YES")
    print(" ".join(map(str, color)))

if __name__ == "__main__":
    solve()