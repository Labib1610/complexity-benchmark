import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1

    orders = []
    for _ in range(k):
        s = int(data[idx]); idx += 1
        t = int(data[idx]); idx += 1
        d = int(data[idx]); idx += 1
        orders.append((s, t, d))

    edges = []
    adj = [[] for _ in range(n + 1)]
    for j in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        cap = int(data[idx]); idx += 1
        edges.append((u, v, cap))
        adj[u].append((v, j))
        adj[v].append((u, j))

    # BFS to find reachable nodes from source
    def bfs_reachable(src):
        visited = [False] * (n + 1)
        visited[src] = True
        q = deque([src])
        while q:
            u = q.popleft()
            for v, j in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        return visited

    # BFS to find path from src to dst
    def bfs_path(src, dst):
        visited = [False] * (n + 1)
        parent = [-1] * (n + 1)
        parent_edge = [-1] * (n + 1)
        visited[src] = True
        q = deque([src])
        while q:
            u = q.popleft()
            if u == dst:
                break
            for v, j in adj[u]:
                if not visited[v] and edge_cap[j] > 0:
                    visited[v] = True
                    parent[v] = u
                    parent_edge[v] = j
                    q.append(v)
        if not visited[dst]:
            return None
        path_edges = []
        cur = dst
        while cur != src:
            j = parent_edge[cur]
            path_edges.append(j)
            cur = parent[cur]
        path_edges.reverse()
        return path_edges

    # Check feasibility
    edge_cap = [cap for (u, v, cap) in edges]
    feasible = True
    for s, t, d in orders:
        reach = bfs_reachable(s)
        if not reach[t]:
            feasible = False
            break

    if not feasible:
        print("NO")
        return

    # Greedy routing
    flow = [[0] * m for _ in range(k)]
    for i in range(k):
        s, t, d = orders[i]
        remaining = d
        while remaining > 0:
            path = bfs_path(s, t)
            if path is None:
                feasible = False
                break
            bottleneck = min(edge_cap[j] for j in path)
            send = min(bottleneck, remaining)
            for j in path:
                edge_cap[j] -= send
                flow[i][j] += send
            remaining -= send
        if not feasible:
            break

    if not feasible:
        print("NO")
    else:
        print("YES")
        out = []
        for i in range(k):
            out.append(' '.join(map(str, flow[i])))
        print('\n'.join(out))

solve()