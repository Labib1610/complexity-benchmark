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

def find_perfect_matching(n, adj, edges):
    # Use simple DFS-based augmenting path for small n (n <= 2000)
    match_to = [-1] * n
    def augment(u, visited):
        for v, eid in adj[u]:
            if visited[v]:
                continue
            visited[v] = True
            if match_to[v] == -1 or augment(match_to[v], visited):
                match_to[v] = u
                match_to[u] = v
                return True
        return False

    for u in range(n):
        if match_to[u] == -1:
            visited = [False] * n
            augment(u, visited)
    return match_to

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

    # Find perfect matching
    match = find_perfect_matching(n, adj, edges)
    # match[u] = v means u matched with v

    color = [0] * m

    # Color matching edges with 1
    for u in range(n):
        if match[u] != -1 and u < match[u]:
            # find edge id
            for v, eid in adj[u]:
                if v == match[u]:
                    color[eid] = 1
                    break

    # Remaining edges form cycles
    # Build adjacency for remaining edges
    rem_adj = [[] for _ in range(n)]
    for eid, (u, v) in enumerate(edges):
        if color[eid] == 0:
            rem_adj[u].append((v, eid))
            rem_adj[v].append((u, eid))

    visited = [False] * n
    for start in range(n):
        if not visited[start] and rem_adj[start]:
            # traverse cycle
            cycle_edges = []
            prev = -1
            cur = start
            while True:
                visited[cur] = True
                # pick next edge not going back to prev
                nxt = None
                for to, eid in rem_adj[cur]:
                    if eid != prev:
                        nxt = (to, eid)
                        break
                if nxt is None:
                    break
                cycle_edges.append(nxt[1])
                prev = nxt[1]
                cur = nxt[0]
                if cur == start:
                    break
            # color cycle alternately 2,3
            for i, eid in enumerate(cycle_edges):
                color[eid] = 2 if i % 2 == 0 else 3

    print("YES")
    print(" ".join(map(str, color)))

if __name__ == "__main__":
    solve()