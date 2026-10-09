import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    _ = int(data[idx]); idx += 1  # always 1

    s = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    d = int(data[idx]); idx += 1

    edges = []
    adj = [[] for _ in range(n + 1)]
    for j in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        C = int(data[idx]); idx += 1
        edges.append((u, v, C))
        adj[u].append((v, j))
        adj[v].append((u, j))

    # BFS from s to t to find a path
    parent_edge = [-1] * (n + 1)
    parent_node = [0] * (n + 1)
    visited = [False] * (n + 1)
    q = deque([s])
    visited[s] = True
    while q:
        u = q.popleft()
        if u == t:
            break
        for v, j in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent_node[v] = u
                parent_edge[v] = j
                q.append(v)

    if not visited[t]:
        print("NO")
        return

    # Reconstruct path
    path_edges = []
    cur = t
    while cur != s:
        j = parent_edge[cur]
        path_edges.append(j)
        cur = parent_node[cur]

    # Assign d to path edges
    x = [0] * m
    for j in path_edges:
        x[j] = d

    # Check bounds
    for j in range(m):
        if x[j] > edges[j][2]:
            print("NO")
            return

    print("YES")
    print(' '.join(map(str, x)))

solve()