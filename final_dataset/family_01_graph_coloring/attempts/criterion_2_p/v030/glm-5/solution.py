import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    # Build adjacency list using arrays (CSR format) for speed
    us = [0] * m
    vs = [0] * m
    deg = [0] * (n + 1)
    for i in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        us[i] = u
        vs[i] = v
        deg[u] += 1
        deg[v] += 1
    
    # CSR
    start = [0] * (n + 2)
    for i in range(1, n + 1):
        start[i + 1] = start[i] + deg[i]
    pos = start[:]  # copy for filling; pos[i] is next slot for vertex i... careful with indices
    adj = [0] * (2 * m)
    for i in range(m):
        u = us[i]
        v = vs[i]
        adj[pos[u]] = v
        pos[u] += 1
        adj[pos[v]] = u
        pos[v] += 1
    
    color = [0] * (n + 1)  # 0 = uncolored, 1 or 2
    
    for s in range(1, n + 1):
        if color[s] != 0:
            continue
        color[s] = 1
        stack = [s]
        while stack:
            u = stack.pop()
            cu = color[u]
            for j in range(start[u], start[u + 1]):
                w = adj[j]
                if color[w] == 0:
                    color[w] = 3 - cu
                    stack.append(w)
                elif color[w] == cu:
                    print("NO")
                    return
    
    print("YES")
    sys.stdout.write(' '.join(map(str, color[1:])))
    sys.stdout.write('\n')

main()