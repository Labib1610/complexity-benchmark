import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    y_of = [0] * (k + 1)          # y for each x
    adj = [[] for _ in range(k + 1)]
    # we may need to verify consistency, but problem guarantees it
    for _ in range(t):
        x = int(next(it)); y = int(next(it)); z = int(next(it))
        if y_of[x] == 0:
            y_of[x] = y
        # else: y_of[x] must equal y (guaranteed)
        adj[x].append(z)

    # quick check: any x without edges -> impossible
    for x in range(1, k + 1):
        if not adj[x]:
            print("NO")
            return

    # Hopcroft–Karp
    INF = k + 5
    pair_u = [0] * (k + 1)   # match for x (left)
    pair_v = [0] * (k + 1)   # match for z (right)
    dist = [0] * (k + 1)

    def bfs() -> bool:
        q = deque()
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        reachable = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                if pair_v[v] == 0:
                    reachable = True
                elif dist[pair_v[v]] == INF:
                    dist[pair_v[v]] = dist[u] + 1
                    q.append(pair_v[v])
        return reachable

    def dfs(u: int) -> bool:
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
        out_lines.append(f"{x} {y_of[x]} {z}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()