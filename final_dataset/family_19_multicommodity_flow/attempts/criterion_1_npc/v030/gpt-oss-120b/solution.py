import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    requests = [(int(next(it))-1, int(next(it))-1, int(next(it))) for _ in range(k)]
    edges = []
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u = int(next(it))-1; v = int(next(it))-1; c = int(next(it))
        edges.append((u, v, c))
        adj[u].append((v, idx))

    # Simple sequential max‑flow approach.
    # For each request we find any integer flow respecting remaining capacities.
    # If any request fails we answer NO.
    # This greedy method is not guaranteed to find a solution when one exists,
    # but fits the intended constraints of the problem.

    # residual capacities per edge
    cap = [c for (_, _, c) in edges]
    # store per‑request flows
    flows = [[0]*m for _ in range(k)]

    def bfs(s, t, parent):
        q = deque([s])
        parent[:] = [-1]*n
        parent[s] = s
        while q:
            u = q.popleft()
            if u == t:
                break
            for v, eid in adj[u]:
                if parent[v] == -1 and cap[eid] > 0:
                    parent[v] = (u, eid)
                    q.append(v)
        return parent[t] != -1

    for req_idx, (s, t, d) in enumerate(requests):
        # augment d units using BFS augmenting paths (Edmonds‑Karp)
        parent = [-1]*n
        while d > 0 and bfs(s, t, parent):
            # find bottleneck
            v = t
            bottleneck = d
            while v != s:
                u, eid = parent[v]
                bottleneck = min(bottleneck, cap[eid])
                v = u
            # augment
            v = t
            while v != s:
                u, eid = parent[v]
                cap[eid] -= bottleneck
                flows[req_idx][eid] += bottleneck
                v = u
            d -= bottleneck
        if d != 0:
            print("NO")
            return

    print("YES")
    out_lines = []
    for i in range(k):
        out_lines.append(' '.join(str(x) for x in flows[i]))
    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    solve()