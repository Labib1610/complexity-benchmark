import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    _ = int(data[idx]); idx += 1
    s = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    d = int(data[idx]); idx += 1

    edges = []
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        cap = int(data[idx]); idx += 1
        edges.append((u, v, cap))
        adj[u].append((v, i))
        adj[v].append((u, i))

    # BFS to find augmenting path in residual graph
    def bfs():
        parent_node = [-1] * (n + 1)
        parent_edge = [-1] * (n + 1)
        parent_node[s] = s
        q = deque([s])
        while q:
            u = q.popleft()
            for v, eid in adj[u]:
                if parent_node[v] == -1:
                    u0, v0, cap = edges[eid]
                    if u == u0:
                        residual = cap - flow[eid]
                    else:
                        residual = flow[eid]
                    if residual > 0:
                        parent_node[v] = u
                        parent_edge[v] = eid
                        if v == t:
                            return parent_node, parent_edge
                        q.append(v)
        return None, None

    flow = [0] * m
    total = 0
    while total < d:
        pn, pe = bfs()
        if pn is None:
            break
        # find bottleneck
        path = []
        cur = t
        b = float('inf')
        while cur != s:
            eid = pe[cur]
            path.append(eid)
            u0, v0, cap = edges[eid]
            if pn[cur] == u0:
                residual = cap - flow[eid]
            else:
                residual = flow[eid]
            if residual < b:
                b = residual
            cur = pn[cur]
        need = d - total
        if b > need:
            b = need
        for eid in path:
            u0, v0, cap = edges[eid]
            if pn[edges[eid][1]] == u0:
                flow[eid] += b
            else:
                flow[eid] -= b
        total += b

    if total < d:
        sys.stdout.write("NO\n")
    else:
        out = ["YES", " ".join(map(str, flow))]
        sys.stdout.write("\n".join(out) + "\n")

solve()