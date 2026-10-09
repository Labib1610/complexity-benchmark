import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    p = [0] * (k + 1)          # key for each ground
    adj = [[] for _ in range(k + 1)]  # satellites reachable from ground
    seen_ground = [False] * (k + 1)

    for _ in range(t):
        x = int(next(it)); y = int(next(it)); z = int(next(it))
        if not seen_ground[x]:
            p[x] = y
            seen_ground[x] = True
        # else y must equal p[x] by problem guarantee
        adj[x].append(z)

    # any ground without any link -> impossible
    for x in range(1, k + 1):
        if not seen_ground[x] or not adj[x]:
            print("NO")
            return

    # Hopcroft–Karp
    INF = 10 ** 9
    pair_u = [0] * (k + 1)   # ground -> satellite
    pair_v = [0] * (k + 1)   # satellite -> ground (satellites also 1..k)
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
            if pair_v[v] == 0 or (dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v])):
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
    for x in range(1, k + 1):
        z = pair_u[x]
        out_lines.append(f"{x} {p[x]} {z}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()