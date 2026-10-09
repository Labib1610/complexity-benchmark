import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    adj = [[] for _ in range(k + 1)]          # 1-indexed pilots -> missions
    starfighter = [0] * (k + 1)               # pilot -> its starfighter

    for _ in range(t):
        p = int(next(it)); s = int(next(it)); m = int(next(it))
        if starfighter[p] == 0:
            starfighter[p] = s
        # else starfighter[p] is already set and must equal s (guaranteed by input)
        adj[p].append(m)

    # quick check: any pilot without edges -> impossible
    for p in range(1, k + 1):
        if not adj[p]:
            print("NO")
            return

    # Hopcroft–Karp
    INF = k + 5
    pair_u = [0] * (k + 1)   # pilot -> mission
    pair_v = [0] * (k + 1)   # mission -> pilot
    dist = [0] * (k + 1)

    def bfs() -> bool:
        q = deque()
        for u in range(1, k + 1):
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
            pu = pair_v[v]
            if pu == 0 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1

    if matching != k:
        print("NO")
        return

    print("YES")
    out_lines = []
    for p in range(1, k + 1):
        m = pair_u[p]
        s = starfighter[p]
        out_lines.append(f"{p} {s} {m}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()