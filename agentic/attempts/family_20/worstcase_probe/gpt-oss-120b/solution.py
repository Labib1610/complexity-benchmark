import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append((v, idx))
        adj[v].append((u, idx))

    # 1. bipartite test
    color = [-1] * n
    ok = True
    for start in range(n):
        if color[start] != -1:
            continue
        q = deque([start])
        color[start] = 0
        while q:
            v = q.popleft()
            for to, _ in adj[v]:
                if color[to] == -1:
                    color[to] = color[v] ^ 1
                    q.append(to)
                elif color[to] == color[v]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            break
    if not ok:
        print("NO")
        return

    # 2. Hopcroft–Karp for perfect matching
    left = [i for i in range(n) if color[i] == 0]
    right = [i for i in range(n) if color[i] == 1]
    # build adjacency from left to right with edge ids
    G = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if color[u] == 0:
            G[u].append((v, idx))
        else:
            G[v].append((u, idx))

    INF = 10 ** 9
    pair_u = [-1] * n
    pair_v = [-1] * n
    dist = [0] * n

    def bfs():
        q = deque()
        for u in left:
            if pair_u[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        d = INF
        while q:
            u = q.popleft()
            if dist[u] < d:
                for v, _ in G[u]:
                    if pair_v[v] == -1:
                        d = dist[u] + 1
                    elif dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        q.append(pair_v[v])
        return d != INF

    def dfs(u):
        for v, _ in G[u]:
            pu = pair_v[v]
            if pair_v[v] == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = INF
        return False

    matching_size = 0
    while bfs():
        for u in left:
            if pair_u[u] == -1 and dfs(u):
                matching_size += 1

    # matching must be perfect
    if matching_size * 2 != n:
        print("NO")
        return

    # collect matched edge ids
    matched_edge = set()
    for u in left:
        v = pair_u[u]
        # find edge id between u and v
        for to, eid in adj[u]:
            if to == v:
                matched_edge.add(eid)
                break

    # 3. colour edges
    ans = [0] * m
    for eid in matched_edge:
        ans[eid] = 1

    visited_edge = [False] * m
    for eid in matched_edge:
        visited_edge[eid] = True

    for start_eid in range(m):
        if visited_edge[start_eid]:
            continue
        # start a new cycle
        cur_eid = start_eid
        # determine starting vertex
        u, v = edges[cur_eid]
        # we will walk forward, remembering previous vertex
        prev = u
        cur = v
        colour = 2  # first edge of cycle gets colour 2
        while True:
            ans[cur_eid] = colour
            visited_edge[cur_eid] = True
            colour = 5 - colour  # toggle between 2 and 3 (2+3=5)

            # at vertex cur, there are two incident edges not in matching,
            # one is the edge we just came from (cur_eid), the other is next.
            # find the next edge id
            next_eid = None
            for to, eid in adj[cur]:
                if visited_edge[eid]:
                    continue
                # edge not in matching and not yet visited
                next_eid = eid
                nxt = to
                break
            if next_eid is None:
                break  # should not happen
            # move forward
            prev, cur = cur, nxt
            cur_eid = next_eid
            if cur_eid == start_eid:
                # completed the cycle
                ans[cur_eid] = colour
                visited_edge[cur_eid] = True
                break

    print("YES")
    print(' '.join(str(x) for x in ans))

if __name__ == "__main__":
    solve()