import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); _ = int(next(it))  # asset types ignored
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))
    edges_input = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges_input.append((u, v, cap))

    # Dinic
    N = n
    adj = [[] for _ in range(N)]
    class Edge:
        __slots__ = ('to','rev','cap','orig')
        def __init__(self, to, rev, cap, orig=False):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.orig = orig  # marks if this is the forward edge of original input

    # store reference to original forward edges to retrieve flow later
    orig_edges = [None]*m

    def add_edge(u, v, c, idx=None):
        fwd = Edge(v, len(adj[v]), c, idx is not None)
        rev = Edge(u, len(adj[u]), 0, False)
        adj[u].append(fwd)
        adj[v].append(rev)
        if idx is not None:
            orig_edges[idx] = fwd
        return fwd, rev

    for idx, (u, v, cap) in enumerate(edges_input):
        add_edge(u, v, cap, idx)

    level = [0]*N
    it_ptr = [0]*N

    def bfs():
        for i in range(N):
            level[i] = -1
        q = deque([s])
        level[s] = 0
        while q:
            v = q.popleft()
            for e in adj[v]:
                if e.cap > 0 and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t] >= 0

    def dfs(v, f):
        if v == t:
            return f
        for i in range(it_ptr[v], len(adj[v])):
            e = adj[v][i]
            if e.cap > 0 and level[e.to] == level[v] + 1:
                ret = dfs(e.to, min(f, e.cap))
                if ret:
                    e.cap -= ret
                    adj[e.to][e.rev].cap += ret
                    return ret
            it_ptr[v] += 1
        return 0

    flow = 0
    INF = 10**18
    while bfs():
        it_ptr = [0]*N
        while True:
            pushed = dfs(s, INF)
            if not pushed:
                break
            flow += pushed
            if flow >= d:  # we can stop early if reached required flow
                break
        if flow >= d:
            break

    if flow < d:
        print("NO")
        return

    # we may have sent more than d; need to adjust to exactly d.
    # Since capacities are integers, we can simply reduce excess flow along any augmenting path.
    excess = flow - d
    if excess > 0:
        # run a DFS to send back excess from t to s using residual capacities.
        # We'll treat it as sending flow from t to s in the residual graph.
        # Build reverse adjacency for residual edges with positive capacity.
        # Use simple BFS/DFS repeatedly.
        def send_back(v, need):
            if v == s:
                return need
            for e in adj[v]:
                rev_edge = adj[e.to][e.rev]
                # rev_edge is the backward edge in original direction, i.e., can push flow back if rev_edge.cap > 0
                if rev_edge.cap > 0 and level[e.to] == level[v] - 1:  # follow level graph backwards
                    pushed = send_back(e.to, min(need, rev_edge.cap))
                    if pushed:
                        rev_edge.cap -= pushed
                        e.cap += pushed
                        return pushed
            return 0

        # recompute level from t to s in residual graph
        # We'll just repeatedly find any augmenting path from t to s.
        while excess > 0:
            # BFS from t to s in residual graph
            for i in range(N):
                level[i] = -1
            q = deque([t])
            level[t] = 0
            parent = [None]*N
            while q and level[s] == -1:
                v = q.popleft()
                for e in adj[v]:
                    if e.cap > 0 and level[e.to] == -1:
                        level[e.to] = level[v] + 1
                        parent[e.to] = (v, e)
                        q.append(e.to)
            if level[s] == -1:
                break
            # find bottleneck
            v = s
            bott = excess
            while v != t:
                pv, pe = parent[v]
                bott = min(bott, pe.cap)
                v = pv
            # augment
            v = s
            while v != t:
                pv, pe = parent[v]
                pe.cap -= bott
                adj[pe.to][pe.rev].cap += bott
                v = pv
            excess -= bott

    # Now flow == d
    print("YES")
    res = []
    for e in orig_edges:
        used = e.cap  # remaining capacity, original cap - flow
        # we need original capacity; we stored only forward edge with mutable cap.
        # To get flow, we can look at reverse edge's cap.
        rev = adj[e.to][e.rev]
        flow_used = rev.cap
        res.append(str(flow_used))
    print(' '.join(res))

if __name__ == "__main__":
    solve()