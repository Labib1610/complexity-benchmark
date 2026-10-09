import sys
sys.setrecursionlimit(1000000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))

    # Check cubic
    for i in range(n):
        if len(adj[i]) != 3:
            print("NO")
            return

    # Find bridges
    tin = [-1] * n
    low = [-1] * n
    visited = [False] * n
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

    dfs(0, -1)

    # If graph not connected (shouldn't happen for cubic connected? but check)
    for i in range(n):
        if not visited[i]:
            print("NO")
            return

    if bridges:
        print("NO")
        return

    # 3-edge-coloring for bridgeless cubic graph
    # Step 1: Find a perfect matching (1-factor) using greedy + augmenting
    # Since graph is cubic and bridgeless, it has a perfect matching.
    match = [-1] * n
    used = [False] * m

    # Simple greedy matching
    for u in range(n):
        if match[u] == -1:
            for v, eid in adj[u]:
                if match[v] == -1:
                    match[u] = v
                    match[v] = u
                    used[eid] = True
                    break

    # If greedy didn't find perfect matching, we need augmenting paths.
    # But for cubic bridgeless, greedy usually works? Not guaranteed.
    # We'll implement a proper perfect matching via augmenting paths.
    # Actually, we can use a known fact: every bridgeless cubic graph has a perfect matching.
    # We'll find it via standard algorithm.

    # Let's implement a simple augmenting path search for perfect matching.
    def try_kuhn(v, visited_left, match_to):
        for to, eid in adj[v]:
            if not visited_left[to]:
                visited_left[to] = True
                if match_to[to] == -1 or try_kuhn(match_to[to], visited_left, match_to):
                    match_to[to] = v
                    return True
        return False

    match_to = [-1] * n
    for u in range(n):
        visited_left = [False] * n
        try_kuhn(u, visited_left, match_to)

    # match_to[v] = u means u matched to v
    matching_edges = []
    for v in range(n):
        u = match_to[v]
        if u != -1 and u < v:
            # find edge id
            for to, eid in adj[u]:
                if to == v:
                    matching_edges.append(eid)
                    used[eid] = True
                    break

    # Now remove matching edges, remaining graph is 2-regular (cycles)
    # Color remaining edges with 1 and 2 alternately along cycles
    color = [0] * m
    for eid in matching_edges:
        color[eid] = 3

    # Build remaining graph
    rem_adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        if not used[i]:
            rem_adj[u].append((v, i))
            rem_adj[v].append((u, i))

    # Color cycles
    visited_vertex = [False] * n
    for start in range(n):
        if not visited_vertex[start] and rem_adj[start]:
            # traverse cycle
            cur = start
            prev_edge = -1
            c = 1
            while True:
                visited_vertex[cur] = True
                # pick next edge not prev_edge
                for to, eid in rem_adj[cur]:
                    if eid != prev_edge:
                        color[eid] = c
                        prev_edge = eid
                        cur = to
                        c = 3 - c  # switch 1<->2
                        break
                if cur == start:
                    break

    # Output
    print("YES")
    print(" ".join(str(color[i]) for i in range(m)))

if __name__ == "__main__":
    solve()