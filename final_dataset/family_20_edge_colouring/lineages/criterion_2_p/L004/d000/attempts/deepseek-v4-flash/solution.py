import sys
from collections import deque

input = sys.stdin.readline

def solve():
    Na, Nw, m = map(int, input().split())
    edges = []
    adj_alpha = [[] for _ in range(Na + 1)]
    adj_omega = [[] for _ in range(Nw + 1)]
    
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj_alpha[u].append((v, i))
        adj_omega[v].append((u, i))
    
    K = 0
    for u in range(1, Na + 1):
        K = max(K, len(adj_alpha[u]))
    for v in range(1, Nw + 1):
        K = max(K, len(adj_omega[v]))
    
    color = [-1] * m
    
    # color_alpha[u][c] = edge index or -1
    color_alpha = [[-1] * (K + 1) for _ in range(Na + 1)]
    color_omega = [[-1] * (K + 1) for _ in range(Nw + 1)]
    
    for idx, (u, v) in enumerate(edges):
        # find free color for u
        cu = -1
        for c in range(1, K + 1):
            if color_alpha[u][c] == -1 and color_omega[v][c] == -1:
                cu = c
                break
        if cu != -1:
            color[idx] = cu
            color_alpha[u][cu] = idx
            color_omega[v][cu] = idx
            continue
        
        # Need to recolor along alternating path
        # Find a free color for u
        free_u = -1
        for c in range(1, K + 1):
            if color_alpha[u][c] == -1:
                free_u = c
                break
        # Find a free color for v
        free_v = -1
        for c in range(1, K + 1):
            if color_omega[v][c] == -1:
                free_v = c
                break
        
        # Start from v with free_v, find alternating path
        # We'll do BFS/DFS to find path from v (omega side) to u (alpha side)
        # using colors free_v and free_u
        
        # We'll implement the standard algorithm:
        # current vertex is omega v, current color = free_v
        # find edge from v with color free_v, go to alpha, then find edge from that alpha with color free_u, etc.
        
        # We'll use iterative approach
        path_edges = []
        current_omega = v
        current_color = free_v
        visited_alpha = [False] * (Na + 1)
        visited_omega = [False] * (Nw + 1)
        
        while True:
            # find edge from current_omega with current_color
            e = color_omega[current_omega][current_color]
            if e == -1:
                break
            path_edges.append(e)
            a = edges[e][0]
            if visited_alpha[a]:
                break
            visited_alpha[a] = True
            # now from alpha a, find edge with color free_u
            e2 = color_alpha[a][free_u]
            if e2 == -1:
                break
            path_edges.append(e2)
            w = edges[e2][1]
            if visited_omega[w]:
                break
            visited_omega[w] = True
            current_omega = w
            current_color = free_v
        
        # Now recolor path_edges: swap colors free_u and free_v
        for e in path_edges:
            old = color[e]
            if old == free_u:
                color[e] = free_v
            else:
                color[e] = free_u
        # Update color matrices
        # Rebuild color_alpha and color_omega for affected edges
        for e in path_edges:
            a, w = edges[e]
            # remove old
            for c in range(1, K + 1):
                if color_alpha[a][c] == e:
                    color_alpha[a][c] = -1
                if color_omega[w][c] == e:
                    color_omega[w][c] = -1
        for e in path_edges:
            a, w = edges[e]
            color_alpha[a][color[e]] = e
            color_omega[w][color[e]] = e
        
        # Now assign current edge
        # find free color for u
        cu = -1
        for c in range(1, K + 1):
            if color_alpha[u][c] == -1 and color_omega[v][c] == -1:
                cu = c
                break
        color[idx] = cu
        color_alpha[u][cu] = idx
        color_omega[v][cu] = idx
    
    print("YES")
    print(" ".join(map(str, color)))

if __name__ == "__main__":
    solve()