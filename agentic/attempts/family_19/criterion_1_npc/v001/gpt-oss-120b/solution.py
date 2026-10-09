import sys
import collections
import itertools

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    products = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        products.append((s, t, d))

    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))

    # ---------- max flow for one product ----------
    def max_flow(s, t, need, caps):
        """return list of flow on each original edge (length m) or None"""
        # build adjacency list with residual capacities
        adj = [[] for _ in range(n)]
        # each edge: forward and backward
        class Edge:
            __slots__ = ('to','rev','cap','orig')
        forward_refs = [None] * m  # to read residual later

        for idx, (u, v, _) in enumerate(edges):
            cap = caps[idx]
            fwd = Edge()
            rev = Edge()
            fwd.to = v
            fwd.rev = rev
            fwd.cap = cap
            fwd.orig = idx          # original index
            rev.to = u
            rev.rev = fwd
            rev.cap = 0
            rev.orig = -1
            adj[u].append(fwd)
            adj[v].append(rev)
            forward_refs[idx] = fwd

        flow = 0
        parent = [None] * n
        while flow < need:
            # BFS
            for i in range(n):
                parent[i] = None
            q = collections.deque([s])
            parent[s] = (None, None)   # (prev vertex, edge)
            while q and parent[t] is None:
                u = q.popleft()
                for e in adj[u]:
                    if e.cap > 0 and parent[e.to] is None:
                        parent[e.to] = (u, e)
                        q.append(e.to)
            if parent[t] is None:
                break          # no augmenting path
            # find bottleneck
            aug = need - flow
            v = t
            while v != s:
                u, e = parent[v]
                aug = min(aug, e.cap)
                v = u
            # augment
            v = t
            while v != s:
                u, e = parent[v]
                e.cap -= aug
                e.rev.cap += aug
                v = u
            flow += aug
        if flow < need:
            return None
        # compute used flow on original edges
        used = [0] * m
        for idx, fwd in enumerate(forward_refs):
            used[idx] = edges[idx][2] - fwd.cap   # original cap - residual
        return used

    # ---------- try all permutations ----------
    result = [[0] * m for _ in range(k)]
    original_caps = [c for (_, _, c) in edges]

    for perm in itertools.permutations(range(k)):
        caps = original_caps[:]
        ok = True
        for idx in perm:
            s, t, need = products[idx]
            flow = max_flow(s, t, need, caps)
            if flow is None:
                ok = False
                break
            result[idx] = flow
            for j in range(m):
                caps[j] -= flow[j]
        if ok:
            out = ['YES']
            for i in range(k):
                out.append(' '.join(str(x) for x in result[i]))
            sys.stdout.write('\n'.join(out))
            return

    sys.stdout.write('NO')

if __name__ == "__main__":
    solve()