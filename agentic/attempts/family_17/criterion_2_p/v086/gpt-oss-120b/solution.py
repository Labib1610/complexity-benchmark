import sys
from collections import deque

def hopcroft_karp(adj, n_left, n_right):
    INF = 10 ** 9
    pair_u = [-1] * n_left
    pair_v = [-1] * n_right
    dist = [0] * n_left

    def bfs():
        q = deque()
        for u in range(n_left):
            if pair_u[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                pu = pair_v[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                elif pu == -1:
                    found = True
        return found

    def dfs(u):
        for v in adj[u]:
            pu = pair_v[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(n_left):
            if pair_u[u] == -1 and dfs(u):
                matching += 1
    return matching, pair_u

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n_left = q
    n_right = q
    adj = [[] for _ in range(n_left)]
    for _ in range(t):
        a = int(next(it)) - 1          # 0‑based left
        b = int(next(it)) - (q + 1)    # right index 0…q-1
        if 0 <= a < n_left and 0 <= b < n_right:
            adj[a].append(b)

    size, pair_u = hopcroft_karp(adj, n_left, n_right)
    out = []
    if size == q:
        out.append("YES")
        for a in range(q):
            b = pair_u[a] + q + 1
            out.append(f"{a+1} {b}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()