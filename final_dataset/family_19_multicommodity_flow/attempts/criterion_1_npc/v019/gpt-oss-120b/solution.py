import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    n = next(it); m = next(it); k = next(it)

    s = []; t = []; d = []
    for _ in range(k):
        s.append(next(it) - 1)
        t.append(next(it) - 1)
        d.append(next(it))

    edges_u = []
    edges_v = []
    cap = []
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u = next(it) - 1
        v = next(it) - 1
        c = next(it)
        edges_u.append(u)
        edges_v.append(v)
        cap.append(c)
        adj[u].append(idx)          # store edge index

    # remaining capacities
    remaining = cap[:]
    # answer matrix
    ans = [[0] * m for _ in range(k)]

    # ---------- max flow for a single commodity ----------
    def max_flow_one(src, sink, need):
        """returns (flow_value, flow_per_edge) where flow_per_edge is dict edge->amt"""
        flow_on_edge = [0] * m
        total = 0
        # residual adjacency: for each edge we need reverse edge with 0 capacity
        # we build a temporary structure each call
        # store for each edge its residual capacity
        res_cap = remaining[:]          # copy of current capacities
        # also need reverse edges; we will store them in separate lists
        # create adjacency with (to, edge_idx, rev_idx)
        rev_adj = [[] for _ in range(n)]
        for idx in range(m):
            u = edges_u[idx]; v = edges_v[idx]
            rev_adj[u].append((v, idx, len(rev_adj[v])))   # forward
            rev_adj[v].append((u, -1, len(rev_adj[u]) - 1)) # reverse placeholder

        # we will maintain residual capacities in a dict keyed by (u, pos in rev_adj[u])
        # but simpler: we keep arrays forward_cap and reverse_cap
        forward_cap = res_cap[:]
        reverse_cap = [0] * m

        while total < need:
            # BFS
            parent = [None] * n
            q = deque([src])
            parent[src] = (-1, -1)   # mark visited
            while q and parent[sink] is None:
                u = q.popleft()
                for pos, (v, eidx, revpos) in enumerate(rev_adj[u]):
                    # capacity
                    if eidx >= 0:
                        cap_here = forward_cap[eidx]
                    else:
                        # reverse edge of original eidx = -1, need original index
                        # find original edge index from rev adjacency
                        # reverse edge corresponds to some original edge; we can get it via revpos
                        # but we stored reverse_cap aligned with original edges
                        # we can retrieve original edge index from rev_adj[v][revpos][1]
                        orig = rev_adj[v][revpos][1]
                        cap_here = reverse_cap[orig]
                    if cap_here > 0 and parent[v] is None:
                        parent[v] = (u, (eidx, revpos))
                        q.append(v)
                        if v == sink:
                            break
            if parent[sink] is None:
                break   # no augmenting path
            # find bottleneck
            inc = need - total
            v = sink
            while v != src:
                u, (eidx, revpos) = parent[v]
                if eidx >= 0:
                    inc = min(inc, forward_cap[eidx])
                else:
                    orig = rev_adj[v][revpos][1]
                    inc = min(inc, reverse_cap[orig])
                v = u
            # augment
            v = sink
            while v != src:
                u, (eidx, revpos) = parent[v]
                if eidx >= 0:
                    forward_cap[eidx] -= inc
                    reverse_cap[eidx] += inc
                    flow_on_edge[eidx] += inc
                else:
                    orig = rev_adj[v][revpos][1]
                    forward_cap[orig] += inc
                    reverse_cap[orig] -= inc
                    flow_on_edge[orig] -= inc
                v = u
            total += inc
        return total, flow_on_edge

    sys.setrecursionlimit(10000)
    def dfs(idx):
        if idx == k:
            return True
        src = s[idx]; sink = t[idx]; need = d[idx]
        flow_val, flow_edge = max_flow_one(src, sink, need)
        if flow_val < need:
            return False
        # apply flow
        for j in range(m):
            if flow_edge[j]:
                remaining[j] -= flow_edge[j]
                ans[idx][j] = flow_edge[j]
        if dfs(idx + 1):
            return True
        # backtrack
        for j in range(m):
            if flow_edge[j]:
                remaining[j] += flow_edge[j]
                ans[idx][j] = 0
        return False

    possible = dfs(0)
    out = []
    if possible:
        out.append("YES")
        for i in range(k):
            out.append(" ".join(str(x) for x in ans[i]))
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()