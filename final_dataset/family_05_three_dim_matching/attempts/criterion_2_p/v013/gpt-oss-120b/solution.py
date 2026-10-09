import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    y_of = [0] * (k + 1)          # y_of[x] = unique machine for specialist x
    adj = [[] for _ in range(k + 1)]   # edges x -> z

    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        if y_of[x] == 0:
            y_of[x] = y
        # given constraints guarantee consistency, so we skip checks
        adj[x].append(z)

    # quick impossibility check
    for x in range(1, k + 1):
        if not adj[x]:
            print("NO")
            return

    # Hopcroft–Karp
    INF = k + 5
    pair_u = [0] * (k + 1)   # matched z for each x
    pair_v = [0] * (k + 1)   # matched x for each z
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
                pu = pair_v[v]
                if pu == 0:
                    reachable = True
                elif dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
        return reachable

    def dfs(u: int) -> bool:
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
    for x in range(1, k + 1):
        out_lines.append(f"{x} {y_of[x]} {pair_u[x]}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()