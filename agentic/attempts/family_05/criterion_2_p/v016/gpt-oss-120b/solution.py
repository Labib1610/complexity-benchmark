import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    adj = [[] for _ in range(k + 1)]          # u -> list of w
    f = [0] * (k + 1)                         # transmitter -> its fixed module
    for _ in range(t):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        if f[u] == 0:
            f[u] = v
        # else: input guarantees same v, ignore check
        adj[u].append(w)

    # quick check: any transmitter without edges -> impossible
    for u in range(1, k + 1):
        if not adj[u]:
            print("NO")
            return

    # Hopcroft–Karp
    INF = 10 ** 9
    pair_u = [0] * (k + 1)   # u -> w
    pair_w = [0] * (k + 1)   # w -> u (w also 1..k)
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
            for w in adj[u]:
                pu = pair_w[w]
                if pu == 0:
                    reachable = True
                elif dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
        return reachable

    def dfs(u: int) -> bool:
        for w in adj[u]:
            pu = pair_w[w]
            if pu == 0 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_u[u] = w
                pair_w[w] = u
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
    for u in range(1, k + 1):
        w = pair_u[u]
        out_lines.append(f"{u} {f[u]} {w}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()