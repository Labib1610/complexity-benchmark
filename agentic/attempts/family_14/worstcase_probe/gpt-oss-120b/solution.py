import sys
import heapq
def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); t = int(next(it)); B = int(next(it))
    req = [int(next(it)) - 1 for _ in range(t)]
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w, len(edges)))
        adj[v].append((u, w, len(edges)))
        edges.append((u, v, w))
    INF = 10**18
    full = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]
    parent = [[None] * n for _ in range(1 << t)]  # (prev_mask, prev_node, edge_id)
    for i, v in enumerate(req):
        mask = 1 << i
        dp[mask][v] = 0
    # DP over subsets
    for mask in range(1, full + 1):
        # combine submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            for v in range(n):
                val = dp[sub][v] + dp[other][v]
                if val < dp[mask][v]:
                    dp[mask][v] = val
                    parent[mask][v] = (sub, v, None)  # combine at v
            sub = (sub - 1) & mask
        # Dijkstra to propagate through graph
        heap = [(dp[mask][v], v) for v in range(n) if dp[mask][v] < INF]
        heapq.heapify(heap)
        visited = [False] * n
        while heap:
            d, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            for v, w, eid in adj[u]:
                nd = d + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    parent[mask][v] = (mask, u, eid)
                    heapq.heappush(heap, (nd, v))
    # find best root
    best_cost = INF
    best_root = -1
    for v in range(n):
        if dp[full][v] < best_cost:
            best_cost = dp[full][v]
            best_root = v
    if best_cost > B:
        print("NO")
        return
    # reconstruct edges
    used_edges = set()
    def dfs(mask, v):
        p = parent[mask][v]
        if p is None:
            return
        pmask, pu, eid = p
        if eid is not None:
            used_edges.add(eid)
            dfs(pmask, pu)
        else:
            # combine
            sub = pmask
            other = mask ^ sub
            dfs(sub, v)
            dfs(other, v)
    dfs(full, best_root)
    print("YES")
    for eid in used_edges:
        u, v, _ = edges[eid]
        print(u + 1, v + 1)

if __name__ == "__main__":
    solve()