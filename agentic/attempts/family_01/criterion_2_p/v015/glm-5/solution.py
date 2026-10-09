import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1])
    # build adjacency using CSR
    deg = [0] * (n + 1)
    us = [0] * m
    vs = [0] * m
    idx = 2
    for i in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        us[i] = u; vs[i] = v
        deg[u] += 1; deg[v] += 1
    # prefix sums
    start = [0] * (n + 2)
    for i in range(1, n + 1):
        start[i + 1] = start[i] + deg[i]
    adj = [0] * (2 * m)
    pos = start[1:n+1]  # copy? careful
    fill = start[:]  # fill[i] is next insertion index for vertex i
    for i in range(m):
        u = us[i]; v = vs[i]
        adj[fill[u]] = v; fill[u] += 1
        adj[fill[v]] = u; fill[v] += 1
    color = [0] * (n + 1)
    for s in range(1, n + 1):
        if color[s]:
            continue
        color[s] = 1
        q = deque([s])
        while q:
            u = q.popleft()
            cu = color[u]
            nc = 3 - cu
            for j in range(start[u], start[u+1]):
                w = adj[j]
                if color[w] == 0:
                    color[w] = nc
                    q.append(w)
                elif color[w] == cu:
                    print("NO")
                    return
    out = []
    out.append("YES")
    out.append(' '.join(map(str, color[1:])))
    sys.stdout.write('\n'.join(out) + '\n')

main()