import sys
sys.setrecursionlimit(1000000)

def find_bridges(n, adj, edges):
    visited = [False] * n
    tin = [-1] * n
    low = [-1] * n
    timer = 0
    bridges = set()

    def dfs(v, p_edge):
        nonlocal timer
        visited[v] = True
        tin[v] = low[v] = timer
        timer += 1
        for to, eid in adj[v]:
            if eid == p_edge:
                continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.add(eid)
    for i in range(n):
        if not visited[i]:
            dfs(i, -1)
    return bridges

def solve():
    input_data = sys.stdin.read().strip().split()
    n = int(input_data[0])
    m = int(input_data[1])
    edges = []
    adj = [[] for _ in range(n)]
    idx = 2
    for eid in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        edges.append((u, v))
        adj[u].append((v, eid))
        adj[v].append((u, eid))

    # Check for bridges
    bridges = find_bridges(n, adj, edges)
    if bridges:
        print("NO")
        return

    # Find a perfect matching using simple greedy (since cubic bridgeless => perfect matching exists)
    # We'll use a simple approach: find a 2-factor by removing a perfect matching.
    # Use a standard algorithm: find perfect matching via alternating paths (Kőnig's theorem for bipartite? Not bipartite here).
    # Instead, we can use a known constructive method: 
    # 1. Find a perfect matching using a simple DFS-based approach for cubic graphs.
    # But for simplicity, we can use networkx? Not allowed. We'll implement a simple matching algorithm.

    # Since n <= 2000, we can use a simple augmenting path algorithm for general graphs (Edmonds' Blossom) — but that's complex.
    # However, for cubic bridgeless graphs, we can find a perfect matching by repeatedly picking an edge and removing its endpoints.
    # This greedy works for cubic graphs? Not always, but for small n we can try backtracking.

    # Let's implement a simple backtracking perfect matching search.
    match = [-1] * n
    used = [False] * n

    def find_matching():
        # simple greedy: pick vertex with smallest degree, match with neighbor
        deg = [len(adj[i]) for i in range(n)]
        matched = [False] * n
        matching_edges = []
        # We'll do a simple greedy that works for cubic bridgeless graphs in practice
        # Actually, we can use a known fact: every bridgeless cubic graph has a perfect matching.
        # We'll find it via a simple DFS-based approach: 
        # Try to match vertices one by one.
        def backtrack():
            # find first unmatched
            try:
                v = next(i for i in range(n) if not matched[i])
            except StopIteration:
                return True
            # try neighbors
            for to, eid in adj[v]:
                if not matched[to]:
                    matched[v] = matched[to] = True
                    matching_edges.append(eid)
                    if backtrack():
                        return True
                    matching_edges.pop()
                    matched[v] = matched[to] = False
            return False

        backtrack()
        return matching_edges

    matching_edges = find_matching()
    # Color matching edges with 1
    color = [0] * m
    for eid in matching_edges:
        color[eid] = 1

    # Build graph without matching edges
    adj2 = [[] for _ in range(n)]
    for eid, (u, v) in enumerate(edges):
        if color[eid] == 0:
            adj2[u].append((v, eid))
            adj2[v].append((u, eid))

    # Now remaining graph is 2-regular (cycles). Color alternately 2 and 3.
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            # traverse cycle
            cycle_edges = []
            start = i
            prev = -1
            cur = i
            while True:
                visited[cur] = True
                # find next neighbor not prev
                nxt = None
                nxt_eid = None
                for to, eid in adj2[cur]:
                    if eid != prev:
                        nxt = to
                        nxt_eid = eid
                        break
                if nxt is None:
                    break
                cycle_edges.append(nxt_eid)
                prev = nxt_eid
                cur = nxt
                if cur == start:
                    break
            # color alternately
            for k, eid in enumerate(cycle_edges):
                color[eid] = 2 if k % 2 == 0 else 3

    # Output
    print("YES")
    print(" ".join(str(c) for c in color))

if __name__ == "__main__":
    solve()