import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    film_of = [0] * (k + 1)          # film_of[d] = f
    adj = [[] for _ in range(k + 1)]  # rooms reachable from director d
    for _ in range(t):
        d = int(next(it)); f = int(next(it)); s = int(next(it))
        if film_of[d] == 0:
            film_of[d] = f
        # else film_of[d] must equal f by problem statement
        adj[d].append(s)

    # quick check: every director must have at least one possible room
    for d in range(1, k + 1):
        if not adj[d]:
            print("NO")
            return

    # Hopcroft–Karp
    INF = 10 ** 9
    pair_u = [0] * (k + 1)   # director -> room
    pair_v = [0] * (k + 1)   # room -> director
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
    for d in range(1, k + 1):
        s = pair_u[d]
        out_lines.append(f"{d} {film_of[d]} {s}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()