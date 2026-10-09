import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n_left = q
    n_right = q  # platforms indexed 0..q-1 corresponding to q+1..2q
    adj = [[] for _ in range(n_left)]
    for _ in range(t):
        a = int(next(it)) - 1          # controller 0-index
        b = int(next(it)) - (q + 1)    # platform 0-index
        if 0 <= a < n_left and 0 <= b < n_right:
            adj[a].append(b)

    # Hopcroft–Karp
    INF = 10**9
    pair_u = [-1] * n_left
    pair_v = [-1] * n_right
    dist = [0] * n_left

    def bfs() -> bool:
        dq = deque()
        for u in range(n_left):
            if pair_u[u] == -1:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        reachable = False
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                pu = pair_v[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    dq.append(pu)
                elif pu == -1:
                    reachable = True
        return reachable

    def dfs(u: int) -> bool:
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

    out = []
    if matching == q:
        out.append("YES")
        for u in range(n_left):
            v = pair_u[u]
            # convert back to original numbering
            out.append(f"{u+1} {v+q+1}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()