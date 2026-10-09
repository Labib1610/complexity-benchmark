import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n_left = q
    n_right = q
    offset = q  # right nodes are offset+1 .. offset+q (i.e., q+1 .. 2q)

    adj = [[] for _ in range(n_left + 1)]
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        # a in [1,q], b in [q+1,2q]
        adj[a].append(b - offset)  # store right index 1..q

    # Hopcroft–Karp
    INF = 10 ** 9
    pair_u = [0] * (n_left + 1)   # left -> right (0 if nil)
    pair_v = [0] * (n_right + 1)  # right -> left
    dist = [0] * (n_left + 1)

    def bfs() -> bool:
        dq = deque()
        for u in range(1, n_left + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while dq:
            u = dq.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if pair_v[v] == 0:
                        if dist[0] == INF:
                            dist[0] = dist[u] + 1
                    elif dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        dq.append(pair_v[v])
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
        for u in range(1, n_left + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1

    if matching != q:
        sys.stdout.write("NO")
        return

    out_lines = ["YES"]
    for u in range(1, n_left + 1):
        v = pair_u[u] + offset  # convert back to original right node number
        out_lines.append(f"{u} {v}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()