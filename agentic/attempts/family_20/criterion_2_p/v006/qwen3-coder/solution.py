import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    nL = int(data[idx]); idx += 1
    nR = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    edges = []
    adj = [[] for _ in range(nL + nR + 2)]
    degree = [0] * (nL + nR + 2)
    
    offset = nL + 1
    for _ in range(m):
        u = int(data[idx]) + 0; idx += 1
        v = int(data[idx]) + 0; idx += 1
        v_offset = v + nL
        edges.append((u, v_offset))
        adj[u].append(v_offset)
        adj[v_offset].append(u)
        degree[u] += 1
        degree[v_offset] += 1
    
    # Find maximum degree
    delta = max(degree)
    if delta == 0:
        print("YES")
        return
    
    # Edge coloring using BFS-based approach (since graph is bipartite)
    # We'll use a greedy algorithm with available colors tracking per node
    
    color = [0] * (m + 1)
    used_colors_u = [set() for _ in range(nL + 1)]
    used_colors_v = [set() for _ in range(nR + 1)]
    
    # For each edge, assign the smallest available color not used by either endpoint
    for i in range(m):
        u, v_offset = edges[i]
        v = v_offset - nL
        c = 1
        while c in used_colors_u[u] or c in used_colors_v[v]:
            c += 1
        color[i+1] = c
        used_colors_u[u].add(c)
        used_colors_v[v].add(c)
    
    print("YES")
    print(' '.join(map(str, color[1:])))

if __name__ == "__main__":
    main()