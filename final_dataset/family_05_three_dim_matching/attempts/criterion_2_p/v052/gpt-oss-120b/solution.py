import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # store triples and verify one-to-one captain-cruiser mapping
    cap_to_cru = {}
    cru_to_cap = {}
    triples = []  # list of (c,v,s)
    cap_sector_edges = [[] for _ in range(k + 1)]  # 1-indexed captains
    cap_sector_map = {}  # (c,s) -> (c,v,s)

    for _ in range(t):
        c = int(next(it)); v = int(next(it)); s = int(next(it))
        triples.append((c, v, s))
        # enforce mapping (input guarantees it, we just record)
        if c in cap_to_cru:
            if cap_to_cru[c] != v:
                # inconsistent, impossible
                print("NO")
                return
        else:
            cap_to_cru[c] = v
        if v in cru_to_cap:
            if cru_to_cap[v] != c:
                print("NO")
                return
        else:
            cru_to_cap[v] = c
        cap_sector_edges[c].append(s)
        cap_sector_map[(c, s)] = (c, v, s)

    # all captains and cruisers must be present
    if len(cap_to_cru) != k or len(cru_to_cap) != k:
        print("NO")
        return

    # Hopcroft–Karp
    n_left = k
    n_right = k
    INF = 10 ** 9
    pair_u = [0] * (n_left + 1)   # captain -> sector
    pair_v = [0] * (n_right + 1)  # sector -> captain
    dist = [0] * (n_left + 1)

    adj = cap_sector_edges  # already 1-indexed

    def bfs() -> bool:
        q = deque()
        for u in range(1, n_left + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while q:
            u = q.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if pair_v[v] == 0:
                        if dist[0] == INF:
                            dist[0] = dist[u] + 1
                    elif dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        q.append(pair_v[v])
        return dist[0] != INF

    def dfs(u: int) -> bool:
        if u == 0:
            return True
        for v in adj[u]:
            if pair_v[v] == 0 or (dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v])):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(1, n_left + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1

    if matching != k:
        print("NO")
        return

    # construct answer
    print("YES")
    out_lines = []
    for c in range(1, k + 1):
        s = pair_u[c]
        triple = cap_sector_map[(c, s)]
        out_lines.append(f"{triple[0]} {triple[1]} {triple[2]}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()