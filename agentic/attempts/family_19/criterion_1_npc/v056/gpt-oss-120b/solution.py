import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    s = [0]*k
    t = [0]*k
    demand = [0]*k
    for i in range(k):
        s[i] = int(next(it))
        t[i] = int(next(it))
        demand[i] = int(next(it))

    # edges in input order
    class Edge:
        __slots__ = ('u','v','cap')
        def __init__(self,u,v,c):
            self.u=u;self.v=v;self.cap=c
    edges = []
    adj = [[] for _ in range(n+1)]
    for idx in range(m):
        u = int(next(it)); v = int(next(it)); c = int(next(it))
        edges.append(Edge(u,v,c))
        adj[u].append(idx)

    used_total = [0]*m
    used = [[0]*m for _ in range(k)]

    for i in range(k):
        need = demand[i]
        src = s[i]; dst = t[i]
        while need > 0:
            parent_edge = [-1]*(n+1)
            parent_vert = [-1]*(n+1)
            q = deque()
            q.append(src)
            parent_vert[src] = src
            while q and parent_vert[dst] == -1:
                u = q.popleft()
                for e_idx in adj[u]:
                    if parent_vert[edges[e_idx].v] != -1:
                        continue
                    residual = edges[e_idx].cap - used_total[e_idx]
                    if residual > 0:
                        parent_vert[edges[e_idx].v] = u
                        parent_edge[edges[e_idx].v] = e_idx
                        q.append(edges[e_idx].v)
            if parent_vert[dst] == -1:
                print("NO")
                return
            # reconstruct path and bottleneck
            path = []
            bottleneck = need
            v = dst
            while v != src:
                e = parent_edge[v]
                residual = edges[e].cap - used_total[e]
                if residual < bottleneck:
                    bottleneck = residual
                path.append(e)
                v = parent_vert[v]
            # augment
            for e in path:
                used_total[e] += bottleneck
                used[i][e]   += bottleneck
            need -= bottleneck

    # all contracts satisfied
    out_lines = ["YES"]
    for i in range(k):
        out_lines.append(' '.join(str(used[i][e]) for e in range(m)))
    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    solve()